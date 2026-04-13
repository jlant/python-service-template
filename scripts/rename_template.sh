#!/usr/bin/env bash
set -euo pipefail

# Usage:
#   ./scripts/rename_template.sh new_pkg_name new_cli_name new_project_name
#
# Example:
#   ./scripts/rename_template.sh mypkg mycli "My Project"

NEW_PKG="${1:?new package import name (e.g. mypkg)}"
NEW_CLI="${2:?new cli command (e.g. mycli)}"
NEW_PROJ="${3:?new project display name (e.g. My Project)}"

OLD_PKG="python_service_template"
OLD_CLI="pst"

# Rename package directory
if [[ -d "src/${OLD_PKG}" ]]; then
  git mv "src/${OLD_PKG}" "src/${NEW_PKG}" 2>/dev/null || mv "src/${OLD_PKG}" "src/${NEW_PKG}"
fi

# Replace strings (simple heuristic)
python - "$NEW_PKG" "$NEW_CLI" "$NEW_PROJ" <<'PY'
import pathlib
import sys

NEW_PKG = sys.argv[1]
NEW_CLI = sys.argv[2]
NEW_PROJ = sys.argv[3]
OLD_PKG = "python_service_template"
OLD_CLI = "pst"

for p in pathlib.Path(".").rglob("*"):
    if p.is_dir():
        continue
    if any(
        part in {".venv", ".git", "__pycache__", ".ruff_cache", ".pytest_cache", ".mypy_cache"}
        for part in p.parts
    ):
        continue
    if p.suffix in {".png", ".jpg", ".jpeg", ".gif", ".pdf", ".zip"}:
        continue

    try:
        txt = p.read_text(encoding="utf-8")
    except Exception:
        continue

    txt2 = txt
    txt2 = txt2.replace('name = "python_service_template"', f'name = "{NEW_PKG}"')
    txt2 = txt2.replace('app_name: str = "python_service_template"', f'app_name: str = "{NEW_PKG}"')
    txt2 = txt2.replace('app_name=str(app.get("name", "python_service_template"))', f'app_name=str(app.get("name", "{NEW_PKG}"))')
    txt2 = txt2.replace('pst = "python_service_template.cli:app"', f'{NEW_CLI} = "{NEW_PKG}.cli:app"')
    txt2 = txt2.replace('print(f"pst {version(\'python_service_template\')}")', f'print(f"{NEW_CLI} {{version(\'{NEW_PKG}\')}}")')
    txt2 = txt2.replace('print("pst 0.1.0")', f'print("{NEW_CLI} 0.1.0")')
    txt2 = txt2.replace("from python_service_template.", f"from {NEW_PKG}.")
    txt2 = txt2.replace('"python_service_template.', f'"{NEW_PKG}.')
    txt2 = txt2.replace("src/python_service_template", f"src/{NEW_PKG}")
    txt2 = txt2.replace("# python-service-template", f"# {NEW_PROJ}")

    if txt2 != txt:
        p.write_text(txt2, encoding="utf-8")
PY

echo "Renamed package to '${NEW_PKG}', CLI to '${NEW_CLI}', project to '${NEW_PROJ}'."
echo "Next steps:"
echo "  uv lock"
echo "  uv sync --all-extras --dev"
echo "  pre-commit install"
echo "  uv run nox -s lint"
echo "  uv run nox -s tests"
