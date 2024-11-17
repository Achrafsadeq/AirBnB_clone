#!/usr/bin/python3
"""
Defines the City class, inheriting from BaseModel.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    Represents a city, a subclass of BaseModel.

    Public class attributes:
        state_id: (str) will store the State.id
        name: (str) name of the city
    """
    state_id = ""
    name = ""
