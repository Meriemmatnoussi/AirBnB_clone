#!/usr/bin/python3
"""Module test_place

tests for Place Class
"""

import sys
import unittest
import uuid
from datetime import datetime
from io import StringIO

import pycodestyle
from models import place
from tests.test_models.test_base_model import BaseModel

Place = place.Place


class TestPlaceDocsAndStyle(unittest.TestCase):
    """Tests Place class"""

    def test_pycodestyle(self):
        """Tests compliance"""
        style = pycodestyle.StyleGuide(quiet=False)
        result = style.check_files(
            ["models/place.py", "tests/test_models/test_place.py"])
        self.assertEqual(result.total_errors, 0)

    def test_module_docstring(self):
        """Tests whether"""
        self.assertTrue(len(place.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests whether"""
        self.assertTrue(len(Place.__doc__) >= 1)

    def test_class_name(self):
        """Test whether the class"""
        self.assertEqual(Place.__name__, "Place")


class TestPlace(unittest.TestCase):
    """Test cases"""

    def setUp(self):
        """creates a test"""
        self.test_obj = Place()
        self.test_obj.city_id = str(uuid.uuid4())
        self.test_obj.user_id = str(uuid.uuid4())
        self.test_obj.name = "some place"
        self.test_obj.description = "example description"
        self.test_obj.number_rooms = 3
        self.test_obj.number_bathrooms = 3
        self.test_obj.max_guest = 3
        self.test_obj.price_by_night = 3
        self.test_obj.latitude = 10.56
        self.test_obj.longitude = 34.34
        self.test_obj.amenity_ids = [
            str(uuid.uuid4()), str(uuid.uuid4())
        ]

    def test_place_is_subclass_of_base_model(self):
        self.assertTrue(issubclass(Place, BaseModel))
