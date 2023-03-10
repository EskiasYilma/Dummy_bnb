#!/usr/bin/python3
"""
Unittest for Review class
"""
import os
import uuid
import unittest
import json
from models.base_model import BaseModel
from models.review import Review
from datetime import datetime


class Test_Review(unittest.TestCase):
    """
    Test cases for the Review class
    """

    def setUp(self):
        """
        setUp function docstring

        Setting up the test environment
        """
        self.model_1 = Review()

        args = {'created_at': datetime(2023, 3, 8, 19, 30, 48, 436849),
                'updated_at': datetime(2023, 3, 8, 19, 30, 48, 436966),
                'id': 'd42f98a5-71d3-4237-83f3-f480c9dc3c18',
                'name': 'model_1'}
        self.model_2 = Review(**args)
        self.model_2.save()

    def tearDown(self):
        """
        tearDown function docstring

        Clean up the test environment.
        """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_review_init(self):
        """
        test_review_init function docstring

        tests for initialization and parent class inhertances
        """
        self.assertIsInstance(self.model_1, Review)
        self.assertTrue(hasattr(self.model_1, "created_at"))
        self.assertTrue(hasattr(self.model_1, "id"))
        self.assertFalse(hasattr(self.model_1, "updated_at"))

    def test_review_attribute_init(self):
        """
        test_review_attribute_init function docstring

        tests for initialization and Review class attributes
        """
        self.assertTrue(hasattr(self.model_1, "place_id"))
        self.assertTrue(hasattr(self.model_1, "user_id"))
        self.assertTrue(hasattr(self.model_1, "text"))

    def test_review_attribute_value_init(self):
        """
        test_review_attribute_value_init function docstring

        tests for initialization and Review class attributes init values
        """
        self.assertEqual(self.model_1.place_id, "")
        self.assertEqual(self.model_1.user_id, "")
        self.assertEqual(self.model_1.text, "")

    def test_review_re_init(self):
        """
        test_review_re_init function docstring

        tests for reinitialization
        """
        self.assertIsInstance(self.model_2, Review)
        self.assertEqual(self.model_2.id,
                         'd42f98a5-71d3-4237-83f3-f480c9dc3c18')
        self.assertEqual(self.model_2.created_at,
                         datetime(2023, 3, 8, 19, 30, 48, 436849))

    def test_review_id(self):
        """
        test_review_id function docstring

        tests for id attribute of Review
        """
        self.assertIsNotNone(self.model_1.id)
        self.assertEqual(len(self.model_1.id), 36)
        self.assertIsInstance(self.model_1.id, str)

    def test_review_created_at(self):
        """
        test_review_created_at function docstring

        tests for created_at attribute of Review
        """
        self.assertIsInstance(self.model_1.created_at, datetime)

    def test_review_updated_at(self):
        """
        test_review_updated_at function docstring

        tests for updated_at attribute of Review
        """
        self.assertFalse(hasattr(self.model_1, "updated_at"))
        self.model_1.save()
        self.assertTrue(hasattr(self.model_1, "updated_at"))
        self.assertIsInstance(self.model_1.updated_at, datetime)
        self.assertTrue(hasattr(self.model_1, "place_id"))
        self.assertTrue(hasattr(self.model_1, "user_id"))
        self.assertTrue(hasattr(self.model_1, "text"))

    def test_review_str(self):
        """
        test_review_str function docstring

        tests for the string representation of Review
        """
        self.assertIsInstance(str(self.model_1), str)
        self.assertEqual(str(self.model_1),
                         "[Review] ({}) {}".format(self.model_1.id,
                                                   self.model_1.__dict__))

    def test_review_to_dict(self):
        """
        test_review_to_dict function docstring

        tests for the dictionary representation of Review
        """
        json_file = self.model_1.to_dict()
        self.assertTrue(isinstance(json_file, dict))
        self.assertNotEqual(self.model_1.__dict__, json_file)
        self.assertEqual(json_file["__class__"], "Review")
        self.assertEqual(json_file["created_at"],
                         self.model_1.created_at.isoformat())

    def test_review_from_dict(self):
        """
        test_review_from_dict function docstring

        Test the to_dict method of the Review class
        """
        json_file = self.model_2.to_dict()
        model_copy = Review(**json_file)
        self.assertIsInstance(model_copy, Review)
        self.assertEqual(self.model_2.id, model_copy.id)
        self.assertEqual(self.model_2.created_at, model_copy.created_at)
        self.assertEqual(self.model_2.updated_at, model_copy.updated_at)
        self.assertNotEqual(self.model_2.__dict__, json_file)
        self.assertNotIsInstance(json_file["created_at"], datetime)
        self.assertNotIsInstance(json_file["updated_at"], datetime)
        self.assertTrue(hasattr(json_file, "__class__"))

    def test_review_eq(self):
        """
        test_review_eq function docstring

        tests for model equality
        """
        self.assertTrue(self.model_1 != self.model_2)
        self.assertTrue(self.model_2 == self.model_2)

    def test_review_kwargs(self):
        """
        test_review_kwargs function docstring

        tests for kwargs init in Review
        """
        self.assertIsInstance(self.model_1, Review)
        self.assertTrue(hasattr(self.model_1, "created_at"))
        self.assertTrue(hasattr(self.model_1, "id"))
        self.assertFalse(hasattr(self.model_1, "updated_at"))

        args = {'created_at': datetime(2023, 3, 8, 19, 30, 48, 436849),
                'id': 'd42f98a5-71d3-4237-83f3-f480c9dc3c18',
                'name': 'model_3'}
        self.model_3 = Review(**args)
        self.assertFalse(hasattr(self.model_3, "updated_at"))
        self.assertTrue(hasattr(self.model_3, "place_id"))
        self.assertTrue(hasattr(self.model_3, "user_id"))
        self.assertTrue(hasattr(self.model_3, "text"))


if __name__ == "__main__":
    unittest.main()
