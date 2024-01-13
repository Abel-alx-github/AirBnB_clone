#!/usr/bin/python3
import unittest
import models
from datetime import datetime
from models.base_model import BaseModel


class Test_BaseModel(unittest.TestCase):
    """ class to test instance attriubute of BaseModel class's object"""
    
    def test_class_type(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_uniqu_id(self):
        self.assertNotEqual(BaseModel().id, BaseModel().id)

    def test_type_of_id(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_public_id(self):
       obj = BaseModel()
       obj.id = 1000
       self.assertEqual(1000, obj.id)

    def test_type_of_created_at(self):
        self.assertIs(datetime, type(BaseModel().created_at))

    def test_type_of_updated_at(self):
        self.assertIs(datetime, type(BaseModel().updated_at))

    def test_created_at_is_different(self):
        self.assertLess(BaseModel().created_at, BaseModel().created_at)

    def test_str_repr(self):
        obj = BaseModel()
        excpected = f"[{obj.__class__.__name__}] ({obj.id}) {obj.__dict__}"
        self.assertEqual(excpected, str(obj))

    def test_kwargs_BaseModel_init(self):
        updated = datetime.isoformat(datetime.now())
        kw = {"id": 10, "created_at": updated, "updated_at": updated }
        obj = BaseModel(**kw)
        self.assertEqual(10, obj.id)
        self.assertEqual(obj.created_at, datetime.fromisoformat(updated))
        self.assertEqual(obj.updated_at, datetime.fromisoformat(updated))

class Test_To_dict(unittest.TestCase):
    """ unittest for basemodel class method 'to_dict'"""

    def test_to_dict(self):
        updated = datetime.isoformat(datetime.now())
        kw = {"id": 10, "created_at": updated, "updated_at": updated }
        obj = BaseModel(**kw)
        self.assertIn("__class__", obj.to_dict())
        self.assertIn("id", obj.to_dict())
       
    def test_type_of_to_dict(self):
        obj = BaseModel()
        self.assertTrue(dict, type(obj.to_dict()))

    def test_type_of_updated_and_created_time(self):
        obj = BaseModel()
        dictt = obj.to_dict()["updated_at"]
        self.assertTrue(str, type(dictt))
        self.assertEqual(str, type(obj.to_dict()["created_at"]))

    def test_to_dict_vs___dict__(self):
        obj = BaseModel()
        self.assertNotEqual(obj.to_dict, obj.__dict__)

class Test_save_method(unittest.TestCase):
    """unittest fot save method of instance of BaseModel class"""

    def test_is_updated_at_saved(self):
        obj = BaseModel()
        old_update_time = obj.updated_at
        obj.save()
        self.assertLess(old_update_time, obj.updated_at)
        
    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            obj = BaseModel()
            obj.save("something")






