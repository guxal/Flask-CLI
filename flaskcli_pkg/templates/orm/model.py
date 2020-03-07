#!/usr/bin/python3
"""
<[name-model-capitalize]> Class from Models Module
"""
import os
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float
STORAGE_TYPE = os.environ.get('<[app]>_TYPE_STORAGE')


class <[name-model-capitalize]>(BaseModel, Base):
    """
    <[name-model-capitalize]> class handles all applications <[name-model-pluralize]>
    """
    if STORAGE_TYPE == "db":
        __tablename__ = '<[name-model-pluralize]>'
        """
        Your Code db storage Here
        Example:
            email = Column(String(128), nullable=False)
        """
    else:
        """
        Your Code file storage Here
        Example:
            email = ''
        """
        pass
