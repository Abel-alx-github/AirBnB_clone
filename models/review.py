#!/usr/bin/python3
""" defines class review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ class that inherits from BaseModel class"""
    place_id = ""
    user_id = ""
    text = ""
