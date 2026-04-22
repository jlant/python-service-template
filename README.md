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

## Quick start

```bash
uv run pst --help
uv run pst hello
uv run pst hello -n Jeremiah
uv run pst read-config
uv run pst run
PST_LOG_LEVEL=DEBUG PST_RUN_SECONDS=0 uv run pst run
```

## Example - renaming the template
After creating a new repo with this template, you can rename
the template by running the `rename_template.py` script:

```bash
# Preview first
python scripts/rename_template.py my_service mst "My Service Template" --dry-run

# Then apply
python scripts/rename_template.py my_service mst "My Service"
```

then finalize and check is working properly by running:

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
uv run <new_cli_name> read-config

# Check template runs service
uv run <new_cli_name> run

```
