#!/usr/bin/python3
""" define unittest for Amenity class"""
from models.base_model import BaseModel
from models.amenity import Amenity
import unittest


class Test_City(unittest.TestCase):
    """ test class for Amenity class"""

    def test_type_of_attr(self):
        """ test types of attriubute"""
        self.assertTrue(str, type(Amenity().name))
