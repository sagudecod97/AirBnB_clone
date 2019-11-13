#!/usr/bin/python3
"""Unittest module for the city Class."""

import unittest
from datetime import datetime
import time
from models.city import City
from models.user import User
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestCity(unittest.TestCase):

    """Test Cases for the User class."""

    def test_instantiation(self):
        """Tests instantiation of City class."""

        cit = City()
        self.assertEqual(str(type(cit)), "<class 'models.city.City'>")
        self.assertIsInstance(cit, City)
        self.assertTrue(issubclass(type(cit), BaseModel))

    def test_attributes(self):
        """Tests the attributes of City class."""
        cit = City()
        self.assertTrue(hasattr(cit, 'state_id'))
        self.assertTrue(hasattr(cit, 'name'))
        self.assertEqual(type(getattr(cit, 'state_id', None)), str)
        self.assertEqual(type(getattr(cit, 'name', None)), str)


if __name__ == "__main__":
    unittest.main()
