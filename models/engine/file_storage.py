#!/usr/bin/python3
"""Module for Base class."""
from json import dumps, loads
import csv
import uuid
from datetime import datetime
import models.base_model
import os


class FileStorage:
    """A representation of the base of our OOP hierarchy."""
    __file_path = "file.json"
    __objects = {}
    __functions = {'BaseModel': models.base_model.BaseModel}

    def all(self):
        """Method All."""
        return self.__objects

    def new(self, obj):
        """Method New."""
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """Method Save."""
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            new_obj = {key: value.to_dict() for key, value in self.__objects.items()}
            f.write(dumps(new_obj))

    def reload(self):
        """Method Reload."""
        if not os.path.isfile(self.__file_path):
            return
        if os.path.isfile(self.__file_path) and not os.stat(self.__file_path).st_size:
            return
        with open(self.__file_path, 'r', encoding="utf-8") as f:
            objects = loads(f.read())
            obj_dict = {key: self.__functions[value["__class__"]](**value)
                        for key, value in objects.items()}
            self.__objects = obj_dict

