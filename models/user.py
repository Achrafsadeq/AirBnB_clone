#!/usr/bin/python3
"""
Defines the User class, which inherits from BaseModel.
"""

from models.base_model import BaseModel
import json


class User(BaseModel):
    '''Represents a user, which is a subclass of BaseModel.'''

    email = ""
    password = ""
    first_name = ""
    last_name = ""
