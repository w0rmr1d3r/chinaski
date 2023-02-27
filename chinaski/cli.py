import click

from chinaski.chinaski import chinaski


@click.command()
@click.option(
    "--file",
    "file",
    type=str,
    default=None,
    help="Path to single file to scan",
    show_default=True,
)
def cli(
    file: str,
) -> None:
    chinaski(file=file)
