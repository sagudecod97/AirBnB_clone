#!/usr/bin/python3
"""Module for TestHBNBCommand class."""

from io import StringIO
import re
import os
from models.engine.file_storage import FileStorage
import unittest
from console import HBNBCommand
import datetime
from unittest.mock import patch


class TestHBNBCommand(unittest.TestCase):

    """Tests HBNBCommand console."""

    res_val = {
        str: "",
        int: 0,
        float: 0.0
    }

    attr_val = {
        str: "myst",
        int: 82,
        float: 1.23
    }

    test_rand_att = {
        "floatval": 9.8,
        "first_name": "myname",
        "intval": 123
    }

    def test_help(self):
        """Tests for help cmd."""
        with patch('sys.stdout', new=StringIO()) as file:
            HBNBCommand().onecmd("help")
        s = """
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

"""
        self.assertEqual(s, file.getvalue())

    def test_emptyline(self):
        """Tests emptyline."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
        out = ""
        self.assertEqual(out, f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("                  \n")
        out = ""
        self.assertEqual(out, f.getvalue())

    def test_do_EOF(self):
        """Tests EOF cmd."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
        out = f.getvalue()
        self.assertTrue(len(out) == 1)
        self.assertEqual("\n", out)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF fake")
        msj = f.getvalue().strip()
        self.assertFalse(len(msj) == 1)
        self.assertEqual("", msj)

    def test_do_quit(self):
        """Tests quit cmd."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
        out = f.getvalue()
        self.assertTrue(len(out) == 0)
        self.assertEqual("", out)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit fake")
        msj = f.getvalue()
        self.assertTrue(len(msj) == 0)
        self.assertEqual("", msj)

    def test_do_create(self):
        """Tests create for classes."""
        for classname in self.classes():
            self.exec_test_do_create(classname)

    def exec_test_do_create(self, classname):
        """Helper method to test the create cmd."""
        with patch('sys.stdout', new=StringIO()) as file:
            HBNBCommand().onecmd("create {}".format(classname))
        cid = file.getvalue()[:-1]
        self.assertTrue(len(cid) > 0)
        key = "{}.{}".format(classname, cid)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all {}".format(classname))
        self.assertTrue(cid in f.getvalue())

    def test_do_create_error(self):
        """Tests create cmd and errors."""
        with patch('sys.stdout', new=StringIO()) as file:
            HBNBCommand().onecmd("create")
        out = file.getvalue()[:-1]
        self.assertEqual(out, "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as file:
            HBNBCommand().onecmd("create garbage")
        msj = file.getvalue()[:-1]
        self.assertEqual(msj, "** class doesn't exist **")

    def test_do_show(self):
        """Tests show for classes."""
        for classname in self.classes():
            self.exec_test_do_show(classname)
            self.exec_test_show_advanced(classname)

    def exec_test_do_show(self, classname):
        """exec test the show cmd."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create {}".format(classname))
        cid = f.getvalue()[:-1]
        self.assertTrue(len(cid) > 0)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show {} {}".format(classname, cid))
        s = f.getvalue()[:-1]
        self.assertTrue(cid in s)

    def exec_do_show_error(self):
        """Exec show command with errors."""
        with patch('sys.stdout', new=StringIO()) as file:
            HBNBCommand().onecmd("show BaseModel")
        msj = file.getvalue()[:-1]
        self.assertEqual(msj, "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as file:
            HBNBCommand().onecmd("show fake")
        out = file.getvalue()[:-1]
        self.assertEqual(out, "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as file:
            HBNBCommand().onecmd("show")
        out = file.getvalue()[:-1]
        self.assertEqual(out, "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as file:
            HBNBCommand().onecmd("show BaseModel 123456")
        msg = file.getvalue()[:-1]
        self.assertEqual(msg, "** no instance found **")

    def exec_test_show_advanced(self, classname):
        """Exec test .show() cmd."""
        with patch('sys.stdout', new=StringIO()) as file:
            HBNBCommand().onecmd("create {}".format(classname))
        cuid = file.getvalue()[:-1]
        self.assertTrue(len(cuid) > 0)

        with patch('sys.stdout', new=StringIO()) as file:
            HBNBCommand().onecmd('{}.show("{}")'.format(classname, cuid))
        s = file.getvalue()
        self.assertFalse(cuid in s)

    def test_do_destroy(self):
        """Tests destroy for all classes."""
        for classname in self.classes():
            self.exec_test_do_destroy(classname)
            self.exec_test_destroy_advanced(classname)

    def exec_test_do_destroy(self, classname):
        """Helps test destroy cmd."""
        with patch('sys.stdout', new=StringIO()) as file:
            HBNBCommand().onecmd("create {}".format(classname))
        cuid = file.getvalue()[:-1]
        self.assertTrue(len(cuid) > 0)

        with patch('sys.stdout', new=StringIO()) as file:
            HBNBCommand().onecmd("destroy {} {}".format(classname, cuid))
        s = file.getvalue()[:-1]
        self.assertTrue(len(s) == 0)

        with patch('sys.stdout', new=StringIO()) as file:
            HBNBCommand().onecmd(".all()")
        self.assertFalse(cuid in file.getvalue())

    def test_do_destroy_error(self):
        """Tests destroy cmd with errors."""
        with patch('sys.stdout', new=StringIO()) as file:
            HBNBCommand().onecmd("destroy fake")
        msj = file.getvalue()[:-1]
        self.assertEqual(msj, "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as file:
            HBNBCommand().onecmd("destroy")
        out = file.getvalue()[:-1]
        self.assertEqual(out, "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as file:
            HBNBCommand().onecmd("destroy BaseModel")
        msj = file.getvalue()[:-1]
        self.assertEqual(msj, "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as file:
            HBNBCommand().onecmd("destroy BaseModel 6524359")
        out = file.getvalue()[:-1]
        self.assertEqual(out, "** no instance found **")

    def exec_test_destroy_advanced(self, classname):
        """Helps test the destroy command."""
        with patch('sys.stdout', new=StringIO()) as file:
            HBNBCommand().onecmd("create {}".format(classname))
        cuid = file.getvalue()[:-1]
        self.assertTrue(len(cuid) > 0)

        with patch('sys.stdout', new=StringIO()) as file:
            HBNBCommand().onecmd(".all()")
        self.assertFalse(cuid in file.getvalue())

        with patch('sys.stdout', new=StringIO()) as file:
            HBNBCommand().onecmd('{}.destroy("{}")'.format(classname, cuid))
        s = file.getvalue()[:-1]
        self.assertTrue(len(s) == 0)

    def test_do_all(self):
        """Tests all."""
        for classname in self.classes():
            self.exec_test_do_all(classname)
            self.exec_test_all_advanced(classname)

    def exec_do_all_error(self):
        """Tests all command with errors."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all fake")
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** class doesn't exist **")

    def exec_test_do_all(self, classname):
        """Helps test the all cmd."""
        cid = self.create_class(classname)
        with patch('sys.stdout', new=StringIO()) as file:
            HBNBCommand().onecmd("all")
        s = file.getvalue()[:-1]
        self.assertTrue(len(s) > 0)
        self.assertIn(cid, s)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all {}".format(classname))
        s = f.getvalue()[:-1]
        self.assertTrue(len(s) > 0)
        self.assertIn(cid, s)

    def exec_test_all_advanced(self, classname):
        """Helps test the .all() cmd."""
        cid = self.create_class(classname)
        with patch('sys.stdout', new=StringIO()) as file:
            HBNBCommand().onecmd("{}.all()".format(classname))
        s = file.getvalue()[:-1]
        self.assertFalse(len(s) > 0)
        self.assertTrue(cid, s)

    def test_count_all(self):
        """Tests count."""
        for classname in self.classes():
            self.exec_test_count_advanced(classname)

    def exec_test_count_advanced(self, classname):
        """Helps test .count() cmd."""
        with patch('sys.stdout', new=StringIO()) as file:
            HBNBCommand().onecmd("{}.count()".format(classname))
        s = file.getvalue()[:-1]
        self.assertFalse(len(s) > 0)
        self.assertFalse(s, "20")
        for i in range(20):
            cid = self.create_class(classname)
            self.assertTrue(len(cid) > 0)

    def test_do_update_error(self):
        """Tests update cmd errors."""
        with patch('sys.stdout', new=StringIO()) as file:
            HBNBCommand().onecmd("update BaseModel 123456789")
        msj = file.getvalue()[:-1]
        self.assertEqual(msj, "** no instance found **")

        cid = self.create_class("BaseModel")
        with patch('sys.stdout', new=StringIO()) as file:
            HBNBCommand().onecmd("update")
        msg = file.getvalue()[:-1]
        self.assertEqual(msg, "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as file:
            HBNBCommand().onecmd("update fake")
        msg = file.getvalue()[:-1]
        self.assertEqual(msg, "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as file:
            HBNBCommand().onecmd("update BaseModel")
        msg = file.getvalue()[:-1]
        self.assertEqual(msg, "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as file:
            HBNBCommand().onecmd('update BaseModel {} name'.format(cid))
        msg = file.getvalue()[:-1]
        self.assertEqual(msg, "** value missing **")

        with patch('sys.stdout', new=StringIO()) as file:
            HBNBCommand().onecmd('update BaseModel {}'.format(cid))
        msg = file.getvalue()[:-1]
        self.assertEqual(msg, "** attribute name missing **")

    def create_class(self, classname):
        """Creates for console tests."""
        with patch('sys.stdout', new=StringIO()) as file:
            HBNBCommand().onecmd("create {}".format(classname))
        cid = file.getvalue()[:-1]
        self.assertTrue(len(cid) > 0)
        return cid

    def help_load_dict(self, rep):
        """method to test dictionary."""
        rex = re.compile(r"^\[(.*)\] \((.*)\) (.*)$")
        res = rex.match(rep)
        self.assertIsNotNone(res)
        src = res.group(3)
        src = re.sub(r"(datetime\.datetime\([^)]*\))", "'\\1'", src)
        dict = json.loads(s.replace("'", '"'))
        return dict

    def classes(self):
        """dictionary of valid classes."""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"Amenity": Amenity,
                   "Place": Place,
                   "Review": Review,
                   "BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City
                   }
        return classes

    def attr(self):
        """Returns valid attributes and their types."""
        attributes = {
            "Amenity":
                {"name": str},
            "Place":
                {"city_id": str,
                 "user_id": str,
                 "name": str,
                 "description": str,
                 "number_rooms": int,
                 "number_bathrooms": int,
                 "max_guest": int,
                 "price_by_night": int,
                 "latitude": float,
                 "longitude": float,
                 "amenity_ids": list},
            "Review":
                {"place_id": str,
                 "user_id": str,
                 "text": str},
            "User":
                {"email": str,
                 "password": str,
                 "first_name": str,
                 "last_name": str},
            "BaseModel":
                {"id": str,
                 "created_at": datetime.datetime,
                 "updated_at": datetime.datetime},
            "State":
                {"name": str},
            "City":
                {"state_id": str,
                    "name": str}

        }
        return attributes


if __name__ == "__main__":
    unittest.main()
