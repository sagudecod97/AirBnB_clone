#!/usr/bin/python3
"""
Unittest for FileStorage class
"""

import unittest
import pep8
import contextlib
from io import StringIO
import io
import copy
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models import storage
import os
from os import remove
import contextlib
from io import StringIO
import inspect

import uuid
from datetime import datetime
import sys


class FileStorage(unittest.TestCase):

    def setUp(self):
        model = BaseModel()
        model.name = "Holberton"
        model.my_number = 89
        model.save()

    def resetStorage(self):
        try:
            os.remove('file.json')
        except:
            pass

    def test_instantiation(self):
        """Tests instantiation of FileStorage class."""
        inst = FileStorage()
        self.assertTrue(isinstance(inst, FileStorage))
        self.assertEqual(type(storage).__name__, "FileStorage")

    def test_init_no_args(self):
        """Tests __init__ with no arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            FileStorage.__init__()
        msg = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_init_many_args(self):
        """Tests __init__ with many arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            b = FileStorage(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        msg = "__init__() takes from 1 to 2 positional " \
              "arguments but 11 were given"
        self.assertEqual(str(e.exception), msg)

    def test_types(self):
        """Test types of variable storage"""
        try:
            self.assertIs(type(storage.__file_path), str)
            self.assertIs(type(storage.__objects), dict)
            self.assertEqual(storage.__file_path, 'file.json')
        except:
            pass

    def test_storage_all(self):
        """tests all method for classname."""
        all_objs = storage.all()
        self.assertIs(type(all_objs), dict)
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
            temp_stdout = StringIO()
            with contextlib.redirect_stdout(temp_stdout):
                print(obj)
            output = temp_stdout.getvalue().strip()
            self.assertIn("'id':", output)
            self.assertIn("'created_at':", output)
            self.assertIn("'updated_at':", output)

    def test_new(self):
        """tests new() method for classname."""
        obj = User()
        obj.first_name = "My name"
        obj_id = str("User." + obj.id)
        all_objs = storage.all()
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(all_objs[obj_id])
        output = temp_stdout.getvalue().strip()
        self.assertIn("[User]", output)
        self.assertIn("'first_name': 'My name'", output)

    def test_save(self):
        """test save method for classname"""
        self.resetStorage()
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.age = 89
        my_model.save()
        self.assertTrue(os.access('file.json', os.R_OK))
        allobjects = storage.all()
        for obj_id in allobjects.keys():
            if my_model.id in obj_id:
                obj = allobjects[obj_id]
                self.assertEqual(my_model.id, obj.id)
                self.assertEqual(my_model.name, obj.name)
                self.assertEqual(my_model.age, obj.age)
                self.assertEqual(my_model.created_at, obj.created_at)
                self.assertEqual(my_model.updated_at, obj.updated_at)

    def test_reload(self):
        """test reload() method for classname."""
        storage.__objects = {}
        self.assertEqual(len(storage.all()), 0)
        my_model = BaseModel()
        my_model.save()
        storage.__objects = {}
        storage.reload()
        self.assertNotEqual(len(storage.all()), 0)


if __name__ == '__main__':
    unittest.main()
