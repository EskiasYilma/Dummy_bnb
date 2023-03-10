#!/usr/bin/python3
"""
FileStorage Module Docstring

Private class attributes:

    __file_path: string - path to the JSON file (ex: file.json)
    __objects: dictionary - empty but will store all objects by \
    <class name>.id (ex: to store a BaseModel object with \
    id=12121212, the key will be BaseModel.12121212)

Public instance methods:

    all(self): returns the dictionary __objects

    new(self, obj): sets in __objects the obj with key <obj class name>.id

    save(self): serializes __objects to the JSON file (path: __file_path)

    reload(self): deserializes the JSON file to __objects (only if the JSON\
    file (__file_path) exists ; otherwise, do nothing. If the file doesn’t\
    exist, no exception should be raised)

"""

import os
import json
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.review import Review
from models.place import Place
from models.city import City
from models.amenity import Amenity


class FileStorage:
    """
    FileStorage Class Docstring

    """
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """

        """
        self.__models = {"BaseModel": BaseModel, "User": User,
                         "State": State, "Review": Review, "Place": Place,
                         "City": City, "Amenity": Amenity}

    def all(self):
        """
        all Function Docstring
        -----------------------
        Returns the dictionary __objects.
        """
        return self.__objects

    def new(self, obj):
        """
        new Function Docstring
        -----------------------
        Sets in __objects the obj with key <obj class name>.id.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        save Function Docstring
        -----------------------
        Serializes __objects to the JSON file (path: __file_path).
        """
        obj_dict = {}
        for i, j in self.__objects.items():
            obj_dict[i] = j.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
        reload Function Docstring
        -----------------------
        Deserializes the JSON file to __objects.
        """

        self.__objects = {}
        try:
            with open(self.__file_path,
                      mode="r", encoding="utf-8") as f:
                json_file = json.load(f)
        except Exception as e:
            return

        for key, value in json_file.items():
            cls = value.pop("__class__", None)
            if cls not in self.__models.keys():
                continue
            self.__objects[key] = self.__models[cls](**value)
