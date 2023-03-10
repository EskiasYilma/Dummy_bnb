#!usr/bin/python3
"""
Unittest for User class
"""

import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """Unittest for the User class"""
    def test_is_instance(self):
        """Unittest for testing User is an instance of BaseModel"""
        user = User()
        self.assertIsInstance(user, BaseModel)
        self.assertTrue(hasattr(user, 'id'))
        self.assertTrue(hasattr(user, 'created_at'))
        user.save()
        self.assertTrue(hasattr(user, 'updated_at'))

    def test_emial(self):
        """Unittest for testing if User class has email attribute\
                that is an empty string"""
        user = User()
        self.assertTrue(hasattr(user, 'email'))
        self.assertEqual(user.email, "")

    def test_password(self):
        """Unittest for testing if User class has password attribute\
                that is an empty string"""
        user = User()
        self.assertTrue(hasattr(user, "password"))
        self.assertEqual(user.password, "")

    def test_first_name(self):
        """Unittest for testing if User class has first_name attribute\
                that is an empty string"""
        user = User()
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertEqual(user.first_name, "")

    def test_last_name(self):
        """Unittest for testing if User class has last_name attribute\
                that is an empty string"""
        user = User()
        self.assertTrue(hasattr(user, 'last_name'))
        self.assertEqual(user.last_name, "")

    def test_save(self):
        """Unittest for testing if User class's save method works properly"""
        user = User()
        user.save()
        self.assertNotEqual(user.created_at, user.updated_at)

    def test_to_dict(self):
        """Unittest for testing if User class's to_dict method works\
        properly"""
        user = User()
        user.save()
        user_dict = user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertIsInstance(user_dict['created_at'], str)
        self.assertIsInstance(user_dict['updated_at'], str)
        self.assertIsInstance(user_dict['id'], str)

    def test_str(self):
        """Unittest for testing if User class's str method methods works\
        properly"""
        user = User()
        string = '[User] ({}) {}'.format(user.id, user.__dict__)
        self.assertEqual(string, str(user))
