"""Performance benchmarks for flake8-import-guard using CodSpeed."""

import ast

import pytest

from src.main import Flake8ImportGuard


def generate_large_ast(num_imports: int) -> ast.AST:
    """Generate an AST with a specified number of import statements."""
    imports = []
    for i in range(num_imports):
        if i % 3 == 0:
            imports.append(f"import module_{i}")
        elif i % 3 == 1:
            imports.append(f"from package_{i} import func_{i}")
        else:
            imports.append(
                f"from package_{i}.submodule import Class_{i}, func_{i}"
            )

    code = "\n".join(imports)
    return ast.parse(code)


@pytest.mark.benchmark
def test_get_imports_performance():
    """Benchmark the get_imports method with various AST sizes."""
    small_ast = generate_large_ast(10)
    medium_ast = generate_large_ast(100)
    large_ast = generate_large_ast(1000)

    # Benchmark small AST
    imports = Flake8ImportGuard.get_imports(small_ast)
    assert len(imports) > 0

    # Benchmark medium AST
    imports = Flake8ImportGuard.get_imports(medium_ast)
    assert len(imports) > 0

    # Benchmark large AST
    imports = Flake8ImportGuard.get_imports(large_ast)
    assert len(imports) > 0


@pytest.mark.benchmark
def test_run_performance_with_forbidden_imports():
    """Benchmark the run method with various forbidden import configurations."""
    # Create AST with mixed imports
    code = """
import os
import sys
import subprocess
from typing import Any, Dict, List
from collections.abc import Generator
import json
import toml
from flake8.options.manager import OptionManager
import ast
from pathlib import Path
import logging
from datetime import datetime
import requests
"""
    tree = ast.parse(code)

    # Test with no forbidden imports
    checker = Flake8ImportGuard(tree, "test.py")
    checker.forbidden_imports = []
    list(checker.run())

    # Test with few forbidden imports
    checker.forbidden_imports = ["subprocess", "requests"]
    violations = list(checker.run())
    expected_violations = 2
    assert len(violations) == expected_violations

    # Test with many forbidden imports
    checker.forbidden_imports = [
        "os",
        "sys",
        "subprocess",
        "json",
        "toml",
        "ast",
        "logging",
        "requests",
        "pathlib",
    ]
    violations = list(checker.run())
    assert len(violations) > 0


@pytest.mark.benchmark
def test_import_checking_with_nested_modules():
    """Benchmark import checking with deeply nested module structures."""
    code = """
from package.subpackage.module import Class1, Class2, func1
from package.subpackage.subsubpackage.deep_module import DeepClass
from another.package.with_many.levels.of_nesting import NestedFunction
import package.subpackage.module
from typing import (
    Any, Dict, List, Optional, Union,
    Tuple, Set, Callable, TypeVar, Generic
)
"""
    tree = ast.parse(code)

    checker = Flake8ImportGuard(tree, "test.py")
    checker.forbidden_imports = ["package.subpackage", "levels.of.nesting"]

    violations = list(checker.run())
    min_expected_violations = 2
    assert len(violations) >= min_expected_violations


@pytest.mark.benchmark
def test_performance_with_complex_import_patterns():
    """Benchmark performance with complex import patterns and aliases."""
    # Generate code with aliased imports
    imports = []
    for i in range(50):
        imports.append(f"import module_{i} as m{i}")
        imports.append(f"from package_{i} import func_{i} as f{i}")

    code = "\n".join(imports)
    tree = ast.parse(code)

    checker = Flake8ImportGuard(tree, "test.py")
    # Set forbidden imports that will match some patterns
    checker.forbidden_imports = [f"module_{i}" for i in range(0, 50, 5)]

    violations = list(checker.run())
    expected_violations = 10  # Should match every 5th module
    assert len(violations) == expected_violations
