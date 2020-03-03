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


def create_api(path, dirname):
    try:
        os.makedirs(path + '/api/v1/views')
        append_write(path + "/api/__init__.py", "")
        append_write(path + "/api/v1/__init__.py", "")
        shutil.copy(dirname + '/templates/restfull/app.py', path + "/api/v1/")
        shutil.copy(dirname + '/templates/restfull/index.py', path + "/api/v1/views/")
        shutil.copy(dirname + '/templates/restfull/__init__.py', path + "/api/v1/views/")
    except OSError:
        print ("Creation of the directory %s failed" % "api/ api/v1 api/v1/views")
    else:
        print ("Successfully created the directory %s" % "api/ api/v1 api/v1/views")    

def create_view(path, dirname):
    try:
        os.makedirs(path + '/web/static/styles')
        os.makedirs(path + '/web/static/scripts')
        os.makedirs(path + '/web/static/images')
        os.makedirs(path + '/web/templates')

        shutil.copy(dirname + '/templates/front/app.py', path + '/web/')
        shutil.copy(dirname + '/templates/front/index.html', path + '/web/templates/0-index.html')
        
        append_write(path + '/web/__init__.py')
        append_write(path + '/web/static/styles/0-style.css')
        append_write(path + '/web/static/scripts/0-script.js')


    except OSError:
        print ("Creation of the directory %s failed" % "web/ web/static,styles,scripts web/templates")
    else:
        print ("Successfully created the directory %s" % "web/ web/static,styles,scripts web/templates")

def create_test():
    pass

def create_console(path, dirname):
    shutil.copy(dirname + '/templates/cli/console.py', path)

@app.command("app")
def cli_app(name: str = "app"):
    path = "./" + name
    try:
        os.mkdir(path)
        dirname = os.path.dirname(__file__)
        create_orm(path, dirname)
        create_console(path, dirname)
        create_api(path, dirname)
        create_view(path, dirname)

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
