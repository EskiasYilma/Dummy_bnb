#!/usr/bin/python3
"""
Unittest for City class
"""
import os
import uuid
import unittest
import json
from models.base_model import BaseModel
from models.city import City
from datetime import datetime


class Test_City(unittest.TestCase):
    """
    Test cases for the City class
    """

    def setUp(self):
        """
        setUp function docstring

        Setting up the test environment
        """
        self.model_1 = City()

        args = {'created_at': datetime(2023, 3, 8, 19, 30, 48, 436849),
                'updated_at': datetime(2023, 3, 8, 19, 30, 48, 436966),
                'id': 'd42f98a5-71d3-4237-83f3-f480c9dc3c18',
                'name': 'model_1'}
        self.model_2 = City(**args)
        self.model_2.save()

    def tearDown(self):
        """
        tearDown function docstring

        Clean up the test environment.
        """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_init(self):
        """
        test_init function docstring

        tests for initialization and variable attributes
        """
        self.assertIsInstance(self.model_1, City)
        self.assertTrue(hasattr(self.model_1, "created_at"))
        self.assertTrue(hasattr(self.model_1, "id"))
        self.assertFalse(hasattr(self.model_1, "updated_at"))
        self.assertTrue(hasattr(self.model_1, "name"))
        self.assertTrue(hasattr(self.model_1, "state_id"))
        self.assertEqual(self.model_1.name, "")
        self.assertEqual(self.model_1.state_id, "")

    def test_re_init(self):
        """
        test_re_init function docstring

        tests for reinitialization
        """
        self.assertIsInstance(self.model_2, City)
        self.assertEqual(self.model_2.id,
                         'd42f98a5-71d3-4237-83f3-f480c9dc3c18')
        self.assertEqual(self.model_2.created_at,
                         datetime(2023, 3, 8, 19, 30, 48, 436849))

    def test_id(self):
        """
        test_id function docstring

        tests for id attribute of City
        """
        self.assertIsNotNone(self.model_1.id)
        self.assertEqual(len(self.model_1.id), 36)
        self.assertIsInstance(self.model_1.id, str)

    def test_created_at(self):
        """
        test_created_at function docstring

        tests for created_at attribute of City
        """
        self.assertIsInstance(self.model_1.created_at, datetime)

    def test_updated_at(self):
        """
        test_updated_at function docstring

        tests for updated_at attribute of City
        """
        self.assertFalse(hasattr(self.model_1, "updated_at"))
        self.model_1.save()
        self.assertTrue(hasattr(self.model_1, "updated_at"))
        self.assertIsInstance(self.model_1.updated_at, datetime)
        self.assertTrue(hasattr(self.model_1, "name"))
        self.assertTrue(hasattr(self.model_1, "state_id"))

    def test_str(self):
        """
        test_str function docstring

        tests for the string representation of City
        """
        self.assertIsInstance(str(self.model_1), str)
        self.assertEqual(str(self.model_1),
                         "[City] ({}) {}".format(self.model_1.id,
                                                 self.model_1.__dict__))

    def test_to_dict(self):
        """
        test_to_dict function docstring

        tests for the dictionary representation of City
        """
        json_file = self.model_1.to_dict()
        self.assertTrue(isinstance(json_file, dict))
        self.assertNotEqual(self.model_1.__dict__, json_file)
        self.assertEqual(json_file["__class__"], "City")
        self.assertEqual(json_file["created_at"],
                         self.model_1.created_at.isoformat())

    def test_from_dict(self):
        """
        test_from_dict function docstring

        Test the to_dict method of the City class
        """
        json_file = self.model_2.to_dict()
        model_copy = City(**json_file)
        self.assertIsInstance(model_copy, City)
        self.assertEqual(self.model_2.id, model_copy.id)
        self.assertEqual(self.model_2.created_at, model_copy.created_at)
        self.assertEqual(self.model_2.updated_at, model_copy.updated_at)
        self.assertNotEqual(self.model_2.__dict__, json_file)
        self.assertNotIsInstance(json_file["created_at"], datetime)
        self.assertNotIsInstance(json_file["updated_at"], datetime)
        self.assertTrue(hasattr(json_file, "__class__"))

    def test_eq(self):
        """
        test_eq function docstring

        tests for model equality
        """
        self.assertTrue(self.model_1 != self.model_2)
        self.assertTrue(self.model_2 == self.model_2)

    def test_kwargs(self):
        """
        test_kwargs function docstring

        tests for kwargs init in City
        """
        self.assertIsInstance(self.model_1, City)
        self.assertTrue(hasattr(self.model_1, "created_at"))
        self.assertTrue(hasattr(self.model_1, "id"))
        self.assertFalse(hasattr(self.model_1, "updated_at"))
        self.assertTrue(hasattr(self.model_1, "name"))
        self.assertTrue(hasattr(self.model_1, "state_id"))

        args = {'created_at': datetime(2023, 3, 8, 19, 30, 48, 436849),
                'id': 'd42f98a5-71d3-4237-83f3-f480c9dc3c18',
                'name': 'model_3'}
        self.model_3 = City(**args)
        self.assertFalse(hasattr(self.model_3, "updated_at"))
        self.assertTrue(hasattr(self.model_3, "name"))
        self.assertTrue(hasattr(self.model_3, "state_id"))


if __name__ == "__main__":
    unittest.main()
