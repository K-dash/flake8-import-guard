
![GitHub License](https://img.shields.io/github/license/K-dash/flake8-import-guard)
[![PyPI version](https://img.shields.io/pypi/v/flake8-import-guard.svg)](https://pypi.org/project/flake8-import-guard/)
[![Python versions](https://img.shields.io/pypi/pyversions/flake8-import-guard.svg)](https://pypi.org/project/flake8-import-guard/)
[![codecov](https://codecov.io/gh/K-dash/flake8-import-guard/graph/badge.svg?token=4GG16B2ZU0)](https://codecov.io/gh/K-dash/flake8-import-guard)
![GitHub last commit](https://img.shields.io/github/last-commit/K-dash/flake8-import-guard)


# Flake8 Import Guard 💂

Flake8 Import Guard is a Flake8 plugin that helps enforce import restrictions in your Python projects. It allows you to specify forbidden imports and detects their usage in your codebase, focusing on newly added imports in version-controlled files.

[flake8-import-guard on PyPI](https://pypi.org/project/flake8-import-guard/)

## Features

- 🚫 Detects forbidden imports in new and modified files
- 🔧 Configurable via .flake8 or pyproject.toml
- 🔍 Focuses on newly added imports in Git-versioned files
- 🔗 Seamless integration with existing Flake8 workflows

## Motivation

Flake8 Import Guard is designed to address several common challenges in Python development.

- **Enforcing Security Measures**
    - Prevent the use of potentially unsafe or deprecated modules, enhancing the overall security of your codebase.
    - Prevent the import of forbidden external libraries, maintaining better control over your project's external dependencies.

- **Dependency Management**
    - Restrict and control project dependencies, reducing complexity and potential conflicts.

- **License Compliance**
    - Ensure compliance with licensing requirements by preventing the use of libraries with incompatible licenses.

- **Performance Optimization**
    - Avoid the use of heavyweight or inefficient imports that could impact performance.

- **Coding Standards Enforcement**
    - Maintain consistent coding standards across your project by enforcing specific import patterns.

- **Gradual Deprecation of Legacy Code**
    - Facilitate the phasing out of old modules or deprecated imports as your project evolves.

By using Flake8 Import Guard, development teams can proactively manage their codebase, ensuring better quality, security, and maintainability of their Python projects.

## Installation

You can install Flake8 Import Guard using pip.

```
pip install flake8-import-guard
```

## Usage

Once installed, Flake8 Import Guard will automatically be used by Flake8. You can run it using the standard Flake8 command.

```
flake8 path/to/your/code
```

## Configuration

You can configure Flake8 Import Guard using Flake8's standard configuration system or through `pyproject.toml`.

For example, let's say you want to prohibit the use of `load_dotenv` and `subprocess` in your project. Here's how you would configure that.

### Using Flake8 Configuration

Add the following to your `.flake8` file.

```ini
[flake8]
forbidden_imports = load_dotenv,subprocess
```

### Using pyproject.toml

Add the following to your `pyproject.toml` file.

```toml
[tool.flake8-import-guard]
forbidden_imports = [
    "load_dotenv",
    "subprocess"
]
```

## Example

### Configuration

Let's say you have the following configuration in your `.flake8` file.

```ini
[flake8]
forbidden_imports = load_dotenv,subprocess
```

### Sample Python File

Consider the following Python file.

```python
# test_file.py
import os
from datetime import datetime

from subprocess import check_output  # Violation Module

from dotenv import load_dotenv       # Violation Module

def main():
    pass

if __name__ == "__main__":
    main()
```

### Execution and Result

When you run Flake8 on this file, you'll get the following output.

```console
$ flake8 test_file.py
test_file.py:4:1: CPE001 Forbidden import found: subprocess.check_output
test_file.py:6:1: CPE001 Forbidden import found: dotenv.load_dotenv
```

## How It Works

Flake8 Import Guard uses Git to detect changes in your codebase.

1. For new files, it checks all imports against the forbidden list.
2. For existing files, it compares the current version with the last committed version to identify newly added imports.
3. Only newly added imports that match the forbidden list are reported as violations.

## Capabilities and Limitations

### What It Can Do

- Detect newly added forbidden imports in both new and existing files
- Work with Git-versioned projects
- Configure forbidden imports through Flake8 config or pyproject.toml
- Integrate seamlessly with existing Flake8 workflows

### What It Cannot Do

- Work in non-Git environments
- Identify removed or modified imports (focus is on new additions only)
- Detect indirect imports (e.g., imports within imported modules)

## Error Codes

- CPE001: Forbidden import found

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
See [CONTRIBUTING.md](https://github.com/K-dash/flake8-import-guard/blob/main/CONTRIBUTING.md) to get an idea of how contributions work.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
