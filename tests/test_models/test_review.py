#!/usr/bin/python3
""" unittest for review class"""
from models.base_model import BaseModel
from models.review import Review
import unittest


class Test_Review(unittest.TestCase):
    """ test for class Review"""

    def test_type_of_attriubute(self):
        """ test tyes of attr"""
        self.assertTrue(str, type(Review().text))
