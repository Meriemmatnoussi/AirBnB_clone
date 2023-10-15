#!/usr/bin/python3
"""unittest module for FileStorage class"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User


class TestFileStorage(unittest.TestCase):
    """TestFileStorage class"""
    def test_private_class_attr(self):
        """Test if the class attributes are private"""
        fs = FileStorage()

        with self.assertRaises(AttributeError):
            fs.__file_path
        with self.assertRaises(AttributeError):
            fs.__objects

    def test_all_returns_dict(self):
        """Test all() instance method"""
        fs = FileStorage()
        self.assertIsInstance(fs.all(), dict)

    def test_new(self):
        """Test new() instance method"""
        bm = BaseModel()
        fs = FileStorage()

        fs.new(bm)
        key = "BaseModel.{}".format(bm.id)
        self.assertTrue(key in fs.all())

    def test_save(self):
        """Test save() method"""
        fs = FileStorage()
        bm = BaseModel()

        bm.name = "Test object"
        fs.save()
        all_objs = fs.all()
        self.assertIn("BaseModel.{}".format(bm.id,), all_objs)
        obj = all_objs["BaseModel.{}".format(bm.id)].name
        self.assertEqual(obj, "Test object")

    def test_loading_existing_objects(self):
        """Test Loading Existing Object"""
        obj = BaseModel()
        fs = FileStorage()
        obj.name = "Test Object"

        fs.new(obj)
        fs.save()

        fs.__objects = {}
        fs.reload()

        loaded_obj = fs.all()["BaseModel." + obj.id]
        self.assertEqual(loaded_obj.id, obj.id)
        self.assertEqual(loaded_obj.name, "Test Object")
