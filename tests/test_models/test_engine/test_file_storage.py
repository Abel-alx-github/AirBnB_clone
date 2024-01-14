#!/usr/bin/python3
"""unittest module for file_storage.py module"""
import models
import json
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.review import Review
import unittest


class Test_FileStorage_cls_(unittest.TestCase):
    ''' class to test FileStorage clas,'''

    def test_type_of_obj(self):
        """test type of instance if it is Filestorage"""
        stor = FileStorage()
        self.assertTrue(type(stor), FileStorage)

    def test_cls_attr_file_path_private(self):
        """test whether the class attribute is set to private"""
        with self.assertRaises(AttributeError):
            FileStorage().__file_path

    def test_cls_attr_objects_private(self):
        """test whether the class attribute is set to private"""
        with self.assertRaises(AttributeError):
            FileStorage.__objects

    def test_cls_method_all(self):
        """test the return type is dict """
        self.assertEqual(dict, type(FileStorage().all()))

    def test_cls_attr_type(self):
        """check type of private attr """
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_method_new(self):
        """test whether the new obj is added """
        obj = BaseModel()
        stor = FileStorage()
        stor.new = obj
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, stor.all())
