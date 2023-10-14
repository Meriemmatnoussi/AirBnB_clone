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

    def test_public_attributes_exist(self):
        """tests wether the public instance"""
        req_att = ["id", "created_at", "updated_at",
                   "city_id", "user_id", "name", "description", "number_rooms",
                   "number_bathrooms", "max_guest", "price_by_night",
                   "latitude", "longitude", "amenity_ids"]
        for attrib in req_att:
            self.assertTrue(hasattr(self.test_obj, attrib))

    def test_public_attributes_have_correct_type(self):
        """tests wether the public"""
        req_att_s = ["city_id", "user_id", "name", "description"]
        for attrib in req_att_s:
            self.assertTrue(type(getattr(self.test_obj, attrib)), str)
        req_att_i = ["number_rooms", "number_bathrooms", "max_guest",
                     "price_by_night"]
        for attrib in req_att_i:
            self.assertTrue(type(getattr(self.test_obj, attrib)), int)
        req_att_f = ["latitude", "longitude"]
        for attrib in req_att_f:
            self.assertTrue(type(getattr(self.test_obj, attrib)), float)

        self.assertTrue(type(getattr(self.test_obj, "amenity_ids")), list)

    def test_bas_str_should_print_formatted_output(self):
        """__str__ should print"""
        self.test_obj.my_number = 89
        cls_name = Place.__name__
        id = self.test_obj.id
        expected = f"[{cls_name}] ({id}) {self.test_obj.__dict__}"
        output = StringIO()
        sys.stdout = output
        print(self.test_obj)
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue().strip("\n"), expected)

