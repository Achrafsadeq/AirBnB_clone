#!/usr/bin/python3
"""
Defines the Amenity class, which inherits from BaseModel.
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Represents an amenity, a subclass of BaseModel.

    Public class attribute:
        name: (str) name of the amenity
    """
    name = ""
