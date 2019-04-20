import click

@click.group()
def cliente():
    """ciclo vital manejo de clientes"""
    pass

@cliente.comando()
@click.pass_context
def crear(ctx,nombre,compañia,email,position):
    """ crear nuevo cliente """
    pass

@cliente.comando()
@click.pass_context
def lista():
    """lista todos los clientes"""
    pass

@cliente.comando()
@click.pass_context
def editar(ctx,id_cliente):
    """editar cliente"""
    pass

@cliente.comando()
@click.pass_context
def quitar(ctx, id_cliente):
    """quita cliente """
    pass

all = cliente