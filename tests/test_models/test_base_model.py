#!/usr/bin/python3
"""
Unittest for Base class
"""
import os
import uuid
import unittest
import json
from models.base_model import BaseModel
from time import sleep
from datetime import datetime


class Test_BaseModel(unittest.TestCase):
    """
    Test the base model class
    """

    def setUp(self):
        """Unittest for testing setup"""
        self.model1 = BaseModel()

        test_args = {'created_at': datetime(2023, 3, 8, 19, 30, 48, 436849),
                     'updated_at': datetime(2023, 3, 8, 19, 30, 48, 436966),
                     'id': 'd42f98a5-71d3-4237-83f3-f480c9dc3c18',
                     'name': 'model1'}
        self.model2 = BaseModel(**test_args)

    def test_instantiation(self):
        """Unittest for testing proper instantiation"""
        self.assertIsInstance(self.model1, BaseModel)
        self.assertTrue(hasattr(self.model1, "created_at"))
        self.assertTrue(hasattr(self.model1, "id"))
        self.assertFalse(hasattr(self.model1, "updated_at"))
        self.assertFalse(hasattr(self.model1, "name"))

    def test_reinstantiation(self):
        """Unittest for proper reinstantiation"""
        self.assertIsInstance(self.model2, BaseModel)
        self.assertEqual(self.model2.id,
                         'd42f98a5-71d3-4237-83f3-f480c9dc3c18')
        self.assertEqual(self.model2.created_at,
                         datetime(2023, 3, 8, 19, 30, 48, 436849))
        self.assertEqual(self.model2.updated_at,
                         datetime(2023, 3, 8, 19, 30, 48, 436966))
        self.assertEqual(self.model2.name, 'model1')

    def test_empty_kwargs(self):
        """Unittest for testing if id and created at are generated for empty\
                kwargs"""
        test_args = {}
        model = BaseModel(**test_args)
        self.assertTrue(hasattr(model, "created_at"))
        self.assertTrue(hasattr(model, "id"))

    def test_args_kwargs(self):
        """Unittest for testing args are ignored when passed with kwargs"""
        time = datetime(2023, 3, 9, 10, 8, 55, 459621)
        id_arg = 'd42f98a5-71d3-4237-83f3-f480c9dc3c18'
        model = BaseModel('1235', id_arg, created_at=time, name='Monty')
        self.assertNotEqual(model.id, 'd42f98a5-71d3-4237-83f3-f480c9dc3c18')
        self.assertEqual(model.created_at, datetime(2023, 3, 9, 10, 8, 55,
                                                    459621))
        self.assertEqual(model.name, 'Monty')

    def test_save(self):
        """Unittest for testing the save method"""
        self.assertFalse(hasattr(self.model1, "updated_at"))
        self.model1.save()
        self.assertTrue(hasattr(self.model1, "updated_at"))
        old_time = self.model2.updated_at
        self.model2.save()
        self.assertNotEqual(old_time, self.model2.updated_at)

    def test_to_dict(self):
        """Unittest for tasting the to_dict method"""
        jsonified = self.model2.to_dict()
        self.assertNotEqual(self.model2.__dict__, jsonified)
        self.assertNotIsInstance(jsonified["created_at"], datetime)
        self.assertEqual(jsonified["created_at"], '2023-03-08T19:30:48.436849')
        self.assertTrue(hasattr(jsonified, "__class__"))
        self.assertEqual(jsonified["__class__"], "BaseModel")

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
        model.save()
        self.assertIsInstance(model.updated_at, datetime)

    def test_str(self):
        """Unittest for testing the str method returns the correct string"""
        model = BaseModel()
        self.assertIsInstance(str(model), str)

    def test_to_dict(self):
        """Unittest for testing the to_dict method returns a dictionary\
                and all requiered elements are presented"""
        model = BaseModel()
        model.save()
        dict_model = model.to_dict()
        self.assertIsInstance(dict_model, dict)
        self.assertIn('__class__', dict_model)
        self.assertIn('id', dict_model)
        self.assertIn('created_at', dict_model)

    def test_id_unique_id(self):
        """Unittest for testing if ids generated are unique"""
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)

    def test_different_created_at(self):
        """Unittest for testing created_at times are different"""
        b1 = BaseModel()
        sleep(0.05)
        b2 = BaseModel()
        self.assertLess(b1.created_at, b2.created_at)
