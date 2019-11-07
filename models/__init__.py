#!/usr/bin/python3
"""Module for Base class."""
from json import dumps, loads
import csv
import uuid
from datetime import datetime


class BaseModel:
    """A representation of the base of our OOP hierarchy."""

    def __init__(self, id=None, created_at=None, updated_at=None):
        """Constructor."""
        if id is None:
            self.id = str(uuid.uuid4())
        else:
            self.id = str(id)

        if created_at is None:
            self.created_at = datetime.now()

        if updated_at is None:
            self.updated_at = datetime.now()
        else:
            self.updated_at = datetime.now()

    def __str__(self):
        """method str."""
        return "[{}] ({}) {}".format(BaseModel.__name__, self.id, self.__dict__)

    def save(self):
        """ method save: Updates the time of the property Update_at"""
        self.updated_at = datetime.now()

    def to_dict(self):
        ret_dict = self.__dict__
        ret_dict["__class__"] = BaseModel.__name__
        ret_dict["created_at"] = str(datetime.isoformat(self.created_at))
        ret_dict["updated_at"] = str(datetime.isoformat(self.updated_at))
        return ret_dict

def main():
    my_model = BaseModel()
    my_model.name = "Holberton"
    my_model.my_number = 89
    print(my_model)

    my_model.save()
    print(my_model)

    my_model_json = my_model.to_dict()
    print(my_model_json)

    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

main()
