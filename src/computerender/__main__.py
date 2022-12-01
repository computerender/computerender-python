"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Computerender."""


if __name__ == "__main__":
    main(prog_name="computerender")  # pragma: no cover
