# Contributing to Flake8 Import Guard

We're thrilled that you're interested in contributing to Flake8 Import Guard! This document provides guidelines for contributions to make the process smooth and effective for everyone involved.

## Code of Conduct

By participating in this project, you are expected to uphold our Code of Conduct. Please report unacceptable behavior to [project_email@example.com].

## How Can I Contribute?

### Reporting Bugs

- Ensure the bug was not already reported by searching on GitHub under [Issues](https://github.com/yourusername/flake8-import-guard/issues).
- If you're unable to find an open issue addressing the problem, [open a new one](https://github.com/yourusername/flake8-import-guard/issues/new). Be sure to include a title and clear description, as much relevant information as possible, and a code sample or an executable test case demonstrating the expected behavior that is not occurring.

### Suggesting Enhancements

- Open a new issue with a clear title and detailed description of the suggested enhancement.
- Provide examples and explain why this enhancement would be useful to most users.

### Pull Requests

1. Fork the repo and create your branch from `main`.
2. If you've added code that should be tested, add tests.
3. If you've changed APIs, update the `README.md`.
4. Ensure the test suite passes.
5. Make sure your code lints.
6. Issue that pull request!

## Development Setup

To set up Flake8 Import Guard for development:

1. Fork and clone the repo.
2. Install dependencies and Activate the virtual environment.
   ```
   make install
   ```
3. Run tests to ensure everything is set up correctly:
   ```
   make all

   or

   make output_cov
   ```

> [!NOTE]
> This project uses `Makefile` as a task runner. You need to set up your environment to be able to run the `make` command.

## Styleguides

### Git Commit Messages

- Please comply with the [Semantic Commit Message](https://gist.github.com/joshbuchea/6f47e86d2510bce28f8e7f42ae84c716) and [Commit Message Guideline](https://gist.github.com/robertpainsi/b632364184e70900af4ab688decf6f53)

### Python Styleguide

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/).
- This is achieved using the `ruff` Linter and Formatter.
- Use type hints where possible.

### Documentation Styleguide

- Use [Markdown](https://daringfireball.net/projects/markdown/) for documentation.
- Reference functions and classes appropriately.

## Additional Notes

### Issue and Pull Request Labels

- `bug`: Something isn't working
- `enhancement`: New feature or request
- `documentation`: Improvements or additions to documentation
- `good first issue`: Good for newcomers

Thank you for contributing to Flake8 Import Guard!
