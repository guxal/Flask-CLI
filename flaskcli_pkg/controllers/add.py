from controllers.make_file import search_and_add

def add_strings_model(params):
    """
    """
    search_string = "from models.base_model import BaseModel\n"
    new_string = "from models." + params.get('_nclass') + " import "\
                 + params.get('<[name-model-capitalize]>') + "\n"
    search_and_add('./models/__init__.py', search_string, new_string)

