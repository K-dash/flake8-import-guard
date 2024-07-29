import ast
import os
import subprocess
from typing import Any, Dict, Generator, List, Set, Tuple

import toml
from flake8.options.manager import OptionManager


class Flake8ImportGuard:
    name = "flake8-import-guard"
    version = "0.1.0"

    def __init__(self, tree: ast.AST, filename: str):
        self.tree = tree
        self.filename = filename
        self.config = self.load_config()

    @staticmethod
    def load_config() -> Dict[str, List[str]]:
        try:
            with open("pyproject.toml", "r", encoding="utf-8") as f:
                config = toml.load(f)
            return config.get("tool", {}).get("flake8-import-guard", {})
        except FileNotFoundError:
            return {}

    @staticmethod
    def add_options(option_manager: OptionManager) -> None:
        option_manager.add_option(
            "--enforce-patterns",
            default="",
            parse_from_config=True,
            comma_separated_list=True,
            help="Comma-separated list of import patterns to enforce",
        )

    @classmethod
    def parse_options(cls, options: Any) -> None:
        cls.enforce_patterns = options.enforce_patterns

    def run(self) -> Generator[Tuple[int, int, str, type], None, None]:
        forbidden_imports = self.config.get("forbidden_imports", [])
        if not forbidden_imports:
            return

        # 新規ファイルかどうかを確認
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
            # 新規ファイルの場合は全てのimportをチェック
            imports_to_check = current_imports
            previous_imports = set()
        else:
            # 既存ファイルの場合は前回のコミットの状態を取得
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
                # Gitコマンドが失敗した場合（例：初回コミット前）は
                # 全てのimportをチェック
                imports_to_check = current_imports
                previous_imports = set()

        # デバッグ用の出力
        print(f"Is new file: {is_new_file}")
        print(f"Current imports: {current_imports}")
        print(f"Previous imports: {previous_imports}")
        print(f"Imports to check: {imports_to_check}")

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
                    for forbidden in forbidden_imports:
                        if forbidden in import_name:
                            yield (
                                node.lineno,
                                node.col_offset,
                                f"CPE001 Forbidden import found: {import_name}",
                                type(self),
                            )
                            break  # 同じimportに対して複数の違反を報告しない

    @classmethod
    def get_imports(cls, tree: ast.AST) -> Set[str]:
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

    def __iter__(self):
        return self.run()
