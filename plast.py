import click

from formulas import commands as formulas_commands

FORMULAS_TABLA = '.formulas.csv'


@click.group()
@click.pass_context
def cli(ctx):
	ctx.obj = {}
	ctx.obj['formulas_table'] = FORMULAS_TABLA


cli.add_command(formulas_commands.all)