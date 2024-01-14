#!/usr/bin/python3
"""define city class """
from models.base_model import BaseModel


class City(BaseModel):
    """ class that inherits basemodel class"""
    state_id = ""
    name = ""
