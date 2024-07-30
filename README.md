# Flake8 Import Guard

Flake8 Import Guard is a Flake8 plugin that helps enforce import restrictions in your Python projects. It allows you to specify forbidden imports and detects their usage in your codebase, focusing on newly added imports in version-controlled files.

## Features

- Detects forbidden imports in Python files
- Supports configuration through Flake8's standard configuration system and `pyproject.toml`
- Focuses on newly added imports, ignoring existing ones in version-controlled files
- Easy integration with existing Flake8 setups

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
