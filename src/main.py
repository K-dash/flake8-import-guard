import ast
import os
import subprocess
from typing import Any, Dict, Generator, List, Set, Tuple

import toml
from flake8.options.manager import OptionManager


class Flake8ImportGuard:
    """
    A Flake8 plugin to enforce import restrictions in Python code.

    This plugin checks for forbidden imports in Python files and reports violations.
    It supports configuration through Flake8's standard configuration system and pyproject.toml.
    """

    name = "flake8-import-guard"
    version = "0.1.5"
    forbidden_imports: List[str] = []

    def __init__(self, tree: ast.AST, filename: str):
        """
        Initialize the Flake8ImportGuard instance.

        Args:
            tree (ast.AST): The AST of the Python file to check.
            filename (str): The name of the file being checked.
        """
        self.tree = tree
        self.filename = filename

    @classmethod
    def add_options(cls, option_manager: OptionManager) -> None:
        """
        Add Flake8 command-line options for this plugin.

        Args:
            option_manager (OptionManager): Flake8's OptionManager instance.
        """
        option_manager.add_option(
            "--forbidden-imports",
            default="",
            parse_from_config=True,
            comma_separated_list=True,
            help="Comma-separated list of forbidden imports",
        )

    @classmethod
    def parse_options(cls, options: Any) -> None:
        """
        Parse the options provided by Flake8 and pyproject.toml.

        Args:
            options (Any): The options object provided by Flake8.
        """
        cls.forbidden_imports = options.forbidden_imports
        pyproject_config = cls.load_pyproject_config()
        if "forbidden_imports" in pyproject_config:
            cls.forbidden_imports.extend(pyproject_config["forbidden_imports"])

    @classmethod
    def load_pyproject_config(cls) -> Dict[str, List[str]]:
        """
        Load configuration from pyproject.toml file.

        Returns:
            Dict[str, List[str]]: Configuration dictionary from pyproject.toml.
        """
        try:
            with open("pyproject.toml", "r", encoding="utf-8") as f:
                config = toml.load(f)
            return config.get("tool", {}).get("flake8-import-guard", {})
        except FileNotFoundError:
            return {}

    @classmethod
    def get_imports(cls, tree: ast.AST) -> Set[str]:
        """
        Extract all imports from the given AST.

        Args:
            tree (ast.AST): The AST to extract imports from.

        Returns:
            Set[str]: A set of all imports found in the AST.
        """
        imports = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imports.update(alias.name for alias in node.names)
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    imports.update(
                        f"{node.module}.{alias.name}" for alias in node.names
                    )
                else:
                    imports.update(alias.name for alias in node.names)
        return imports

    def run(self) -> Generator[Tuple[int, int, str, type], None, None]:
        """
        Run the import check on the current file.

        Yields:
            Tuple[int, int, str, type]: Violations found in the format (line, col, message, type).
        """
        if not self.forbidden_imports:
            return

        is_new_file = not os.path.exists(self.filename)
        if not is_new_file:
            git_check = subprocess.run(
                ["git", "ls-files", "--error-unmatch", self.filename],
                capture_output=True,
                text=True,
                check=False,
            )
            is_new_file = git_check.returncode != 0

        current_imports = self.get_imports(self.tree)

        if is_new_file:
            imports_to_check = current_imports
            previous_imports = set()
        else:
            try:
                result = subprocess.run(
                    ["git", "show", f"HEAD:{self.filename}"],
                    capture_output=True,
                    text=True,
                    check=True,
                )
                previous_content = result.stdout
                previous_tree = ast.parse(previous_content)
                previous_imports = self.get_imports(previous_tree)
                imports_to_check = current_imports - previous_imports
            except subprocess.CalledProcessError:
                imports_to_check = current_imports
                previous_imports = set()

        for node in ast.walk(self.tree):
            if not isinstance(node, (ast.Import, ast.ImportFrom)):
                continue
            for alias in node.names:
                import_name = (
                    alias.name
                    if isinstance(node, ast.Import)
                    else (f"{node.module}.{alias.name}")
                )
                if import_name in imports_to_check:
                    for forbidden in self.forbidden_imports:
                        if forbidden in import_name:
                            yield (
                                node.lineno,
                                node.col_offset,
                                f"CPE001 Forbidden import found: {import_name}",
                                type(self),
                            )
                            break

    def __iter__(self):
        """
        Make the class iterable, returning the run generator.

        Returns:
            Generator: The run method's generator.
        """
        return self.run()
