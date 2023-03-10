#!/usr/bin/python3
"""
Module Docstring
"""
import unittest
from models.base_model import BaseModel
from models.state import State


class TestUser(unittest.TestCase):
    """Unittest for the User class"""
    def test_is_instance(self):
        """Unittest for testing state is an instance of BaseModel"""
        state = State()
        self.assertIsInstance(state, BaseModel)
        self.assertTrue(hasattr(state, 'id'))
        self.assertTrue(hasattr(state, 'created_at'))
        state.save()
        self.assertTrue(hasattr(state, 'updated_at'))

    def test_name(self):
        """Unittest for testing if State class has name attribute\
                that is an empty string"""
        state = State()
        self.assertTrue(hasattr(state, 'name'))
        self.assertEqual(state.name, "")

    def test_save(self):
        """Unittest for testing if State class's save method works properly"""
        state = State()
        state.save()
        self.assertNotEqual(state.created_at, state.updated_at)

    def test_to_dict(self):
        """Unittest for testing if State class's to_dict method works\
        properly"""
        state = State()
        state.save()
        state_dict = state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertIsInstance(state_dict['created_at'], str)
        self.assertIsInstance(state_dict['updated_at'], str)
        self.assertIsInstance(state_dict['id'], str)

    def test_str(self):
        """Unittest for testing if User class's str method methods works\
        properly"""
        state = State()
        string = '[State] ({}) {}'.format(state.id, state.__dict__)
        self.assertEqual(string, str(state))
