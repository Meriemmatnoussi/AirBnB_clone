#!/usr/bin/python3
"""Module test_user

tests for User Class
"""

import inspect
import sys
import unittest
from datetime import datetime
from io import StringIO

import pycodestyle
from models import user
from tests.test_models.test_base_model import BaseModel

User = user.User


class TestUserDocsAndStyle(unittest.TestCase):
    """Tests User class"""

    def test_pycodestyle(self):
        """Tests compliance"""
        style = pycodestyle.StyleGuide(quiet=False)
        result = style.check_files(
            ["models/user.py", "tests/test_models/test_user.py"])
        self.assertEqual(result.total_errors, 0)

    def test_module_docstring(self):
        """Tests whether"""
        self.assertTrue(len(user.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests whether"""
        self.assertTrue(len(User.__doc__) >= 1)

    def test_class_name(self):
        """Test whether"""
        self.assertEqual(User.__name__, "User")
