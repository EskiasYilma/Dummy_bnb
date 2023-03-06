#!/usr/bin/python3
"""
Unittest for Base class
"""
import os
import unittest
import json
from models.base_model import BaseModel
from datetime import datetime


class TestBase_Init(unittest.TestCase):
    """Unittest for the init mathod of the BaseMOdel class"""

    def test_id(self):
        """Unittest for testing id genetated is of str type"""

        model = BaseModel()
        self.assertIsInstance(model.id, str)

    def test_created_at(self):
        """Unittest for testig created_at attribute is of datetime type"""

        model = BaseModel()
        self.assertIsInstance(model.created_at, datetime)

    def test_updated_at(self):
        """Unittest for testig updated_at attribute is of datetime type"""

        model = BaseModel()
        self.assertIsInstance(model.updated_at, datetime)

    def test_str(self):
        """Unittest for testing the str method returns the correct string"""

        model = BaseModel()
        self.assertIsInstance(str(model), str)

    def test_save(self):
        """Unittest for testing the save method updates the instance"""

        model = BaseModel()
        updated_at = model.updated_at
        model.save()
        self.assertNotEqual(updated_at, model.updated_at)

    def test_to_dict(self):
        """Unittest for testing the test_to_dict returns a dictionary and all\
                requiered elements are presented"""

        model = BaseModel()
        dict_model = model.to_dict()
        self.assertIsInstance(dict_model, dict)
        self.assertIn('__class__', dict_model)
        self.assertIn('id', dict_model)
        self.assertIn('created_at', dict_model)
        self.assertIn('updated_at', dict_model)
