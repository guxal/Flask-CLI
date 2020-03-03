#!/usr/bin/python3

import typer
import shutil
import os


app = typer.Typer()



def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file
    and Returns the number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)


def create_orm(path, dirname):
    try:
        os.makedirs(path + '/models/engine')
        shutil.copy(dirname + '/templates/orm/__init__.py', path + "/models/")
        shutil.copy(dirname + '/templates/orm/base_model.py', path + "/models/")
        shutil.copy(dirname + '/templates/orm/file_storage.py', path + "/models/engine/")
        shutil.copy(dirname + '/templates/orm/db_storage.py', path + "/models/engine/")
        append_write(path + "/models/engine/__init__.py", "")
    except OSError:
        print ("Creation of the directory %s failed" % "models/ models/engine")
    else:
        print ("Successfully created the directory %s" % "models/ models/engine")    


def create_api():
    pass

def create_view():
    pass

def create_test():
    pass

def create_console(path, dirname):
    shutil.copy(dirname + '/templates/cli/console.py', path)

@app.command("app")
def cli_app(name: str = "app"):
    path = "./" + name
    try:
        os.mkdir(path)
        #print('getcwd:      ', os.getcwd())
        #print('__file__:    ', __file__)
        #print('basename:    ', os.path.basename(__file__))
        #print('dirname:     ', os.path.dirname(__file__))
        dirname = os.path.dirname(__file__)
        create_orm(path, dirname)
        create_console(path, dirname)

    except OSError:
        print ("Creation of the proyect %s failed" % path)
    else:
        typer.echo(f"Creating proyect: {name}")

@app.command("model")
def cli_model(name: str):
    typer.echo(f"Deleting user: {user_name}")

@app.command("api_view")
def cli_api_view(name: str):
    typer.echo("api view")

@app.command("view")
def cli_view(name: str):
    typer.echo("view")

if __name__ == "__main__":
    app()
