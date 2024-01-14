#!/usr/bin/python3
""" define unittest for Place class"""
from models.base_model import BaseModel
from models.place import Place
import unittest


class Test_Place(unittest.TestCase):
    """ test class for city class"""

    def test_type_of_attr(self):
        """ test types of attriubute"""
        self.assertTrue(str, type(Place().city_id))
