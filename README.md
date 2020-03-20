# Flask CLI
------------

[![Build Status](https://api.travis-ci.org/guxal/Flask-CLI.svg?branch=master)](https://travis-ci.org/guxal/Flask-CLI)

FlaskCLI is a CLI for creates, manages, builds and test your Flask projects.

  - Development tools
  - Libraries specialized for Flask
  - Magic
 
### What is CLI
---------------

A command-line interface (CLI) processes commands to a computer program in the form or lines of text.

### What is Flask
-----------------
Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions. However, Flask supports extensions that can add application features as if they were implemented in Flask itself. Extensions exist for object-relational mappers, form validation, upload handling, various open authentication technologies and several common framework related tools.

### The FlaskCLi Goal
--------------------
Building a Flask application gives a greater flexibility than many alternatives. As being a micro-framework, all the additional components are chosen and added separately.

The objective of FlaskCLI is to add components quickly and easily to the applications created under this stack.


# New Features
-------------
  - Create app project
  - Create model
  - Create api_view
  - Create view
  - Build enviroment
  - Launch Flask servers
  - Tests

# Installing
------------
Recoment that use a Vagrant Box ubuntu/xenial64
You should have ````Python3.6```` or higher
Install and update using pip:

```
pip install flaskcli
```

or clone this repo and enter into the folder and use this command

    source dev/alias.sh

# Quick Start
-------------

First use this command for creating the initial structure

    flaskcli create app 
or

    flaskcli create app --name <your-name-app> --shortname <your-short-name>
    
    - default:  --name "app"
                --shortname "APP"

* This creates the following structure

```
.
├── api
│   └── __init__.py
│   └── v1
│       └── __init__.py
│       └── app.py
│       └── views
│           └── __init__.py
│           └── index.py
├── console.py
├── dbconsole.sh
├── dev
│   └── export_enviroment.sh
│   └── requirements.txt
│   └── setup_mysql_dev.sql
│   └── setup_mysql_test.sql
├── models
│   └── __init__.py
│   └── base_model.py
│   └── engine 
│       └──  __init__.py
│       └──  db_storage.py
│       └──  file_storage.py
├── web
│   └── __init__.py
│   └── app.py
│   └── static
│   │   └── images
│   │   └── scripts
│   │       └── 0-script.js
│   │   └── styles
│   │       └── 0-style.css
│   └── templates
│       └── 0-index.html
└── build.sh
```

The next thing is to install the requirements and configure the local environment, all this is done by the following command.

```
chmod u+x build.sh && ./build.sh
```
This command assigns permissions to ```build.sh``` and execute file.


This command executes some files that are contained within the dev folder.
Here we will explain each of them

### Files that build.sh runs

| Name | Description |
|------------------------|-----------------|
|setup_local_server.sh| config local enviroment for development |
|requirements.txt| install packages that need this repo |
|setup_mysql_dev.sql| create database and user for development |
|setup_mysql_test.sql| create database and user for testing |


In this way we prepare an environment with a mysql database and install the necessary requirements for the application to run correctly.

In the dev folder there are different files that will help you configure your environment

```
├── dev
│   ├── export_enviroment.sh
│   ├── export_fc_var.sh
│   ├── requirements.txt
│   ├── setup_local_server.sh
│   ├── setup_mysql_dev.sql
│   └── setup_mysql_test.sql
```

for create model your need export this file 

    source dev/export_fc_var.sh
    
this command export this variable 

    FC_VAR_ENV="<your_app_var>"
    

run your app
```
./dbconsole.sh # to run with the connection to db
```

```
./console.py #  to run with the connection to file storage
```

Enjoy.

## Manage your launches.

when launching this will launch flask and raise the servers for your application
It will create 4 files 2 in the root directory and another 2 in dev

Execute this for launch

    ./launch

### ./
|Name| Description |
|------|--------|
|api.pid |  contains the api pid process number|
|web.pid | contains the web pid process number|

### ./dev/
| Name | Description |
|----|----|
| api.log |contains the api logs|
| web.log | contains the web logs|

use the following command to anchor logs in real time

    tail -f dev/api.log
or
    
    tail -f dev/web.log
You can continue writing code, these will be kept updated while the global variable   
````<yourApp> _API_DEBUG ```` and ````<yourApp> _FRONT_DEBUG````
stay ````true````.
run a debugging and testing environment for development, can switch to production at any time.

# Configuration
---------------
Consider these global variables according to the name of your application
Note the default name if you don't use this option

```
STORAGE
<[app]>_MYSQL_USER=<[app-lower]>_dev
<[app]>_MYSQL_PWD=<[app-lower]>_dev_pwd
<[app]>_MYSQL_HOST=localhost
<[app]>_MYSQL_DB=<[app-lower]>_dev_db
<[app]>_TYPE_STORAGE=db
<[app]>_ENV=test

API LAUNCH
<[app]>_API_HOST=0.0.0.0
<[app]>_API_PORT=5000
<[app]>_API_DEBUG=True
<[app]>_API_THREAD=True

FRONT LAUNCH
<[app]>_FRONT_HOST=0.0.0.0
<[app]>_FRONT_PORT=5001
<[app]>_FRONT_DEBUG=True
<[app]>_FRONT_THREAD=True

CLI
FC_VAR_ENV="<your_app_var>" # MUST BE CREATED TO ADD MODELS
```

# Usage
--------

*   ``` flaskcli create app [--name, --shortname] ```
*       default: --name="app", --shortname="APP"
        example:
            - flaskcli create app
            - flaskcli create app --name inventory --shortname INV

*   ``` flaskcli create model <name>```
*       -   Your must export a environt with name FC_VAR_ENV="your_shortname"  
        -   <name> is required, must be in singular and lowercase
        example:
        -   flaskcli create model product
        
*   ```flaskcli create api_view <name>```
*       - <name> is required, must be in singular and lowercase
        example:
            -   flaskcli create api_view product

*   ```flaskcli create view <name> [--url]```
*       - <name> is required, must be in singular and lowercase
        - if you don't put url the name is put as url
        example:
            -   flaskcli create view product
            -   flaskcli create view product --url products



## console.py

This file containt a cli for manager your objects

### Commands

These are some of the commands implemented in our console (HBNBCommand):

| Command | Description |
| ------ | ------ |
| all | Prints all string representation of all instances based or not on the class name |
| create | Creates a new instance of class name, saves it (to the JSON file) and prints the id |
| destroy | Deletes an instance based on the class name and id (save the change into the JSON file) |
| help | List available commands with "help" or detailed help with "help cmd" |
| quit - EOF | Commands to exit the program |
| show | Prints the string representation of an instance based on the class name and id |
| update | Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file) |

To start, navigate to the project folder and enter `./console.py` in the shell.

| Examples of how to use the commands |
| ------ |
| Create: |
| `create <class name>` Ex: `create BaseModel` |
| Show: |
| `show <class name> <object id>` Ex: `show User my_id` |
| Destroy: |
| `destroy <class name> <object id>` Ex: `destroy Place my_place_id` |
| All: |
| `all` or `all <class name>` Ex: `all` or `all State` |
| Quit: |
| `quit` or `EOF (Ctrl-d)` |
| Help: |
| `help` or `help <command>` Ex: `help` or `help all` |
| Additionally, the console supports: |
| `<class name>.<command>(<parameters>)` syntax. Ex: `City.show(my_city_id)` |





### Plugins

| Plugin | README |
| ------ | ------ |
| Deploy Flask CLI | [github/drc288/dfc](https://github.com/drc288/dfc) |



# Authors
* Guxal | [Github](https://github.com/guxal) | [Twitter](https://twitter.com/bitcoincucuta)
* MonicaJaimes | [Github](https://github.com/monicajaimesc) / [Twitter](https://twitter.com/Lama6a)


# License

MIT
**Free Software, Hell Yeah!**


