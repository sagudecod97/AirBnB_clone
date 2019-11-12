#!/usr/bin/python3
"""Module for Base class."""
from json import dumps, loads
import csv
import uuid
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os


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
            new_obj = {key: value.to_dict() for key,
                       value in self.__objects.items()}
            f.write(dumps(new_obj))

    def reload(self):
        """Method Reload."""
        if not os.path.isfile(self.__file_path):
            return
        if os.path.isfile(self.__file_path) and \
                not os.stat(self.__file_path).st_size:
            return
        with open(self.__file_path, 'r', encoding="utf-8") as f:
            objects = loads(f.read())
            for key, value in objects.items():
                self.__objects[key] = eval(value['__class__'])(**value)
