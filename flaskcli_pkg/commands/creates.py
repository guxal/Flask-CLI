#!/usr/bin/python3

from controllers.create import * 
import typer
import shutil
import os


app = typer.Typer()


@app.command("app")
def cli_app(name: str = "app", shortname: str = "APP"):
    path = "./" + name
    params = {
            "<[app]>": shortname,
            "<[name-app]>": name
            }
    try:
        os.mkdir(path)
        os.mkdir(path + "/dev")
        dirname = os.path.dirname(__file__)
        dirname = dirname.split('/')
        dirname.pop()
        dirname = "/".join(dirname)
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
    typer.echo(f"Create model: {name}")

@app.command("api_view")
def cli_api_view(name: str):
    typer.echo("Create api view")

@app.command("view")
def cli_view(name: str):
    typer.echo("Create view")

if __name__ == "__main__":
    app()
