from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version
from pathlib import Path
from typing import Annotated

import typer
from rich import print

from .settings import Settings, load_settings

DIST_NAME = "python-service-template"
CLI_NAME = "pst"

app = typer.Typer(
    no_args_is_help=True,
    add_completion=False,
    rich_markup_mode="rich",  # Allows for help text to use [bold], [green], etc.
    epilog="Made with :heart:  by [blue]Jeremiah Lant[/blue]",  # Footer text
)


def version_callback(value: bool):
    if value:
        try:
            v = version(DIST_NAME)
        except PackageNotFoundError:
            v = "0.0.0"
        print(f"{CLI_NAME} {v}")
        raise typer.Exit()


@app.callback()
def main(
    ctx: typer.Context,
    version: bool | None = typer.Option(
        None,
        "--version",
        "-v",
        callback=version_callback,
        is_eager=True,
        help="Show app version and exit.",
    ),
):
    """
    [green] Python Service Template (PST) CLI Tool[/green] :rocket:

    A minimal, production-grade Python Service Template (PST) with a CLI interface.
    """
    # Customize behavior if no command is provided
    if ctx.invoked_subcommand is None:
        # This only runs if no subcommand was typed
        pass


@app.command()
def hello(
    name: str = typer.Option("world", "--name", "-n"),
) -> None:
    """Example command that reads a TOML config file and prints a greeting."""
    print(f"[bold green]Hello, {name}![/bold green]")


@app.command()
def read_config(
    config: Annotated[Path, typer.Option("--config", "-c", exists=False)] = Path("config/app.toml"),
) -> None:
    """Example command that reads a TOML config file and prints its contents."""
    settings: Settings = load_settings(config)
    print(f"app_name={settings.app_name!r}")
    print(f"log_level={settings.log_level!r}")
