"""TestBaseModel Module"""
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """TestBaseModel class"""
    def test_updated_at(self):
        """Test if the updated_at attribute change value when
        save() method is called
        """
        base_model = BaseModel()
        updated_at = base_model.updated_at
        base_model.save()
        updated_at2 = base_model.updated_at
        self.assertNotEqual(updated_at, updated_at2)

    def test_str(self):
        """Test the string representation of the class"""
        bm = BaseModel()
        bm_str = "[BaseModel] ({}) {}".format(bm.id, bm.__dict__)
        self.assertEqual(str(bm), bm_str)

    def test_to_dict(self):
        """Test to_dict method"""
        bm = BaseModel()
        bm_dict = bm.__dict__
        bm_dict["__class__"] = "BaseModel"
        self.assertDictEqual(bm.to_dict(), bm_dict)
