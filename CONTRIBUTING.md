# Contributing to python-service-template
Thank you for considering contributing to Python Service Template.

To maintain code quality and a smooth workflow, please take a moment to review these guidelines.

## Development workflow

```bash
uv lock
uv sync --all-extras --dev
pre-commit install

# Format
uv run nox -s fmt

# Lint + type check
uv run nox -s lint

# Run tests
uv run nox -s tests

# Check template reads config file
uv run pst read-config

# Check template runs service
uv run pst run

```
