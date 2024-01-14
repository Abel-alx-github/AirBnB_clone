#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Defines the FileStorage class."""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        all_dic = self.__objects
        dic = {obj: all_dic[obj].to_dict() for obj in all_dic.keys()}
        with open(self.__file_path, 'w') as j_file:
            json.dump(dic, j_file)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file"""
        try:
            with open(FileStorage.__file_path, 'r') as j_file:
                obj_dic = json.load(j_file)
                for key, value in obj_dic.items():
                    cls, obj_id = key.split('.')
                    cls = eval(cls)
                    instance = cls(**value)
                    self.__objects[key] = instance
        except FileNotFoundError:
            return
