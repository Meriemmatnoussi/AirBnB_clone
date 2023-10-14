#!/usr/bin/python3
"""
Defines the review model
"""
from .base_model import BaseModel


class Review(BaseModel):
    """
    Review objects
    """
    user_id = ""
    place_id = ""
    text = ""
