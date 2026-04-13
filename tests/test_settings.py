from pathlib import Path

from python_service_template.settings import load_settings


def test_load_settings_from_toml_file(tmp_path: Path) -> None:
    path = tmp_path / "app.toml"
    path.write_text(
        """
[app]
name = "demo-app"
log_level = "DEBUG"
""".strip(),
        encoding="utf-8",
    )

    settings = load_settings(path)

    assert settings.app_name == "demo-app"
    assert settings.log_level == "DEBUG"


def test_load_settings_missing_toml_file(tmp_path: Path) -> None:
    s = load_settings(tmp_path / "missing.toml")
    assert s.app_name == "python-service-template"
    assert s.log_level == "INFO"


def test_load_settings_without_app_table(tmp_path: Path) -> None:
    path = tmp_path / "app.toml"
    path.write_text(
        """
[other]
value = 1
""".strip(),
        encoding="utf-8",
    )

    settings = load_settings(path)

    assert settings.app_name == "python-service-template"
    assert settings.log_level == "INFO"
