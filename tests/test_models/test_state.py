#!/usr/bin/python3
"""
Unittest for State class
"""
import os
import uuid
import unittest
import json
from models.base_model import BaseModel
from models.state import State
from datetime import datetime


class Test_State(unittest.TestCase):
    """
    Test cases for the State class
    """

    def setUp(self):
        """
        setUp function docstring

        Setting up the test environment
        """
        self.model_1 = State()

        args = {'created_at': datetime(2023, 3, 8, 19, 30, 48, 436849),
                'updated_at': datetime(2023, 3, 8, 19, 30, 48, 436966),
                'id': 'd42f98a5-71d3-4237-83f3-f480c9dc3c18',
                'name': 'model_1'}
        self.model_2 = State(**args)
        self.model_2.save()

    def tearDown(self):
        """
        tearDown function docstring

        Clean up the test environment.
        """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_state_init(self):
        """
        test_state_init function docstring

        tests for initialization and parent class inhertances
        """
        self.assertIsInstance(self.model_1, State)
        self.assertTrue(hasattr(self.model_1, "created_at"))
        self.assertTrue(hasattr(self.model_1, "id"))
        self.assertFalse(hasattr(self.model_1, "updated_at"))

    def test_state_attribute_init(self):
        """
        test_state_attribute_init function docstring

        tests for initialization and State class attributes
        """
        self.assertTrue(hasattr(self.model_1, "name"))

    def test_state_attribute_value_init(self):
        """
        test_state_attribute_value_init function docstring

        tests for initialization and State class attributes init values
        """
        self.assertEqual(self.model_1.name, "")

    def test_state_re_init(self):
        """
        test_state_re_init function docstring

        tests for reinitialization
        """
        self.assertIsInstance(self.model_2, State)
        self.assertEqual(self.model_2.id,
                         'd42f98a5-71d3-4237-83f3-f480c9dc3c18')
        self.assertEqual(self.model_2.created_at,
                         datetime(2023, 3, 8, 19, 30, 48, 436849))

    def test_state_id(self):
        """
        test_state_id function docstring

        tests for id attribute of State
        """
        self.assertIsNotNone(self.model_1.id)
        self.assertEqual(len(self.model_1.id), 36)
        self.assertIsInstance(self.model_1.id, str)

    def test_state_created_at(self):
        """
        test_state_created_at function docstring

        tests for created_at attribute of State
        """
        self.assertIsInstance(self.model_1.created_at, datetime)

    def test_state_updated_at(self):
        """
        test_state_updated_at function docstring

        tests for updated_at attribute of State
        """
        self.assertFalse(hasattr(self.model_1, "updated_at"))
        self.model_1.save()
        self.assertTrue(hasattr(self.model_1, "updated_at"))
        self.assertIsInstance(self.model_1.updated_at, datetime)
        self.assertTrue(hasattr(self.model_1, "name"))

    def test_state_str(self):
        """
        test_state_str function docstring

        tests for the string representation of State
        """
        self.assertIsInstance(str(self.model_1), str)
        self.assertEqual(str(self.model_1),
                         "[State] ({}) {}".format(self.model_1.id,
                                                  self.model_1.__dict__))

    def test_state_to_dict(self):
        """
        test_state_to_dict function docstring

        tests for the dictionary representation of State
        """
        json_file = self.model_1.to_dict()
        self.assertTrue(isinstance(json_file, dict))
        self.assertNotEqual(self.model_1.__dict__, json_file)
        self.assertEqual(json_file["__class__"], "State")
        self.assertEqual(json_file["created_at"],
                         self.model_1.created_at.isoformat())

    def test_state_from_dict(self):
        """
        test_state_from_dict function docstring

        Test the to_dict method of the State class
        """
        json_file = self.model_2.to_dict()
        model_copy = State(**json_file)
        self.assertIsInstance(model_copy, State)
        self.assertEqual(self.model_2.id, model_copy.id)
        self.assertEqual(self.model_2.created_at, model_copy.created_at)
        self.assertEqual(self.model_2.updated_at, model_copy.updated_at)
        self.assertNotEqual(self.model_2.__dict__, json_file)
        self.assertNotIsInstance(json_file["created_at"], datetime)
        self.assertNotIsInstance(json_file["updated_at"], datetime)
        self.assertTrue(hasattr(json_file, "__class__"))

    def test_state_eq(self):
        """
        test_state_eq function docstring

        tests for model equality
        """
        self.assertTrue(self.model_1 != self.model_2)
        self.assertTrue(self.model_2 == self.model_2)

    def test_state_kwargs(self):
        """
        test_state_kwargs function docstring

        tests for kwargs init in State
        """
        self.assertIsInstance(self.model_1, State)
        self.assertTrue(hasattr(self.model_1, "created_at"))
        self.assertTrue(hasattr(self.model_1, "id"))
        self.assertFalse(hasattr(self.model_1, "updated_at"))

        args = {'created_at': datetime(2023, 3, 8, 19, 30, 48, 436849),
                'id': 'd42f98a5-71d3-4237-83f3-f480c9dc3c18',
                'name': 'model_3'}
        self.model_3 = State(**args)
        self.assertFalse(hasattr(self.model_3, "updated_at"))
        self.assertTrue(hasattr(self.model_3, "name"))


if __name__ == "__main__":
    unittest.main()
