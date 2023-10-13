#!/usr/bin/python3
""""FileStorage engine Module"""
import json
import os


class FileStorage():
    """FileStorage class"""
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """instance initiator"""
        pass

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """append obj to __objects"""
        FileStorage.__objects[type(obj).__name__] = obj.id

    def save(self):
        """serializes __objects to the JSON file"""
        with open(FileStorage.__file_path, "w+") as f:
            objs = {}
            for key, val in FileStorage.__objects.items():
                objs[key] = val
            json.dump(objs, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if os.path.isfile(FileStorage.__file_path):
            return json.load(FileStorage.__file_path)
