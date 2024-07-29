import ast
import subprocess
from unittest.mock import MagicMock, patch

import pytest

from src.main import Flake8ImportGuard


@pytest.fixture
def enforcer():
    def _create_enforcer(code="", filename="test_file.py"):
        tree = ast.parse(code)
        return Flake8ImportGuard(tree, filename)

    return _create_enforcer


def test_get_imports(enforcer):
    code = "import os\nfrom datetime import datetime"
    test_enforcer = enforcer(code)
    imports = test_enforcer.get_imports(test_enforcer.tree)
    assert imports == {"os", "datetime.datetime"}


def test_run_with_forbidden_import(enforcer):
    code = "from dotenv import load_dotenv"
    test_enforcer = enforcer(code)
    test_enforcer.config = {"forbidden_imports": ["load_dotenv"]}
    violations = list(test_enforcer.run())
    assert len(violations) == 1
    assert violations[0][2] == (
        "CPE001 Forbidden import found: dotenv.load_dotenv"
    )


def test_run_with_allowed_import(enforcer):
    code = "import os"
    test_enforcer = enforcer(code)
    test_enforcer.config = {"forbidden_imports": ["load_dotenv"]}
    violations = list(test_enforcer.run())
    assert len(violations) == 0


@pytest.mark.parametrize(
    (
        "is_new_file",
        "previous_content",
        "current_content",
        "expected_violations",
    ),
    [
        # 新規ファイル
        (True, "", "from dotenv import load_dotenv", 1),
        # 既存ファイルに新しい禁止インポートを追加j
        (False, "import os", "import os\nfrom dotenv import load_dotenv", 1),
        # 既存ファイルに変更なし
        (
            False,
            "from dotenv import load_dotenv",
            "from dotenv import load_dotenv",
            0,
        ),
    ],
)
def test_run_with_different_file_states(
    enforcer,
    is_new_file,
    previous_content,
    current_content,
    expected_violations,
):
    test_enforcer = enforcer(current_content)
    with patch("os.path.exists", return_value=not is_new_file), patch(
        "subprocess.run"
    ) as mock_run:
        mock_run.side_effect = [
            MagicMock(returncode=1 if is_new_file else 0),
            MagicMock(stdout=previous_content, returncode=0)
            if not is_new_file
            else MagicMock(returncode=1),
        ]

        test_enforcer.config = {"forbidden_imports": ["load_dotenv"]}
        violations = list(test_enforcer.run())

        print(f"Test case - Is new file: {is_new_file}")
        print(f"Test case - Previous content: {previous_content}")
        print(f"Test case - Current content: {current_content}")
        print(f"Test case - Expected violations: {expected_violations}")
        print(f"Test case - Actual violations: {violations}")

    assert len(violations) == expected_violations, (
        f"Expected {expected_violations} violations, "
        f"but got {len(violations)}\nViolations: {violations}"
    )
    if expected_violations > 0:
        assert any(
            "load_dotenv" in v[2] for v in violations
        ), "Expected violation for 'load_dotenv' not found"


def test_add_options():
    option_manager = MagicMock()
    Flake8ImportGuard.add_options(option_manager)
    option_manager.add_option.assert_called_once_with(
        "--enforce-patterns",
        default="",
        parse_from_config=True,
        comma_separated_list=True,
        help="Comma-separated list of import patterns to enforce",
    )


def test_parse_options():
    options = MagicMock()
    options.enforce_patterns = ["pattern1", "pattern2"]
    Flake8ImportGuard.parse_options(options)
    assert Flake8ImportGuard.enforce_patterns == ["pattern1", "pattern2"]


def test_run_empty_forbidden_imports(enforcer):
    test_enforcer = enforcer("")
    test_enforcer.config = {"forbidden_imports": []}
    assert list(test_enforcer.run()) == []


def test_run_git_check(enforcer):
    with patch("os.path.exists", return_value=True), patch(
        "subprocess.run"
    ) as mock_run:
        mock_run.side_effect = [
            MagicMock(returncode=1),  # git ls-files
            MagicMock(returncode=1),  # git show (fails)
        ]
        test_enforcer = enforcer("import os")
        test_enforcer.config = {"forbidden_imports": ["os"]}
        violations = list(test_enforcer.run())
        assert len(violations) == 1


def test_run_git_command_fails(enforcer):
    with patch("os.path.exists", return_value=True), patch(
        "subprocess.run"
    ) as mock_run:
        mock_run.side_effect = [
            MagicMock(returncode=0),  # git ls-files
            subprocess.CalledProcessError(1, "git show"),  # git show (fails)
        ]
        test_enforcer = enforcer("import os")
        test_enforcer.config = {"forbidden_imports": ["os"]}
        violations = list(test_enforcer.run())
        assert len(violations) == 1


def test_get_imports_with_module(enforcer):
    code = "from os import path"
    test_enforcer = enforcer(code)
    imports = test_enforcer.get_imports(test_enforcer.tree)
    assert imports == {"os.path"}


def test_get_imports_without_module(enforcer):
    code = "from . import some_function"
    test_enforcer = enforcer(code)
    imports = test_enforcer.get_imports(test_enforcer.tree)
    assert imports == {"some_function"}
