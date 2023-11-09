import click


@click.command()
@click.option("--count", default=1, help="Number of greetings.")
@click.option("--path", prompt="Shapefile path", help="The Shapefile path (dir).")
def cli(count, path: str):
    """Simple program that reads and logs shapefile data."""
    click.echo(path)
