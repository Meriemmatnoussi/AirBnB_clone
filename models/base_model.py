#!/usr/bin/python3
"""BaseModel module"""
from uuid import uuid4
from datetime import datetime


class BaseModel():
    """BaseModel class
    """
    def __init__(self, *args, **kwargs):
        """BaseClass Instance initiator"""
        if kwargs is not None and len(kwargs) != 0:
            if '__class__' in kwargs:
                del kwargs["__class__"]

            self.id = kwargs["id"]
            kwargs["created_at"] = datetime.fromisoformat(kwargs["created_at"])
            kwargs["updated_at"] = datetime.fromisoformat(kwargs["updated_at"])
            self.__dict__.update(kwargs)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            from . import storage
            storage.new(self)

    def __str__(self):
        """Return the class string representation"""
        cls_name = type(self).__name__
        return "[{}] ({}) {}".format(cls_name, str(self.id), self.__dict__)

    def save(self):
        """Update the updated_at attribute"""
        self.updated_at = datetime.now()
        from . import storage
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of
        __dict__ of the instance
        """
        obj_dict = self.__dict__
        obj_dict["created_at"] = obj_dict["created_at"].isoformat()
        obj_dict["updated_at"] = obj_dict["updated_at"].isoformat()
        obj_dict["__class__"] = type(self).__name__
        return obj_dict
