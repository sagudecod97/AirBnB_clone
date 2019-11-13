#!/usr/bin/python3
"""Unittest module for the User Class."""

import unittest
from datetime import datetime
import time
from models.state import State
from models.user import User
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestState(unittest.TestCase):

    """Test Cases for the State class."""

    def test_instantiation(self):
        """Tests instantiation of State class."""

        stat = State()
        self.assertEqual(str(type(stat)), "<class 'models.state.State'>")
        self.assertIsInstance(stat, State)
        self.assertTrue(issubclass(type(stat), BaseModel))

    def test_attributes(self):
        """Tests the attributes of State class."""
        stat = State()
        self.assertTrue(hasattr(stat, 'name'))
        self.assertEqual(type(getattr(stat, 'name', None)), str)


if __name__ == "__main__":
    unittest.main()
