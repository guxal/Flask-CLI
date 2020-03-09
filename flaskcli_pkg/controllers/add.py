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
