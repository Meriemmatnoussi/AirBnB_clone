#!/usr/bin/python3
"""BaseModel module"""
from uuid import uuid4
from datetime import datetime


class BaseModel():
    """BaseModel class
    """
    def __init__(self, *args, **kwargs):
        """BaseClass Instance initiator"""
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            kwargs = kwargs.pop("__class__")
#            self.id = kwargs["id"]
            self.created_at = datetime.fromisoformat(kwrags["created_at"])
            self.updated_at = datetime.fromisoformat(kwrags["updated_at"])
            

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
        obj_dict["created_at"] = obj_dict["created_at"].isoformat()
        obj_dict["updated_at"] = obj_dict["updated_at"].isoformat()
        obj_dict["__class__"] = type(self).__name__
        return obj_dict
