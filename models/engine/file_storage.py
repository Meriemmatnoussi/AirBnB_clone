#!/usr/bin/python3
""""FileStorage engine Module"""
import json
import os
from models.user import User
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage():
    """FileStorage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """append obj to __objects"""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        objects_items = FileStorage.__objects.items()
        serialized_objs = {key: obj.to_dict() for key, obj in objects_items}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(serialized_objs, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path) as file:
                objs_dict = json.load(file)
                for key, serialized_obj in objs_dict.items():
                    obj = eval(key.split(".")[0])(**serialized_obj)
                    FileStorage.__objects[key] = obj
