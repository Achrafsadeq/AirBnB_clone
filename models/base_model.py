#!/usr/bin/python3
"""Base model class for the AirBnB clone project"""
import uuid
from datetime import datetime


class BaseModel:
    """Base class for all models in the AirBnB clone"""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel

        Args:
            *args: Unused
            **kwargs: Dictionary of attributes
        """
        from models import storage
        time_format = "%Y-%m-%dT%H:%M:%S.%f"

        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        setattr(self, key,
                                datetime.strptime(value, time_format))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Return string representation of BaseModel instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update updated_at with current time and save to storage"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Convert instance to dictionary format"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
