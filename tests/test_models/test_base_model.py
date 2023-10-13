"""TestBaseModel Module"""
import unittest
from models.base_model import BaseModel
import time
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """TestBaseModel class"""
    def test_init_no_args(self):
        """constructor works when called without any arguments"""
        bm = BaseModel()
        self.assertIsInstance(bm, BaseModel)
        self.assertIsNotNone(bm.id)
        self.assertIsInstance(bm.created_at, datetime)
        self.assertIsInstance(bm.updated_at, datetime)

    def test_constructor_attributes(self):
        """Test if attributes id, created_at and updated_at are
        initialized correctly
        """
        bm = BaseModel()

        self.assertTrue(
                hasattr(bm, "id"),
                "BaseModel does not have the an 'id' attribute"
        )
        self.assertTrue(
                hasattr(bm, "created_at"),
                "BaseModel does not have the an 'created_at' attribute"
        )
        self.assertTrue(
                hasattr(bm, "updated_at"),
                "BaseModel does not have the an 'updated_at' attribute"
        )

    def test_attr_type(self):
        """Test whether id, created_at and updated_at have the correct type"""
        bm = BaseModel()
        self.assertIsInstance(bm.id, str, "'id' is not a string.")
        self.assertIsInstance(
                bm.created_at,
                datetime,
                "'created_at' is not a datetime object."
        )
        self.assertIsInstance(
                bm.updated_at,
                datetime,
                "'updated_at' is not a datetime object."
        )

    def test_save(self):
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

    def test_unique_id(self):
        """Test if two instances have different ids"""
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_timestamps_attributes(self):
        """Test if created_at and updated_at instance attributes
        were assigned to the current datetime at initiatization
        """
        bm1 = BaseModel()
        time.sleep(1)
        bm2 = BaseModel()
        created_at_difference = bm2.created_at - bm1.updated_at
        updated_at_difference = bm2.updated_at - bm1.updated_at
        self.assertEqual(created_at_difference.seconds, 1)
        self.assertEqual(updated_at_difference.seconds, 1)

    def test_serialization_format(self):
        """Test serialization format of created_at and updated_at format"""
        bm = BaseModel()
        created_at_iso = bm.created_at.isoformat()
        updated_at_iso = bm.updated_at.isoformat()

        bm_dict = bm.to_dict()

        self.assertEqual(created_at_iso, bm_dict["created_at"])
        self.assertEqual(updated_at_iso, bm_dict["updated_at"])

    def test_init_with_kwargs(self):
        """"Test if __init__ correctly assigns attrs when **kwargs
        are provided
        """
        data = {
            "id": "test_id",
            "created_at": "2023-10-13T00:00:00.000000",
            "updated_at": "2023-10-14T00:00:00.000000"
        }
        bm = BaseModel(**data)

        self.assertIsInstance(bm, BaseModel)
        self.assertEqual(bm.id, "test_id")
        self.assertEqual(bm.created_at, datetime(2023, 10, 13, 0))
        self.assertEqual(bm.updated_at, datetime(2023, 10, 14, 0))

    def test_created_updated_conversion(self):
        """Test created_at and updated_at attrs if correctly converted"""
        data = {
            "id": "test_id",
            "created_at": "2023-10-13T00:00:00.000000",
            "updated_at": "2023-10-14T00:00:00.000000",
        }
        bm = BaseModel(**data)
        self.assertIsInstance(bm.created_at, datetime)
        self.assertEqual(bm.created_at, datetime(2023, 10, 13, 0))
        self.assertIsInstance(bm.updated_at, datetime)
        self.assertEqual(bm.updated_at, datetime(2023, 10, 14, 0))

    def test_no_class_attribute(self):
        """Test that the __class__ atribute isn't added as an instance
        attribute when using **kwargs
        """
        data = {
            "id": "test_id",
            "created_at": "2023-10-13T00:00:00.000000",
            "updated_at": "2023-10-14T00:00:00.000000",
            "__class__": "BaseModel"
        }
        bm = BaseModel(**data)
        self.assertFalse("__class__" in bm.__dict__)
