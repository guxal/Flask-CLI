from controllers.make_file import render_template, make_file
import os
import shutil


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file
    and Returns the number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)

def create_orm(path, dirname, params):
    """
    """
    try:
        os.makedirs(path + '/models/engine')
        
        new_file = render_template(dirname + '/templates/orm/__init__.py', params)
        make_file(path + "/models/__init__.py", new_file)

        new_file = render_template(dirname + '/templates/orm/base_model.py', params)
        make_file(path + "/models/base_model.py", new_file)
        
        new_file = render_template(dirname + '/templates/orm/file_storage.py', params)
        make_file(path + "/models/engine/file_storage.py", new_file)

        new_file = render_template(dirname + '/templates/orm/db_storage.py', params)
        make_file(path + "/models/engine/db_storage.py", new_file)
        
        append_write(path + "/models/engine/__init__.py")
    except OSError:
        print ("Creation of the directory %s failed" % "models/ models/engine")
    else:
        print ("Successfully created the directory %s" % "models/ models/engine")    

def create_api(path, dirname, params):
    """
    """
    try:
        os.makedirs(path + '/api/v1/views')

        append_write(path + "/api/__init__.py")
        append_write(path + "/api/v1/__init__.py")

        new_file = render_template(dirname + '/templates/restfull/app.py', params)
        make_file(path + '/api/v1/app.py', new_file)
        
        new_file = render_template(dirname + '/templates/restfull/index.py', params)
        make_file(path + '/api/v1/views/index.py', new_file)

        new_file = render_template(dirname + '/templates/restfull/__init__.py', params)
        make_file(path + '/api/v1/views/__init__.py', new_file)
    except OSError:
        print ("Creation of the directory %s failed" % "api/ api/v1 api/v1/views")
    else:
        print ("Successfully created the directory %s" % "api/ api/v1 api/v1/views")


def create_view(path, dirname, params):
    """
    """
    try:
        os.makedirs(path + '/web/static/styles')
        os.makedirs(path + '/web/static/scripts')
        os.makedirs(path + '/web/static/images')
        os.makedirs(path + '/web/templates')

        new_file = render_template(dirname + '/templates/front/app.py', params)
        make_file(path + '/web/app.py', new_file)

        new_file = render_template(dirname + '/templates/front/index.html', params)
        make_file(path + '/web/templates/0-index.html', new_file)
        
        append_write(path + '/web/__init__.py')
        append_write(path + '/web/static/styles/0-style.css')
        append_write(path + '/web/static/scripts/0-script.js')


    except OSError:
        print ("Creation of the directory %s failed" % "web/ web/static,styles,scripts web/templates")
    else:
        print ("Successfully created the directory %s" % "web/ web/static,styles,scripts web/templates")

def create_test():
    """
    """
    pass

def create_console(path, dirname, params):
    """
    """
    new_file = render_template(dirname + '/templates/cli/console.py', params)
    make_file(path + '/console.py', new_file)

def create_export(path, dirname, params):
    """
    """
    new_file = render_template(dirname + '/templates/dev/export_enviroment.sh', params)
    make_file(path + '/dev/export_enviroment.sh', new_file)

def create_dbconsole(path, dirname, params):
    """
    """
    new_file = render_template(dirname + '/templates/cli/dbconsole.sh', params)
    make_file(path + '/dbconsole.sh', new_file)

def create_setup_mysql(path, dirname, params):
    """
    """
    new_file = render_template(dirname + '/templates/dev/setup_mysql_dev.sql', params)
    make_file(path + '/dev/setup_mysql_dev.sql', new_file)

    new_file = render_template(dirname + '/templates/dev/setup_mysql_test.sql', params)
    make_file(path + '/dev/setup_mysql_test.sql', new_file)

def create_requirements(path, dirname):
    """
    """
    shutil.copy(dirname + '/templates/dev/requirements.txt', path + '/dev/requirements.txt')

def create_model(path, dirname, params):
    """
    """
    new_file = render_template(dirname + '/templates/orm/model.py', params)
    make_file(path + '/models/' + params.get('_nclass') + '.py', new_file)
