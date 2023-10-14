#!/usr/bin/python3
"""Module test_city

tests City Class
"""

import sys
import unittest
import uuid
from datetime import datetime
from io import StringIO

import pycodestyle
from models import city
from tests.test_models.test_base_model import BaseModel

City = city.City


class TestCityDocsAndStyle(unittest.TestCase):
    """Tests City class"""

    def test_pycodestyle(self):
        """Tests compliance with pycodestyle"""
        style = pycodestyle.StyleGuide(quiet=False)
        result = style.check_files(
            ["models/city.py", "tests/test_models/test_city.py"])
        self.assertEqual(result.total_errors, 0)

    def test_module_docstring(self):
        """Tests whether"""
        self.assertTrue(len(city.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests whether"""
        self.assertTrue(len(City.__doc__) >= 1)

    def test_class_name(self):
        """Test whether the class"""
        self.assertEqual(City.__name__, "City")


class TestCity(unittest.TestCase):
    """Test cases for City Class"""

    def setUp(self):
        """creates a test """
        self.test_obj = City()
        self.test_obj.state_id = str(uuid.uuid4())
        self.test_obj.name = "fantasy land"

    def test_city_is_subclass_of_base_model(self):
        self.assertTrue(issubclass(City, BaseModel))

    def test_public_attributes_exist(self):
        """tests wether the public"""
        req_att = ["id", "created_at", "updated_at",
                   "state_id", "name"]
        for attrib in req_att:
            self.assertTrue(hasattr(self.test_obj, attrib))

    def test_public_attributes_have_correct_type(self):
        """tests wether the public"""
        req_att = ["state_id", "name"]
        for attrib in req_att:
            self.assertTrue(type(getattr(self.test_obj, attrib)), str)
