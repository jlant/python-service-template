from __future__ import annotations

import tomllib
from dataclasses import dataclass
from pathlib import Path

DEFAULT_APP_NAME = "python-service-template"
DEFAULT_LOG_LEVEL = "INFO"


@dataclass(frozen=True)
class Settings:
    app_name: str = DEFAULT_APP_NAME
    log_level: str = DEFAULT_LOG_LEVEL


def load_settings(path: Path) -> Settings:
    """Load settings from a TOML file. Missing file => defaults.

    Expected TOML shape:

    [app]
    name = "..."
    log_level = "..."
    """
    if not path.exists():
        return Settings()

    data = tomllib.loads(path.read_text(encoding="utf-8"))
    app = data.get("app", {})

    return Settings(
        app_name=str(app.get("name", DEFAULT_APP_NAME)),
        log_level=str(app.get("log_level", DEFAULT_LOG_LEVEL)),
    )
