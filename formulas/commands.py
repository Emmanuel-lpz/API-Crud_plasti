import click

from formulas.services import ServicioClient
from formulas.models import Formula


@click.group()
def formulas():
	"""Controla el ciclo de vida de las formulas"""
	pass


@formulas.command()
@click.option('-n', '--nombre',
			  type=str,
			  prompt=True,
			  help='El nombre de la formula')
@click.option('-m1', '--mat1',
			  type=str,
			  prompt=True,
			  help='El nombre del primer material')
@click.option('-m2', '--mat2',
			  type=str,
			  prompt=True,
			  help='El nombre del segundo material')
@click.option('-m3', '--mat3',
			  type=str,
			  prompt=True,
			  help='El nombre del tercer material')
@click.option('-m4', '--mat4',
			  type=str,
			  prompt=True,
			  help='El nombre del cuarto material')
@click.pass_context
def crear(ctx, nombre, mat1, mat2, mat3, mat4):
	"""Creauna nueva formula"""
	formula = Formula(nombre, mat1, mat2, mat3, mat4)
	formulas_services = ServicioClient(ctx.obj['table_name'])

	formulas_services.crear_formula(formula)


@formulas.command()
@click.pass_context
def lista(ctx):
	"""Lista de formulas"""
	formulas_services = ServicioClient(ctx.obj['formulas_table'])
	formulas = formulas_services.lista_formulas()

	click.echo(' ID   |  Nombre    |  Material 1    |  Material 2    |  Material 3    |  Material 4    ')
	click.echo('-*-' * 100)

	for formula in formulas:
		click.echo('{uid}  |  {mat1}  |  {mat2}   |  {mat3}  |  {mat4}'.format(
			uid=formula['uid'],
			nombre=formula['nombre'],
			mat1=formula['mat1'],
			mat2=formula['mat2'],
			mat3=formula['mat3'],
			mat4=formula['mat4']))


@formulas.command()
@click.pass_context
def actualizar(ctx, formula_uid):
    """Actualiza y modifica las formulas"""
    formulas_services = ServicioClient(ctx.obj['formulas_table'])

    formula = [formula for formula in formulas_services.lista_formulas() if formula['uid'] == formula_uid]
    
    if formula:
        formula = _update_formula_flow(Formula(**formula[0]))
        formulas_services.actualizar_formulas(formula)

        click.echo('Formula actualizada')
    else:
        click.echo('Formula no encontrada')

def _update_formula_flow(formula):
    click.echo('Deje en blanco si no quiere modificar el valor')

    client.nombre = click.prompt('Nueva formula (nombre)', type=str, default=formula.nombre)
    client.mat1 = click.prompt('Nuevo material 1', type=str, default=formula.mat1)
    client.mat2 = click.prompt('Nuevo material 2', type=str, default=formula.mat2)
    client.mat3 = click.prompt('Nuevo material 3', type=str, default=formula.mat3)
    client.mat4 = click.prompt('Nuevo material 4', type=str, default=formula.mat3)

    return client

@formulas.command()
@click.pass_context
def elimina(ctx, formula_uid):
	"""Elimina formulas que ya no necesitamos"""
	formulas_services = ServicioClient(ctx.obj['formulas_table'])

	if click.confirm('Esta seguro que quiere eliminar la formula con uid? '.format(formula_uid)):
		formulas_services.elimina_formula(formula_uid)


all = formulas
