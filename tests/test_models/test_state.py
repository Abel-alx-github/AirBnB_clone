#!/usr/bin/python3
""" define unittest for State class"""
from models.base_model import BaseModel
from models.state import State
import unittest


class Test_State(unittest.TestCase):
    """ test class for state class"""

    def test_type_of_attr(self):
        """ test types of attriubute"""
        self.assertTrue(str, type(State().name))
