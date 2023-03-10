#!/usr/bin/python3
"""
Module Docstring
"""

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestUser(unittest.TestCase):
    """Unittest for the User class"""
    def test_is_instance(self):
        """Unittest for testing User is an instance of BaseModel"""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)
        self.assertTrue(hasattr(amenity, 'id'))
        self.assertTrue(hasattr(amenity, 'created_at'))
        amenity.save()
        self.assertTrue(hasattr(amenity, 'updated_at'))

    def test_name(self):
        """Unittest for testing if User class has last_name attribute\
                that is an empty string"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'name'))
        self.assertEqual(amenity.name, "")

    def test_save(self):
        """Unittest for testing if User class's save method works properly"""
        amenity = Amenity()
        amenity.save()
        self.assertNotEqual(amenity.created_at, amenity.updated_at)

    def test_to_dict(self):
        """Unittest for testing if User class's to_dict method works\
        properly"""
        amenity = Amenity()
        amenity.save()
        amenity_dict = amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertIsInstance(amenity_dict['created_at'], str)
        self.assertIsInstance(amenity_dict['updated_at'], str)
        self.assertIsInstance(amenity_dict['id'], str)

    def test_str(self):
        """Unittest for testing if User class's str method methods works\
        properly"""
        amenity = Amenity()
        string = '[Amenity] ({}) {}'.format(amenity.id, amenity.__dict__)
        self.assertEqual(string, str(amenity))
