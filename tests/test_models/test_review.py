#!/usr/bin/python3
"""Unittest module for the User Class."""

import unittest
from datetime import datetime
import time
from models.review import Review
from models.user import User
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestReview(unittest.TestCase):

    """Test Cases for the Review class."""

    def test_instantiation(self):
        """Tests instantiation of Review class."""

        rev = Review()
        self.assertEqual(str(type(rev)), "<class 'models.review.Review'>")
        self.assertIsInstance(rev, Review)
        self.assertTrue(issubclass(type(rev), BaseModel))

    def test_attributes(self):
        """Tests the attributes of Review class."""
        rev = Review()
        self.assertTrue(hasattr(rev, 'place_id'))
        self.assertTrue(hasattr(rev, 'user_id'))
        self.assertTrue(hasattr(rev, 'text'))
        self.assertEqual(type(getattr(rev, 'place_id', None)), str)
        self.assertEqual(type(getattr(rev, 'user_id', None)), str)
        self.assertEqual(type(getattr(rev, 'text', None)), str)


if __name__ == "__main__":
    unittest.main()
