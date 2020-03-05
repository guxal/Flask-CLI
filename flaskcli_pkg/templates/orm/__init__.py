import os
from models.base_model import BaseModel

"""CNC - dictionary = { Class Name (string) : Class Type }"""

if os.environ.get('<[app]>_TYPE_STORAGE') == 'db':
    from models.engine import db_storage
    CNC = db_storage.DBStorage.CNC
    storage = db_storage.DBStorage()
else:
    from models.engine import file_storage
    CNC = file_storage.FileStorage.CNC
    storage = file_storage.FileStorage()

storage.reload()
