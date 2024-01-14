#!/usr/bin/python3
""" define unittest for city class"""
from models.base_model import BaseModel
from models.city import City
import unittest


class Test_City(unittest.TestCase):
    """ test class for city class"""

    def test_type_of_attr(self):
        """ test types of attriubute"""
        self.assertTrue(str, type(City().state_id))
