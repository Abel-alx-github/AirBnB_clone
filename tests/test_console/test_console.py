#!/usr/bin/python3
""" unittest for console"""
import unittest
from console import HBNBCommand
import cmd


class Test_Console(unittest.TestCase):
    """class to test console """

    def test_prompt(self):
        """ test the prompt"""
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)
