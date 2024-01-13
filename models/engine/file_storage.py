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
        return self.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        dic = {obj: self.__objects[obj].to_dict()
               for obj in self.__objects.keys()}
        with open(self.__file_path, 'w') as j_file:
            json.dump(dic, j_file)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r') as j_file:
                obj_dic = json.load(j_file)
                for obj in obj_dic.values():
                    class_name = obj["__class__"]
                    del obj['__class__']
                    self.new(eval(class_name)(**obj))
        except FileNotFoundError:
            return
