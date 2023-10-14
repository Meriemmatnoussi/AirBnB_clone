#!/usr/bin/python3
"""Module test_review

tests for Review Class
"""

import sys
import unittest
import uuid
from datetime import datetime
from io import StringIO

import pycodestyle
from models import review
from tests.test_models.test_base_model import BaseModel

Review = review.Review


class TestReviewDocsAndStyle(unittest.TestCase):
    """Tests Review"""

    def test_pycodestyle(self):
        """Tests compliance"""
        style = pycodestyle.StyleGuide(quiet=False)
        result = style.check_files(
            ["models/review.py", "tests/test_models/test_review.py"])
        self.assertEqual(result.total_errors, 0)

    def test_module_docstring(self):
        """Tests whether """
        self.assertTrue(len(review.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests whether"""
        self.assertTrue(len(Review.__doc__) >= 1)

    def test_class_name(self):
        """Test whether"""
        self.assertEqual(Review.__name__, "Review")
