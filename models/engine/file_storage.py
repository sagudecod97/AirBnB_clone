#!/usr/bin/python3
"""Module for Base class."""
import copy
from json import dumps, loads
import csv
import uuid
from datetime import datetime
from models.base_model import BaseModel

class FileStorage:
    """A representation of the base of our OOP hierarchy."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Method All."""
        return self.__objects

    def new(self, obj):
        """Method New."""
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """Method Save."""
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            new_obj = copy.deepcopy(self.__objects)
            dict_write = {}

            for key, value in new_obj.items():
                dict_write[key] = value.to_dict()
            f.write(dumps(dict_write))

    def reload(self):
        """Method Reload."""
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                objects = loads(f.read())
                self.__objects = objects
                new_dict = {}
                count = 0

                for key, value in objects.items():
                    new_dict[key] = value
                    count += 1
                for key, value in new_dict.items():
                    new_dict[key] = BaseModel(**value)
                self.__objects = new_dict
        except Exception:
            pass
