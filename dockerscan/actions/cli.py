import click
import logging

from dockerscan import global_options

from .image.cli import image

log = logging.getLogger('dockerscan')


@global_options()
@click.pass_context
def cli(ctx, **kwargs):
    ctx.obj = kwargs

cli.add_command(image)

if __name__ == "__main__" and __package__ is None:  # pragma no cover
    cli()
