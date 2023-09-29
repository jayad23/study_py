import click
from tabulate import tabulate
from clients.services import Clients_Service
from clients.models import Client

@click.group()
def clients():
  '''Manages the clients lifecycle'''
  pass;


@clients.command()
@click.option('-n', '--name',
              type=str,
              prompt=True,
              help='The Client name')
@click.option('-c', '--company',
              type=str,
              prompt=True,
              help='The Client company')
@click.option('-e', '--email',
              type=str,
              prompt=True,
              help='The Client email')
@click.option('-p', '--position',
              type=str,
              prompt=True,
              help='The Client position')              
@click.pass_context
def create(ctx, name, company, email, position):
  '''Creates a new client'''
  client = Client(name, company, email, position)
  service = Clients_Service(ctx.obj['clients_table'])

  service.create_client(client)
  pass;


@clients.command()
@click.pass_context
def enlist(ctx):
  """List all clients"""
  service = Clients_Service(ctx.obj['clients_table'])
  clients_list = service.list_clients()

  headers = [field.capitalize() for field in Client.schema()]
  table = []

  for client in clients_list:
    table.append(
      [
        client['uid'],
        client['name'],
        client['company'],
        client['email'],
        client['position'],
      ]
    )

  print(tabulate(table, headers))


@clients.command()
@click.argument("client_uid", type=str)
@click.pass_context
def update(ctx, client_uid):
  '''Updates a client'''
  service = Clients_Service(ctx.obj['clients_table'])
  clients = service.list_clients()

  client = [client for client in clients if client['uid'] == client_uid]

  if client:
    client = __update_client_flow(Client(**client[0]))
    service.update_client(client)
    click.echo("Client updated successfully")
    
  else:
    click.echo("Client not found")


def __update_client_flow(client):
  click.echo("Leave empty if you do not want to modify the value")

  client.name = click.prompt("New name", type=str, default=client.name)
  client.company = click.prompt("New company", type=str, default=client.company)
  client.email = click.prompt("New email", type=str, default=client.email)
  client.position = click.prompt("New position", type=str, default=client.position)

  return client;

@clients.command()
@click.pass_context
def delete(ctx, client_uid):
  '''Deletes a client'''
  pass


all = clients;
