#!/usr/bin/python3
"""
Module Docstring
"""
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """Unittest for the City class"""
    def test_is_instance(self):
        """Unittest for testing City is an instance of BaseModel"""
        city = City()
        self.assertIsInstance(city, BaseModel)
        self.assertTrue(hasattr(city, 'id'))
        self.assertTrue(hasattr(city, 'created_at'))
        city.save()
        self.assertTrue(hasattr(city, 'updated_at'))

    def test_state_id(self):
        """Unittest for testing if City class has email attribute\
                that is an empty string"""
        city = City()
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertEqual(city.state_id, "")

    def test_name(self):
        """Unittest for testing if City class has first_name attribute\
                that is an empty string"""
        city = City()
        self.assertTrue(hasattr(city, 'name'))
        self.assertEqual(city.name, "")

    def test_save(self):
        """Unittest for testing if City class's save method works properly"""
        city = City()
        city.save()
        self.assertNotEqual(city.created_at, city.updated_at)

    def test_to_dict(self):
        """Unittest for testing if City class's to_dict method works\
        properly"""
        city = City()
        city.save()
        city_dict = city.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertIsInstance(city_dict['created_at'], str)
        self.assertIsInstance(city_dict['updated_at'], str)
        self.assertIsInstance(city_dict['id'], str)

    def test_str(self):
        """Unittest for testing if City class's str method methods works\
        properly"""
        city = City()
        string = '[City] ({}) {}'.format(city.id, city.__dict__)
        self.assertEqual(string, str(city))
