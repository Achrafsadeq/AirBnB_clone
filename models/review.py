#!/usr/bin/python3
"""
Defines the Review class, which is a subclass of BaseModel.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Represents a review, subclass of BaseModel.

    Public class attributes:
        place_id: (str) will store the Place.id
        user_id: (str) will store the User.id
        text: (str) contains the review text
    """
    place_id = ""
    user_id = ""
    text = ""
