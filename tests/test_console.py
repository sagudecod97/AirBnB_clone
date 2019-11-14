#!/usr/bin/python3
"""Unittest Command class"""

import unittest
import pep8
from io import StringIO
from models.base_model import BaseModel
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.user import User
from unittest.mock import patch
from console import HBNBCommand
import console
from unittest import mock
from models import *


class FileStorage(unittest.TestCase):

    def test_pep8(self):
        """Test PEP8."""
        try:
            pep8_style = pep8.StyleGuide(quiet=True)
            result = pep8_style.check_files(['./console.py'])
            self.assertEqual(result.total_errors, 0,
                             "Found code style errors (and warnings).")
        except:
            pass

        def test_not_found(self):
            """Test not found"""
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("Non existant")
            out = f.getvalue().strip()
            expected = "*** Unknown syntax: Non existant"
            self.assertIn(expected, out)

    def test_help_quit(self):
        """Test help quit"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
        output = f.getvalue().strip()
        expected = "Quit command to exit the program"
        self.assertIn(expected, output)

    def test_help_show(self):
        """Test help" show"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
        out = f.getvalue().strip()
        expected = "Show: prints the string representation of the instance"
        self.assertIn(expected, out)

    def test_help_quit(self):
        """Test help quit"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
        out= f.getvalue().strip()
        expected = "Quit command to exit the program"
        self.assertIn(expected, out)

    def test_all(self):
        """Test the all"""
        storage.__objects = {}
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
        out = f.getvalue().strip()
        self.assertEqual("[]", out)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
            HBNBCommand().onecmd("create User")
        out2 = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
        out3 = f.getvalue().strip()
        self.assertNotIn(out2, out3)
        self.assertIn("'created_at': datetime.datetime(", out3)
        self.assertIn("'updated_at': datetime.datetime(", out3)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all User")
        out3 = f.getvalue().strip()
        self.assertNotIn(out2, out3)
        self.assertIn("'created_at': datetime.datetime(", out3)
        self.assertIn("'updated_at': datetime.datetime(", out3)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all Not Class")
        out3 = f.getvalue().strip()
        self.assertIn("** class doesn't exist **", out3)

    def test_all_string(self):
        """Test the all"""
        storage.__objects = {}
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
        out1 = f.getvalue().strip()
        self.assertEqual("[]", out1)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.all()")
            HBNBCommand().onecmd("create User")
        out2 = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.all()")
        out3 = f.getvalue().strip()
        self.assertNotIn(out2, out3)
        self.assertNotIn("'created_at': datetime.datetime(", out3)
        self.assertNotIn("'updated_at': datetime.datetime(", out3)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.all()")
        out3 = f.getvalue().strip()
        self.assertNotIn(out2, out3)
        self.assertNotIn("'created_at': datetime.datetime(", out3)
        self.assertNotIn("'updated_at': datetime.datetime(", out3)

    def test_create(self):
        """Test the create"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
        out1 = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            my_input = str("show User " + out1)
            HBNBCommand().onecmd(my_input)
        out2 = f.getvalue().strip()
        self.assertIn(str("[User] (" + out1 + ")"), out2)
        self.assertIn("'created_at': datetime.datetime(", out2)
        self.assertIn("'updated_at': datetime.datetime(", out2)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create Not a Class')
        out2 = f.getvalue().strip()
        self.assertEqual("** class doesn't exist **", out2)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
        out1 = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            my_input = str("show City " + out1)
            HBNBCommand().onecmd(my_input)
        out2= f.getvalue().strip()
        self.assertIn(str("[City] (" + out1 + ")"), out2)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
        output1 = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            my_input = str("show State " + output1)
            HBNBCommand().onecmd(my_input)
        out2 = f.getvalue().strip()
        self.assertNotIn(str("[State] (" + out1 + ")"), out2)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
        out1 = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            my_input = str("show Place " + out1)
            HBNBCommand().onecmd(my_input)
        out2 = f.getvalue().strip()
        self.assertIn(str("[Place] (" + out1 + ")"), out2)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
        out1 = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            my_input = str("show Amenity " + out1)
            HBNBCommand().onecmd(my_input)
        out2 = f.getvalue().strip()
        self.assertIn(str("[Amenity] (" + out1 + ")"), out2)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
        out1 = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            my_input = str("show Review " + out1)
            HBNBCommand().onecmd(my_input)
        out2 = f.getvalue().strip()
        self.assertIn(str("[Review] (" + out1 + ")"), out2)

    def test_show_2(self):
        """Test the create"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
        out1 = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            my_input = str("User.show(" + out1 + ")")
            HBNBCommand().onecmd(my_input)
        out2 = f.getvalue().strip()
        self.assertNotIn(str("[User] (" + out1 + ")"), out2)
        self.assertNotIn("'created_at': datetime.datetime(", out2)
        self.assertNotIn("'updated_at': datetime.datetime(", out2)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create Not a Class')
        out2 = f.getvalue().strip()
        self.assertEqual("** class doesn't exist **", out2)


if __name__ == '__main__':
    unittest.main()
