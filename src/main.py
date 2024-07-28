"""
Flake8 plugin to detect and enforce code patterns in Python files.

This plugin checks for newly added occurrences of specified patterns
in modified files within a Git repository.
It can be used to enforce coding standards, prevent usage of
certain functions or variables, or maintain security practices.
"""

import ast
import os
import subprocess
from typing import Any, List, Set, Tuple


class CodePatternVisitor(ast.NodeVisitor):
    """
    AST visitor to find occurrences of specified patterns in the code.

    This visitor traverses the Abstract Syntax Tree (AST) of Python code and
    records the locations where specified patterns are found in identifiers,
    function names, class names, or string literals.
    """

    def __init__(self, target_patterns: Set[str]):
        """
        Initialize the CodePatternVisitor.

        Args:
            target_patterns (Set[str]):
                A set of string patterns to search for in the code.
        """
        self.target_patterns = target_patterns
        self.pattern_occurrences = {pattern: [] for pattern in target_patterns}

    def visit(self, node):
        """
        Visit a node in the AST and check for target patterns.

        This method is called for every node in the AST.
        It checks if any of the target patterns are present in the node's
        name, id, or string content.

        Args:
            node (ast.AST): The AST node being visited.
        """
        for pattern in self.target_patterns:
            if (
                hasattr(node, "name")
                and isinstance(node.name, str)
                and pattern in node.name
            ):
                self.pattern_occurrences[pattern].append((
                    node.lineno,
                    node.col_offset,
                ))
            elif (
                hasattr(node, "id")
                and isinstance(node.id, str)
                and pattern in node.id
            ):
                self.pattern_occurrences[pattern].append((
                    node.lineno,
                    node.col_offset,
                ))
            elif isinstance(node, ast.Str) and pattern in node.s:
                self.pattern_occurrences[pattern].append((
                    node.lineno,
                    node.col_offset,
                ))
        self.generic_visit(node)


def get_git_root() -> str:
    """
    Get the root directory of the current Git repository.

    Returns:
        str: The path to the Git root directory,
        or None if not in a Git repository.
    """
    try:
        return (
            subprocess.check_output(["git", "rev-parse", "--show-toplevel"])
            .decode("utf-8")
            .strip()
        )
    except subprocess.CalledProcessError:
        return None


def get_git_staged_and_modified_files() -> List[str]:
    """
    Get a list of staged and modified files in the current Git repository.

    Returns:
        List[str]: A list of file paths that are either staged or modified.
    """
    git_root = get_git_root()
    if not git_root:
        return []
    try:
        staged = (
            subprocess.check_output(
                ["git", "diff", "--cached", "--name-only"], cwd=git_root
            )
            .decode("utf-8")
            .splitlines()
        )
        modified = (
            subprocess.check_output(
                ["git", "diff", "--name-only"], cwd=git_root
            )
            .decode("utf-8")
            .splitlines()
        )
        return list(set(staged + modified))
    except subprocess.CalledProcessError:
        return []


class Flake8CodePatternEnforcer:
    """
    Flake8 plugin to enforce code patterns in Python files.

    This plugin checks for newly added occurrences of specified patterns in
    modified files within a Git repository. It can be used to enforce coding
    standards, prevent usage of certain functions or variables, or maintain
    security practices.
    """

    name = "flake8-code-pattern-enforcer"
    version = "0.3.1"

    def __init__(self, tree: ast.AST, filename: str = ""):
        """
        Initialize the Flake8CodePatternEnforcer.

        Args:
            tree (ast.AST): The AST of the file being checked.
            filename (str): The name of the file being checked.
        """
        self.tree = tree
        self.filename = filename

    @classmethod
    def add_options(cls, parser):
        """
        Add custom options to the Flake8 command-line parser.

        Args:
            parser: The OptionManager instance used by Flake8.
        """
        parser.add_option(
            "--target-patterns",
            default="[load_dotenv]",
            parse_from_config=True,
            help="List of patterns to detect, enclosed in square brackets",
        )

    @classmethod
    def parse_options(cls, options):
        """
        Parse the custom options provided to the plugin.

        This method processes the 'target-patterns' option, converting it from
        a string to a set of patterns.

        Args:
            options: The parsed options from Flake8.
        """
        # Remove square brackets and split by comma
        patterns = options.target_patterns.strip("[]").split(",")
        # Remove whitespace and filter out empty strings
        cls.target_patterns = set(
            pattern.strip() for pattern in patterns if pattern.strip()
        )

    def run(self) -> List[Tuple[int, int, str, Any]]:
        """
        Run the plugin on the current file.

        This method checks if the file is in a Git repository and
        has been modified. If so, it compares the current version
        with the previous version to detect
        newly added occurrences of the target patterns.

        Returns:
            List[Tuple[int, int, str, Any]]: A list of Flake8 error tuples.
            Each tuple contains the line number, column number, error message,
            and type of the error.
        """
        if not self.filename:
            return []

        git_root = get_git_root()
        if not git_root:
            return []  # Not in a git repository

        relative_filename = os.path.relpath(self.filename, git_root)
        modified_files = get_git_staged_and_modified_files()

        if relative_filename not in modified_files:
            return []  # File not modified

        visitor = CodePatternVisitor(self.target_patterns)
        visitor.visit(self.tree)

        try:
            old_content = subprocess.check_output(
                ["git", "show", f"HEAD:{relative_filename}"],
                cwd=git_root,
                stderr=subprocess.DEVNULL,
            ).decode("utf-8")
            old_tree = ast.parse(old_content)
            old_visitor = CodePatternVisitor(self.target_patterns)
            old_visitor.visit(old_tree)

            results = []
            for pattern, occurrences in visitor.pattern_occurrences.items():
                new_occurrences = set(occurrences) - set(
                    old_visitor.pattern_occurrences[pattern]
                )
                for lineno, col_offset in new_occurrences:
                    results.append((
                        lineno,
                        col_offset,
                        f'CPE001 New occurrence of "{pattern}" added.'
                        f"This is not allowed in this project."
                        f"Please remove or revise this code.",
                        type(self),
                    ))

            return results

        except subprocess.CalledProcessError:
            # File is new, all occurrences are considered new
            return [
                (
                    lineno,
                    col_offset,
                    f'CPE001 New occurrence of "{pattern}" found in a new file.'
                    f"This is not allowed in this project."
                    f"Please remove or revise this code.",
                    type(self),
                )
                for pattern, occurrences in visitor.pattern_occurrences.items()
                for lineno, col_offset in occurrences
            ]
