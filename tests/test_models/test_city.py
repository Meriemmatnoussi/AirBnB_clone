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
