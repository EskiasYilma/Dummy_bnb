#!/usr/bin/python3

"""
Base Model Docstring
"""

import uuid
from datetime import datetime


class BaseModel:
    """
    BaseModel Class Docstring

    Defines all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        init Function Docstring
        Class Constructor
        id: string - assignes a unique uuid when an\
        instance is created
        created_at: datetime - assign with the current\
        datetime when an instance is created
        updated_at: datetime - assign with the current\
        datetime when an instance is created and it will\
        be updated every time you change
        """
        if kwargs and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self)
                    else:
                        self.id = value
                if key == "created_at":
                    self.created_at = datetime.strptime(value,
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                if key == "updated_at":
                    self.created_at = datetime.strptime(value,
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        __str__ Function Docstring
        Return: [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id,
                                     self.__dict__)

    def save(self):
        """
        save Function Docstring
        Return: Updates the public instance attribute\
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        return self.updated_at

    def to_dict(self):
        """
        to_dict Function Docstring
        Return: the dictionary representation of BaseModel
        """
        self.__dict__['__class__'] = self.__class__.__name__
        dates = {'created_at': self.created_at, 'updated_at': self.updated_at}
        for i, j in dates.items():
            self.__dict__[str(i)] = j.isoformat()
        return self.__dict__
