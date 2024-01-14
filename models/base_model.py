#!/usr/bin/python3
""" module that contain class defination"""
import models
import uuid
from datetime import datetime


class BaseModel:
    """defines all common attributes/methods for other classes: """

    def __init__(self, *args, **kwargs):
        """init instance:
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, val in kwargs.items():
                if key != '__class__':
                    if key == 'created_at':
                        val = datetime.fromisoformat(val)
                    elif key == 'updated_at':
                        val = datetime.fromisoformat(val)
                    setattr(self, key, val)
        else:
            models.storage.new(self)

    def __str__(self):
        """should print: [<class name>] (<self.id>) <self.__dict__>"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance"""
        dic = {key: val for key, val in (self.__dict__.items())}
        dic["__class__"] = self.__class__.__name__
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        return dic
