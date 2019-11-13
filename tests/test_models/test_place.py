#!/usr/bin/python3
"""Unittest module for the User Class."""

import unittest
from datetime import datetime
import time
from models.place import Place
from models.user import User
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):

    """Test Cases for the Place class."""

    def test_instantiation(self):
        """Tests instantiation of Place class."""

        pla = Place()
        self.assertEqual(str(type(pla)), "<class 'models.place.Place'>")
        self.assertIsInstance(pla, Place)
        self.assertTrue(issubclass(type(pla), BaseModel))

    def test_attributes(self):
        """Tests the attributes of Place class."""
        pla = Place()
        self.assertTrue(hasattr(pla, 'city_id'))
        self.assertTrue(hasattr(pla, 'user_id'))
        self.assertTrue(hasattr(pla, 'name'))
        self.assertTrue(hasattr(pla, 'description'))
        self.assertTrue(hasattr(pla, 'number_rooms'))
        self.assertTrue(hasattr(pla, 'number_bathrooms'))
        self.assertTrue(hasattr(pla, 'max_guest'))
        self.assertTrue(hasattr(pla, 'price_by_night'))
        self.assertTrue(hasattr(pla, 'latitude'))
        self.assertTrue(hasattr(pla, 'longitude'))
        self.assertTrue(hasattr(pla, 'amenity_ids'))
        self.assertEqual(type(getattr(pla, 'city_id', None)), str)
        self.assertEqual(type(getattr(pla, 'user_id', None)), str)
        self.assertEqual(type(getattr(pla, 'name', None)), str)
        self.assertEqual(type(getattr(pla, 'description', None)), str)
        self.assertEqual(type(getattr(pla, 'number_rooms', None)), int)
        self.assertEqual(type(getattr(pla, 'number_bathrooms', None)), int)
        self.assertEqual(type(getattr(pla, 'max_guest', None)), int)
        self.assertEqual(type(getattr(pla, 'price_by_night', None)), int)
        self.assertEqual(type(getattr(pla, 'latitude', None)), float)
        self.assertEqual(type(getattr(pla, 'longitude', None)), float)
        self.assertEqual(type(getattr(pla, 'amenity_ids', None)), list)


if __name__ == "__main__":
    unittest.main()
