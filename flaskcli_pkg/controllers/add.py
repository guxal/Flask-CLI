from controllers.make_file import search_and_add

def add_strings_model(params):
    """
    """
    search_string = "from models.base_model import BaseModel\n"
    new_string = "from models." + params.get('_nclass') + " import "\
                 + params.get('<[name-model-capitalize]>') + "\n"
    search_and_add('./models/__init__.py', search_string, new_string)
    
    search_string = "from models import base_model\n"
    new_string = "from models import " + params.get('_nclass') + "\n"
    search_and_add('./models/engine/db_storage.py', search_string, new_string)
    search_and_add('./models/engine/file_storage.py', search_string, new_string)

    search_string = "    CNC = {\n"
    new_string = "        '" + params.get('<[name-model-capitalize]>') + "': " + params.get('_nclass') + "." + params.get('<[name-model-capitalize]>') + ",\n"

    search_and_add('./models/engine/db_storage.py', search_string, new_string)

    search_string = "        'BaseModel': base_model.BaseModel,\n"
    new_string = "        '" + params.get('<[name-model-capitalize]>') + "': " + params.get('_nclass') + "." + params.get('<[name-model-capitalize]>') + ",\n"
    
    search_and_add('./models/engine/file_storage.py', search_string, new_string)

def add_strings_api(params):
    """
    """
    search_string = "from api.v1.views.index import *  # noqa\n"
    new_string = "from api.v1.views." + params.get('<[name-api-pluralize]>') + " import *  # noqa\n"
    search_and_add('./api/v1/views/__init__.py', search_string, new_string)
