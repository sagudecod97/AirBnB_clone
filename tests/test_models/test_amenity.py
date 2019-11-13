#!/usr/bin/python3
"""Unittest module for the User Class."""

import unittest
from datetime import datetime
import time

from models.amenity import Amenity
from models.user import User
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):

    """Test Cases for the Amenity class."""

    def test_instantiation(self):
        """Tests instantiation of Amenity class."""

        amen = Amenity()
        self.assertEqual(str(type(amen)), "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(amen, Amenity)
        self.assertTrue(issubclass(type(amen), BaseModel))

    def test_attributes(self):
        """Tests the attributes of Amenity class."""
        amen = Amenity()
        self.assertTrue(hasattr(amen, 'name'))
        self.assertEqual(type(getattr(amen, 'name', None)), str)


if __name__ == "__main__":
    unittest.main()
