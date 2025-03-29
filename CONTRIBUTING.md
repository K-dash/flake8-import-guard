# Contributing to Flake8 Import Guard

We're thrilled that you're interested in contributing to Flake8 Import Guard! This document provides guidelines for contributions to make the process smooth and effective for everyone involved.

## Code of Conduct

By participating in this project, you are expected to uphold our Code of Conduct. Please report unacceptable behavior to ["K' <51281148+K-dash@users.noreply.github.com>"].

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

This project uses `uv` as its Python project management tool for fast, reliable dependency management and virtual environment handling.

To set up Flake8 Import Guard for development:

1. Install `uv` first if you haven't already:

   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

   For other installation methods, please refer to the [uv documentation](https://docs.astral.sh/uv/).

2. Fork and clone the repo.

3. Install dependencies and activate the virtual environment:

   ```
   make install
   ```

4. Run tests to ensure everything is set up correctly:

   ```
   make all

   or

   make output_cov
   ```

> [!NOTE]
> This project uses `Makefile` as a task runner. You need to set up your environment to be able to run the `make` command.

## Styleguides

### Git Commit Messages

### Git Commit Messages

This project uses the [Conventional Commits](https://www.conventionalcommits.org/) format for all commit messages. This enables automatic versioning and changelog generation.

Your commit messages should follow this structure:

```
<type>(<scope>): <description>

[optional body]

[optional footer(s)]
```

Where `<type>` is one of:

- **feat**: A new feature
- **fix**: A bug fix
- **docs**: Documentation only changes
- **style**: Changes that do not affect the meaning of the code
- **refactor**: A code change that neither fixes a bug nor adds a feature
- **perf**: A code change that improves performance
- **test**: Adding missing tests or correcting existing tests
- **ci**: Changes to CI configuration files and scripts
- **chore**: Other changes that don't modify source or test files

Examples:

```
feat(parser): add ability to parse arrays
fix(import): resolve issue with wildcard imports
docs(readme): update installation instructions
```

Using this format helps in automatic versioning where:

- `fix` triggers a PATCH release (1.0.0 -> 1.0.1)
- `feat` triggers a MINOR release (1.0.0 -> 1.1.0)
- `feat` or `fix` with `BREAKING CHANGE` in the footer triggers a MAJOR release (1.0.0 -> 2.0.0)### Python Styleguide

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
