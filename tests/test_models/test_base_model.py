#!/usr/bin/python3
"""Unittest module for the BaseModel Class."""

from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
import json
import os
import re
import time
import unittest
import uuid
import pep8
import contextlib
from io import StringIO
import io
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_instantiation(self):
        """Tests instantiation of BaseModel class."""

        inst = BaseModel()
        self.assertEqual(str(type(inst)),
                         "<class 'models.base_model.BaseModel'>")
        self.assertIsInstance(inst, BaseModel)
        self.assertTrue(issubclass(type(inst), BaseModel))

    def test_init_no_args(self):
        """Tests __init__ with no arguments."""
        with self.assertRaises(TypeError) as e:
            BaseModel.__init__()
        msj = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msj)

    def test_init_many_args(self):
        """Tests __init__ with many arguments."""
        args = [i for i in range(100)]
        inst_m = BaseModel(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        inst_m = BaseModel(*args)

    def test_attributes(self):
        attr = BaseModel()
        self.assertTrue(hasattr(attr, 'id'))
        self.assertTrue(hasattr(attr, 'created_at'))
        self.assertTrue(hasattr(attr, 'updated_at'))
        self.assertEqual(type(getattr(attr, 'updated_at', None)), datetime)
        self.assertEqual(type(getattr(attr, 'created_at', None)), datetime)
        self.assertEqual(type(getattr(attr, 'id', None)), str)

    def test_types(self):
        typ = BaseModel()
        self.assertIs(type(typ.id), str)
        self.assertIs(type(typ.created_at), datetime)
        self.assertIs(type(typ.updated_at), datetime)

    def test_id_diff(self):
        id1 = BaseModel()
        id2 = BaseModel()
        self.assertNotEqual(id1.id, id2.id)

    def test_instantiation_1(self):
        o_model = BaseModel()
        self.assertTrue(hasattr(o_model, "created_at"))
        self.assertTrue(hasattr(o_model, "updated_at"))

    def test_str(self):
        """__str__: should print: [<class name>] (<self.id>) <self.__dict__>"""
        str_model = BaseModel()
        str_model.name = "Holberton"
        str_model.age = 89
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(str_model)
        output = temp_stdout.getvalue().strip()
        self.assertIn("[BaseModel]", output)
        self.assertIn("'age': 89", output)
        self.assertIn("'name': 'Holberton'", output)
        self.assertIn("'created_at': datetime.datetime", output)
        self.assertIn("'updated_at': datetime.datetime", output)

    def test_save(self):
        """Test save(): updates the public instance attribute updated_at"""
        save_model = BaseModel()
        var = save_model.updated_at
        save_model.save()
        self.assertNotEqual(var, save_model.updated_at)

    def test_save_no_args(self):
        """Tests save(): with no arguments."""
        with self.assertRaises(TypeError) as e:
            BaseModel.save()
        msj = "save() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msj)

    def test_save_excess_args(self):
        """Tests save(): with too many arguments."""
        with self.assertRaises(TypeError) as e:
            BaseModel.save(self, 98)
        msj = "save() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), msj)

    def test_from_dict(self):
        """__init__(self, *args, **kwargs)"""
        from_dict = BaseModel()
        from_dict.name = "Pedro"
        from_dict.age = 95
        from_dict_json = from_dict.to_dict()
        from_dict_new = BaseModel(**from_dict_json)
        self.assertEqual(from_dict_new.to_dict(), from_dict.to_dict())

    def test_to_dict(self):
        """Test the public instance method to_dict"""
        to_dict = BaseModel()
        to_dict.name = "Santiago"
        to_dict.age = 8
        to_dict_json = to_dict.to_dict()
        self.assertEqual(to_dict_json["name"], to_dict.name)
        self.assertEqual(to_dict_json["id"], to_dict.id)
        self.assertEqual(to_dict_json["age"], to_dict.age)
        self.assertEqual(to_dict_json["__class__"], type(to_dict).__name__)
        self.assertEqual(to_dict_json["created_at"],
                         to_dict.created_at.isoformat())
        self.assertEqual(to_dict_json["created_at"],
                         to_dict.created_at.isoformat())
        self.assertEqual(to_dict_json["updated_at"],
                         to_dict.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
