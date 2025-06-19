
![GitHub License](https://img.shields.io/github/license/K-dash/flake8-import-guard)
[![PyPI version](https://img.shields.io/pypi/v/flake8-import-guard.svg)](https://pypi.org/project/flake8-import-guard/)
[![Downloads](https://static.pepy.tech/badge/flake8-import-guard)](https://pepy.tech/project/flake8-import-guard)
![Static Badge](https://img.shields.io/badge/Flake8-%5Ev7.1.0-blue?style=flat)
[![Python versions](https://img.shields.io/pypi/pyversions/flake8-import-guard.svg)](https://pypi.org/project/flake8-import-guard/)
[![codecov](https://codecov.io/gh/K-dash/flake8-import-guard/graph/badge.svg?token=4GG16B2ZU0)](https://codecov.io/gh/K-dash/flake8-import-guard)
![GitHub last commit](https://img.shields.io/github/last-commit/K-dash/flake8-import-guard)
[![CI](https://github.com/K-dash/flake8-import-guard/actions/workflows/ci.yml/badge.svg)](https://github.com/K-dash/flake8-import-guard/actions/workflows/ci.yml)
[![CodeQL](https://github.com/K-dash/flake8-import-guard/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/K-dash/flake8-import-guard/actions/workflows/github-code-scanning/codeql)

<p align="center">
  <img src="https://github.com/user-attachments/assets/7f4a88d5-c52a-473f-bfa3-8eca21fa5c54" />
</p>




Flake8 Import Guard is a Flake8 plugin that helps enforce import restrictions in your Python projects. It allows you to specify forbidden imports and detects their usage in your codebase, focusing on newly added imports in version-controlled files.

- [flake8-import-guard on PyPI](https://pypi.org/project/flake8-import-guard/)
- [Introductory post on reddit](https://www.reddit.com/r/Python/comments/1eoip79/flake8_import_guard_automate_import_restriction/)

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
 
- **Guardrail for AI-Powered Development**
    - As AI coding assistants become more common, they may introduce unintended or forbidden libraries. This plugin acts as a safety guardrail, automatically blocking prohibited imports in AI-generated code. This ensures that all code, whether written by humans or AI, adheres to your project's security, licensing, and architectural standards.

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

## Recommended Integration

It is highly recommended to integrate Flake8 Import Guard into your pre-commit hooks and CI workflows. This ensures that import restrictions are enforced consistently across your development process, catching potential violations early and maintaining code quality standards.

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

`flake8-import-guard` uses Git to detect changes in your codebase and enforce import restrictions. Here's a detailed explanation of its operation.


1. For new files
   - It checks all imports against the forbidden list.
   - Any import found in the forbidden list is reported as a violation.

2. For existing files
   - It compares the current version with the last committed version to identify newly added imports.
   - Only newly added imports that match the forbidden list are reported as violations.

> [!IMPORTANT]
> If a forbidden import already exists in the file at the time of introducing `flake8-import-guard`, it will not be detected as a violation. The plugin focuses only on new changes to prevent disruption to existing codebases.

3. Violation reporting
   - Only newly added imports that match the forbidden list are reported as violations.
   - This approach allows for gradual implementation of import restrictions without causing immediate breaks in existing code.

This behavior ensures that introducing `flake8-import-guard` to an existing project doesn't immediately flag all existing forbidden imports, allowing for a smoother integration and gradual code improvement.


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
