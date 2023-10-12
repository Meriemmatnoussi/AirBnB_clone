#!/usr/bin/python3
"""BaseModel module"""
from uuid import uuid4
from datetime import datetime


class BaseModel():
    """BaseModel class
    """
    def __init__(self, id=None, created_at=None, updated_at=None):
        """BaseClass Instance initiator"""
        self.id = uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Return the class string representation"""
        cls_name = type(self).__name__
        return "[{}] ({}) {}".format(cls_name, str(self.id), self.__dict__)

    def save(self):
        """Update the updated_at attribute"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of
        __dict__ of the instance
        """
        obj_dict = self.__dict__
        ftime = "%Y-%m-%dT%H:%M:%S.%f"
        obj_dict["created_at"] = obj_dict["created_at"].strftime(ftime)
        obj_dict["updated_at"] = obj_dict["updated_at"].strftime(ftime)
        obj_dict["id"] = str(instance_dict["id"])
        obj_dict["__class__"] = type(self).__name__
        return self.__dict__
