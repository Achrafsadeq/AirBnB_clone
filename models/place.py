#!/usr/bin/python3
"""
Defines the Place class, which inherits from BaseModel.
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Represents a place, a subclass of BaseModel.

    Public class attributes:
        city_id: (str) will store the City.id
        user_id: (str) will store the User.id
        name: (str) name of the place
        description: (str) description of the place
        number_rooms: (int) number of rooms, default is 0
        number_bathrooms: (int) number of bathrooms, default is 0
        max_guest: (int) maximum number of guests, default is 0
        price_by_night: (int) price per night, default is 0
        latitude: (float) latitude of the place, default is 0.0
        longitude: (float) longitude of the place, default is 0.0
        amenity_ids: (list) list of Amenity.id
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
