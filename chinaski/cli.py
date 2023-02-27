import click

from chinaski.henry import core


@click.command()
@click.option(
    "--file",
    "file",
    type=str,
    default=None,
    help="REQUIRED - Path to single file to scan.",
    show_default=True,
)
def cli(
    file: str,
) -> None:
    # todo - if file or path are none or empty, raise exception and test to it
    for result in core(file_path=file):
        print(result)
