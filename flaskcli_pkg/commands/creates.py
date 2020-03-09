#!/usr/bin/python3
"""
"""
from controllers.create import *
from controllers.add import *
import inflect
import typer
import shutil
import os


app = typer.Typer()
p = inflect.engine()

"""
Select dirname ..
"""
dirname = os.path.dirname(__file__)
dirname = dirname.split('/')
dirname.pop()
dirname = "/".join(dirname)

@app.command("app")
def cli_app(name: str = "app", shortname: str = "APP"):
    """
    """
    path = "./" + name
    params = {
            "<[app]>": shortname,
            "<[name-app]>": name
            }
    try:
        os.mkdir(path)
        os.mkdir(path + "/dev")
        
        create_orm(path, dirname, params)
        create_console(path, dirname, params)
        create_api(path, dirname, params)
        params['<[count]>'] = '0'
        create_view(path, dirname, params)
        params['<[app-lower]>'] = shortname.lower()
        create_export(path, dirname, params)
        create_dbconsole(path, dirname, params)
        create_setup_mysql(path, dirname, params)
        create_requirements(path, dirname)
    except OSError:
        print ("Creation of the proyect %s failed" % path)
    else:
        typer.echo(f"Creating proyect: {name}")

@app.command("model")
def cli_model(name: str):
    """
    """
    if not os.environ.get('FC_VAR_ENV'):
        typer.echo("Please create FC_VAR_ENV with your shortname app.")
    else:
        params = {
            "<[app]>": os.environ.get('FC_VAR_ENV'),
            "<[name-model-capitalize]>": name.capitalize(),
            "<[name-model-pluralize]>": p.plural(name.lower()),
            "_nclass": name.lower()
        }
        create_model('.', dirname, params)
        add_strings_model(params)
        typer.echo(f"Create model: {params.get('_nclass')}")

@app.command("api_view")
def cli_api_view(name: str):
    """
    """
    params = {
        "<[name-api-capitalize]>": name.capitalize(),
        "<[name-api-pluralize]>": p.plural(name.lower()),
        "<[name-api-lower]>": name.lower(),
        "_nclass": p.plural(name.lower())
    }
    create_api_view('.', dirname, params)
    typer.echo(f"Create api_view: {params.get('_nclass')}")

@app.command("view")
def cli_view(name: str):
    """
    """
    typer.echo("Create view")

if __name__ == "__main__":
    app()
