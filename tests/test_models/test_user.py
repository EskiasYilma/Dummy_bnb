#!/usr/bin/python3
"""
Unittest for User class
"""
import os
import uuid
import unittest
import json
from models.base_model import BaseModel
from models.user import User
from datetime import datetime


class Test_User(unittest.TestCase):
    """
    Test cases for the User class
    """

    def setUp(self):
        """
        setUp function docstring

        Setting up the test environment
        """
        self.model_1 = User()

        args = {'created_at': datetime(2023, 3, 8, 19, 30, 48, 436849),
                'updated_at': datetime(2023, 3, 8, 19, 30, 48, 436966),
                'id': 'd42f98a5-71d3-4237-83f3-f480c9dc3c18',
                'name': 'model_1'}
        self.model_2 = User(**args)
        self.model_2.save()

    def tearDown(self):
        """
        tearDown function docstring

        Clean up the test environment.
        """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_user_init(self):
        """
        test_user_init function docstring

        tests for initialization and parent class inhertances
        """
        self.assertIsInstance(self.model_1, User)
        self.assertTrue(hasattr(self.model_1, "created_at"))
        self.assertTrue(hasattr(self.model_1, "id"))
        self.assertFalse(hasattr(self.model_1, "updated_at"))

    def test_user_attribute_init(self):
        """
        test_user_attribute_init function docstring

        tests for initialization and User class attributes
        """
        self.assertTrue(hasattr(self.model_1, "email"))
        self.assertTrue(hasattr(self.model_1, "password"))
        self.assertTrue(hasattr(self.model_1, "first_name"))
        self.assertTrue(hasattr(self.model_1, "last_name"))

    def test_user_attribute_value_init(self):
        """
        test_user_attribute_value_init function docstring

        tests for initialization and User class attributes init values
        """
        self.assertEqual(self.model_1.email, "")
        self.assertEqual(self.model_1.password, "")
        self.assertEqual(self.model_1.first_name, "")
        self.assertEqual(self.model_1.last_name, "")

    def test_user_re_init(self):
        """
        test_user_re_init function docstring

        tests for reinitialization
        """
        self.assertIsInstance(self.model_2, User)
        self.assertEqual(self.model_2.id,
                         'd42f98a5-71d3-4237-83f3-f480c9dc3c18')
        self.assertEqual(self.model_2.created_at,
                         datetime(2023, 3, 8, 19, 30, 48, 436849))

    def test_user_id(self):
        """
        test_user_id function docstring

        tests for id attribute of User
        """
        self.assertIsNotNone(self.model_1.id)
        self.assertEqual(len(self.model_1.id), 36)
        self.assertIsInstance(self.model_1.id, str)

    def test_user_created_at(self):
        """
        test_user_created_at function docstring

        tests for created_at attribute of User
        """
        self.assertIsInstance(self.model_1.created_at, datetime)

    def test_user_updated_at(self):
        """
        test_user_updated_at function docstring

        tests for updated_at attribute of User
        """
        self.assertFalse(hasattr(self.model_1, "updated_at"))
        self.model_1.save()
        self.assertTrue(hasattr(self.model_1, "updated_at"))
        self.assertIsInstance(self.model_1.updated_at, datetime)
        self.assertTrue(hasattr(self.model_1, "email"))
        self.assertTrue(hasattr(self.model_1, "password"))
        self.assertTrue(hasattr(self.model_1, "first_name"))
        self.assertTrue(hasattr(self.model_1, "last_name"))

    def test_user_str(self):
        """
        test_user_str function docstring

        tests for the string representation of User
        """
        self.assertIsInstance(str(self.model_1), str)
        self.assertEqual(str(self.model_1),
                         "[User] ({}) {}".format(self.model_1.id,
                                                 self.model_1.__dict__))

    def test_user_to_dict(self):
        """
        test_user_to_dict function docstring

        tests for the dictionary representation of User
        """
        json_file = self.model_1.to_dict()
        self.assertTrue(isinstance(json_file, dict))
        self.assertNotEqual(self.model_1.__dict__, json_file)
        self.assertEqual(json_file["__class__"], "User")
        self.assertEqual(json_file["created_at"],
                         self.model_1.created_at.isoformat())

    def test_user_from_dict(self):
        """
        test_user_from_dict function docstring

        Test the to_dict method of the User class
        """
        json_file = self.model_2.to_dict()
        model_copy = User(**json_file)
        self.assertIsInstance(model_copy, User)
        self.assertEqual(self.model_2.id, model_copy.id)
        self.assertEqual(self.model_2.created_at, model_copy.created_at)
        self.assertEqual(self.model_2.updated_at, model_copy.updated_at)
        self.assertNotEqual(self.model_2.__dict__, json_file)
        self.assertNotIsInstance(json_file["created_at"], datetime)
        self.assertNotIsInstance(json_file["updated_at"], datetime)
        self.assertTrue(hasattr(json_file, "__class__"))

    def test_user_eq(self):
        """
        test_user_eq function docstring

        tests for model equality
        """
        self.assertTrue(self.model_1 != self.model_2)
        self.assertTrue(self.model_2 == self.model_2)

    def test_user_kwargs(self):
        """
        test_user_kwargs function docstring

        tests for kwargs init in User
        """
        self.assertIsInstance(self.model_1, User)
        self.assertTrue(hasattr(self.model_1, "created_at"))
        self.assertTrue(hasattr(self.model_1, "id"))
        self.assertFalse(hasattr(self.model_1, "updated_at"))

        args = {'created_at': datetime(2023, 3, 8, 19, 30, 48, 436849),
                'id': 'd42f98a5-71d3-4237-83f3-f480c9dc3c18',
                'name': 'model_3'}
        self.model_3 = User(**args)
        self.assertFalse(hasattr(self.model_3, "updated_at"))
        self.assertTrue(hasattr(self.model_3, "email"))
        self.assertTrue(hasattr(self.model_3, "password"))
        self.assertTrue(hasattr(self.model_3, "first_name"))
        self.assertTrue(hasattr(self.model_3, "last_name"))


if __name__ == "__main__":
    unittest.main()
