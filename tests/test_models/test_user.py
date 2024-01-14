#!/usr/bin/python3
"""unittest for user class"""
import unittest
from models.base_model import BaseModel
from models.user import User


class Test_user(unittest.TestCase):
    """ unittest class for user class"""

    def test_type_of_user_attr(self):
        """ test types"""
        self.assertTrue(str, type(User.email))
