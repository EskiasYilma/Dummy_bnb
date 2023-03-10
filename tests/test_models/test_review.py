#!/usr/bin/python3
"""
Module Docstring
"""

from models.base_model import BaseModel
from models.review import Review
import unittest


class TestReview(unittest.TestCase):
    """Unittest for the Review class"""
    def test_is_instance(self):
        """Unittest for testing Review is an instance of BaseModel"""
        review = Review()
        self.assertIsInstance(review, BaseModel)
        self.assertTrue(hasattr(review, 'id'))
        self.assertTrue(hasattr(review, 'created_at'))
        review.save()
        self.assertTrue(hasattr(review, 'updated_at'))

    def test_place_id(self):
        """Unittest for testing if Review class has place_id attribute\
                that is an empty string"""
        review = Review()
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertIsInstance(review.place_id, str)
        self.assertEqual(review.place_id, "")

    def test_user_id(self):
        """Unittest for testing if Review class has user_id attribute\
                that is an empty string"""
        review = Review()
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertIsInstance(review.user_id, str)
        self.assertEqual(review.user_id, "")

    def test_text(self):
        """Unittest for testing if Review class has text attribute\
                that is an empty string"""
        review = Review()
        self.assertTrue(hasattr(review, 'text'))
        self.assertIsInstance(review.text, str)
        self.assertEqual(review.text, "")

    def test_save(self):
        """Unittest for testing if Review class's save method works properly"""
        review = Review()
        review.save()
        self.assertNotEqual(review.created_at, review.updated_at)

    def test_to_dict(self):
        """Unittest for testing if Review class's to_dict method works\
        properly"""
        review = Review()
        review.save()
        review_dict = review.to_dict()
        self.assertIsInstance(review_dict, dict)
        self.assertIsInstance(review_dict['created_at'], str)
        self.assertIsInstance(review_dict['updated_at'], str)
        self.assertIsInstance(review_dict['id'], str)

    def test_str(self):
        """Unittest for testing if Review class's str method methods works\
        properly"""
        review = Review()
        string = '[Review] ({}) {}'.format(review.id, review.__dict__)
        self.assertEqual(string, str(review))
