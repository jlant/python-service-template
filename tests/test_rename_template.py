from rename_template import replace_file_content

OLD = ("python_service_template", "pst", "python-service-template")
NEW = ("my_service", "mst", "my-service", "My Service")


def test_replaces_dist_name() -> None:
    text = 'name = "python-service-template"'
    result = replace_file_content(text, *OLD, *NEW)
    assert result == 'name = "my-service"'


def test_replaces_console_script_before_import_path() -> None:
    text = 'pst = "python_service_template.cli:app"'
    result = replace_file_content(text, *OLD, *NEW)
    assert result == 'mst = "my_service.cli:app"'


def test_replaces_cli_in_readme_code_block() -> None:
    text = "uv run pst run\n"
    result = replace_file_content(text, *OLD, *NEW)
    assert result == "uv run mst run\n"


def test_replaces_env_var_prefix() -> None:
    text = "PST_LOG_LEVEL=DEBUG PST_RUN_SECONDS=0 uv run pst run\n"
    result = replace_file_content(text, *OLD, *NEW)
    assert "PST_" not in result
    assert "MST_" in result
