#!/usr/bin/python3
"""
Unittest for Base class
"""
import os
import unittest
import json
from models.base_model import BaseModel
from datetime import datetime


# class TestBase_Init(unittest.TestCase):
#     """Unittest for the init mathod of the BaseMOdel class"""

#     def test_id(self):
#         """Unittest for testing id genetated is of str type"""

#         model = BaseModel()
#         self.assertIsInstance(model.id, str)

#     def test_created_at(self):
#         """Unittest for testig created_at attribute is of datetime type"""

#         model = BaseModel()
#         self.assertIsInstance(model.created_at, datetime)

#     def test_updated_at(self):
#         """Unittest for testig updated_at attribute is of datetime type"""

#         model = BaseModel()
#         self.assertIsInstance(model.updated_at, datetime)

#     def test_str(self):
#         """Unittest for testing the str method returns the correct string"""

#         model = BaseModel()
#         self.assertIsInstance(str(model), str)

#     def test_save(self):
#         """Unittest for testing the save method updates the instance"""

#         model = BaseModel()
#         updated_at = model.updated_at
#         model.save()
#         self.assertNotEqual(updated_at, model.updated_at)

#     def test_to_dict(self):
#         """Unittest for testing the to_dict method returns a dictionary\
#                 and all requiered elements are presented"""

#         model = BaseModel()
#         dict_model = model.to_dict()
#         self.assertIsInstance(dict_model, dict)
#         self.assertIn('__class__', dict_model)
#         self.assertIn('id', dict_model)
#         self.assertIn('created_at', dict_model)
#         self.assertIn('updated_at', dict_model)

#     def test_kwargs(self):
#         """Unittest for testing proper handling of kwargs"""

#         kwargs = {"id": "12345", "created_at": "2023-01-15T01:30:40.000000",
#                   "updated_at": "2023-01-15T01:30:45.000000",
#                   "name": "BaseModel", "value": 1234}
#         model = BaseModel(**kwargs)
#         self.assertEqual(model.id, kwargs["id"])
#         self.assertEqual(model.created_at, datetime.strptime(
#             kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f"))
#         self.assertEqual(model.updated_at, datetime.strptime(
#             kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f"))
#         self.assertEqual(model.__dict__["name"], kwargs["name"])
#         self.assertEqual(model.__dict__["value"], kwargs["value"])


# Sample Tests



class Test_BaseModel(unittest.TestCase):
    """
    Test the base model class
    """

    def setUp(self):
        self.model1 = BaseModel()

        test_args = {'created_at': datetime(2023, 3, 8, 19, 30, 48, 436849),
                     'updated_at': datetime(2023, 3, 8, 19, 30, 48, 436966),
                     'id': 'eab0171e-dfeb-49e8-afc4-65a864ddada2',
                     'name': 'model1'}
        self.model2 = BaseModel(test_args)
        self.model2.save()

    def test_instantiation(self):
        self.assertIsInstance(self.model1, BaseModel)
        self.assertTrue(hasattr(self.model1, "created_at"))
        self.assertTrue(hasattr(self.model1, "id"))
        self.assertFalse(hasattr(self.model1, "updated_at"))

    def test_reinstantiation(self):
        self.assertIsInstance(self.model2, BaseModel)
        self.assertEqual(self.model2.id,
                         'eab0171e-dfeb-49e8-afc4-65a864ddada2')
        self.assertEqual(self.model2.created_at,
                         datetime(2023, 3, 8, 19, 30, 48, 436849))

    def test_save(self):
        self.assertFalse(hasattr(self.model1, "updated_at"))
        self.model1.save()
        self.assertTrue(hasattr(self.model1, "updated_at"))
        old_time = self.model2.updated_at
        self.model2.save()
        self.assertNotEqual(old_time, self.model2.updated_at)

    def test_to_dict(self):
        jsonified = self.model2.to_dict()
        self.assertNotEqual(self.model2.__dict__, jsonified)
        self.assertNotIsInstance(jsonified["created_at"], datetime)
        self.assertNotIsInstance(jsonified["updated_at"], datetime)
        self.assertEqual(jsonified["created_at"], '2023-03-08T19:30:48.436849')
        self.assertTrue(hasattr(jsonified, "__class__"))
        self.assertEqual(jsonified["__class__"], "BaseModel")
