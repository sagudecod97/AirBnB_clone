#!/usr/bin/python3
"""Unittest module for the User Class."""

import unittest
from datetime import datetime
import time
from models.user import User
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestUser(unittest.TestCase):

    """Test Cases for the User class."""

    def test_instantiation(self):
        """Tests instantiation of User class."""

        inst = User()
        self.assertEqual(str(type(inst)), "<class 'models.user.User'>")
        self.assertIsInstance(inst, User)
        self.assertTrue(issubclass(type(inst), BaseModel))

    def test_attributes(self):
        """Tests the attributes of User class."""
        usr = User()
        self.assertTrue(hasattr(usr, 'id'))
        self.assertTrue(hasattr(usr, 'created_at'))
        self.assertTrue(hasattr(usr, 'updated_at'))
        self.assertTrue(hasattr(usr, 'email'))
        self.assertTrue(hasattr(usr, 'password'))
        self.assertTrue(hasattr(usr, 'first_name'))
        self.assertTrue(hasattr(usr, 'last_name'))
        self.assertEqual(type(getattr(usr, 'id', None)), str)
        self.assertEqual(type(getattr(usr, 'created_at', None)), datetime)
        self.assertEqual(type(getattr(usr, 'updated_at', None)), datetime)
        self.assertEqual(type(getattr(usr, 'email', None)), str)
        self.assertEqual(type(getattr(usr, 'password', None)), str)
        self.assertEqual(type(getattr(usr, 'first_name', None)), str)
        self.assertEqual(type(getattr(usr, 'last_name', None)), str)


if __name__ == "__main__":
    unittest.main()
