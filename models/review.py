#!/usr/bin/python3
"""Module for class review."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class review that inherits from BaseModel."""
    place_id = ""
    user_id = ""
    text = ""
