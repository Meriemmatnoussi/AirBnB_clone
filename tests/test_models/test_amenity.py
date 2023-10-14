#!/usr/bin/python3
"""Module test_amenity

This Module for Amenity Class
"""

import sys
import unittest
from datetime import datetime
from io import StringIO

import pycodestyle
from models import amenity
from tests.test_models.test_base_model import BaseModel

Amenity = amenity.Amenity


class TestAmenityDocsAndStyle(unittest.TestCase):
    """Tests Amenity class """

    def test_pycodestyle(self):
        """Tests compliance """
        style = pycodestyle.StyleGuide(quiet=False)
        result = style.check_files(
            ["models/amenity.py", "tests/test_models/test_amenity.py"])
        self.assertEqual(result.total_errors, 0)

    def test_module_docstring(self):
        """Tests whether """
        self.assertTrue(len(amenity.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests whether """
        self.assertTrue(len(Amenity.__doc__) >= 1)

    def test_class_name(self):
        """Test whether"""
        self.assertEqual(Amenity.__name__, "Amenity")
