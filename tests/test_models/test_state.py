#!/usr/bin/python3
"""Module test_state

tests for State Class
"""

import sys
import unittest
import uuid
from datetime import datetime
from io import StringIO

import pycodestyle
from models import state
from tests.test_models.test_base_model import BaseModel

State = state.State


class TestStateDocsAndStyle(unittest.TestCase):
    """Tests State class"""

    def test_pycodestyle(self):
        """Tests compliance """
        style = pycodestyle.StyleGuide(quiet=False)
        result = style.check_files(
            ["models/state.py", "tests/test_models/test_state.py"])
        self.assertEqual(result.total_errors, 0)

    def test_module_docstring(self):
        """Tests whether"""
        self.assertTrue(len(state.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests whether"""
        self.assertTrue(len(State.__doc__) >= 1)

    def test_class_name(self):
        """Test whether"""
        self.assertEqual(State.__name__, "State")
