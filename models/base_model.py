#!/usr/bin/python3
"""Module for Base class."""
import models
import json
import uuid
from datetime import datetime
import sys


class BaseModel:
    """A representation of the base of our OOP hierarchy."""

    def __init__(self, *args, **kwargs):
        """Constructor."""
        if kwargs is not None and kwargs != {}:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    setattr(self, key,
                            datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif key == "__class__":
                    continue
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """method str."""
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                     self.__dict__)

    def save(self):
        """ method save: Updates the time of the property Update_at"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        ret_dict = self.__dict__.copy()
        ret_dict["__class__"] = type(self).__name__
        ret_dict["created_at"] = ret_dict['created_at'].isoformat()
        ret_dict["updated_at"] = ret_dict["updated_at"].isoformat()
        return ret_dict
