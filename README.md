# python-service-template

A minimal, production-grade Python service template with a CLI interface.

- uv
- src/ layout
- ruff
- pyright
- pytest
- nox
- pre-commit
- GitHub Actions
- Typer for CLI
- TOML as the default config format
- YAML only for multi-step orchestration

## Development workflow

```bash
uv sync --all-extras --dev
pre-commit install

# Format
uv run nox -s fmt

# Lint + type check
uv run nox -s lint

# Run tests
uv run nox -s tests

```
## Quick start

```bash
uv run ppt hello
uv run ppt hello -n Jeremiah
uv run ppt read-config
uv run ppt read-config -c config/app.toml
```

## Example - renaming the template
After creating a new repo with this template, you can rename
the template by running the `rename_template.sh` script:

```bash
./scripts/rename_template.sh mypkg mycli "My Project"
uv lock
uv sync --all-extras --dev
pre-commit install
uv run nox -s fmt
uv run nox -s lint
uv run nox -s tests
```
