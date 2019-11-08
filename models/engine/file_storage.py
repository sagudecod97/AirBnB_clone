#!/usr/bin/python3
"""Module for Base class."""
from json import dumps, loads
import csv
import uuid
from datetime import datetime


class FileStorage:
    """A representation of the base of our OOP hierarchy."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Method All."""
        return self.__objects

    def new(self, obj):
        """Method New."""
        new_obj = obj.__dict__
        new_obj["created_at"] = datetime.isoformat(new_obj["created_at"])
        new_obj["updated_at"] = datetime.isoformat(new_obj["updated_at"])
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = new_obj

    def save(self):
        """Method Save."""
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            new_obj = self.__objects
            f.write(dumps(new_obj))

    def reload(self):
        """Method Reload."""
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                objects = loads(f.read())
                self.__objects = objects
        except Exception:
            pass
