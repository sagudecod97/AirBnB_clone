#!/usr/bin/python3
"""Module for Base class."""
from json import dumps, loads
import csv
import uuid
from datetime import datetime


class BaseModel:
    """A representation of the base of our OOP hierarchy."""

    def __init__(self, *args, **kwargs):
        """Constructor."""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        args_len = len(args)

        if args_len == 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue

                if key in ["created_at", "updated_at"]:
                    setattr(self, key, datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)

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
    print(my_model.id)
    print(my_model)
    print(type(my_model.created_at))
    print("--")
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

    print("--")
    my_new_model = BaseModel(**my_model_json)
    print(my_new_model.id)
    print(my_new_model)
    print(type(my_new_model.created_at))

    print("--")
    print(my_model is my_new_model)


main()
