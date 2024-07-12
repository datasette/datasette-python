import click
import datasette
import sys
import subprocess


@datasette.hookimpl
def register_commands(cli):
    @cli.command(
        context_settings=dict(
            ignore_unknown_options=True,
        )
    )
    @click.argument("args", nargs=-1, type=click.UNPROCESSED)
    def python(args):
        """
        Run Python interpreter, passing through any arguments
        """
        cmd = [sys.executable]
        cmd.extend(args)
        subprocess.run(cmd)
