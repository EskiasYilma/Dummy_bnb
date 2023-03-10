#!/usr/bin/python3
"""
Module Docstring
"""

import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """Unittest for the Place class"""
    def test_is_instance(self):
        """Unittest for testing Place is an instance of BaseModel"""
        place = Place()
        self.assertIsInstance(place, BaseModel)
        self.assertTrue(hasattr(place, 'id'))
        self.assertTrue(hasattr(place, 'created_at'))
        place.save()
        self.assertTrue(hasattr(place, 'updated_at'))

    def test_city_id(self):
        """Unittest for testing if Place class has city_id attribute\
                that is an empty string"""
        place = Place()
        self.assertTrue(hasattr(place, 'city_id'))
        self.assertEqual(place.city_id, "")
        self.assertIsInstance(place.city_id, str)

    def test_user_id(self):
        """Unittest for testing if Place class has user_id attribute\
                that is an empty string"""
        place = Place()
        self.assertTrue(hasattr(place, "user_id"))
        self.assertEqual(place.user_id, "")
        self.assertIsInstance(place.city_id, str)

    def test_name(self):
        """Unittest for testing if Place class has name attribute\
                that is an empty string"""
        place = Place()
        self.assertTrue(hasattr(place, 'name'))
        self.assertEqual(place.name, "")
        self.assertIsInstance(place.name, str)

    def test_description(self):
        """Unittest for testing if Place class has description attribute\
                that is an empty string"""
        place = Place()
        self.assertTrue(hasattr(place, 'description'))
        self.assertEqual(place.description, "")
        self.assertIsInstance(place.description, str)

    def test_number_rooms(self):
        """Unittest for testing if Place class has number_rooms attribute\
                that is zero"""
        place = Place()
        self.assertTrue(hasattr(place, 'number_rooms'))
        self.assertEqual(place.number_rooms, 0)
        self.assertIsInstance(place.number_rooms, int)

    def test_bathrooms(self):
        """Unittest for testing if Place class has number_bathrooms attribute\
                that is zero"""
        place = Place()
        self.assertTrue(hasattr(place, 'number_bathrooms'))
        self.assertEqual(place.number_bathrooms, 0)
        self.assertIsInstance(place.number_bathrooms, int)

    def test_max_guest(self):
        """Unittest for testing if Place class has max_guest attribute\
                that is zero"""
        place = Place()
        self.assertTrue(hasattr(place, 'max_guest'))
        self.assertEqual(place.max_guest, 0)
        self.assertIsInstance(place.max_guest, int)

    def price_by_night(self):
        """Unittest for testing if Place class has price_by_night attribute\
                that is zero"""
        place = Place()
        self.assertTrue(hasattr(place, 'price_by_night'))
        self.assertEqual(place.price_by_night, 0)
        self.assertIsInstance(place.price_by_night, int)

    def test_latitude(self):
        """Unittest for testing if Place class has latitude attribute\
                that is zero"""
        place = Place()
        self.assertTrue(hasattr(place, 'latitude'))
        self.assertEqual(place.latitude, 0)
        self.assertIsInstance(place.latitude, float)

    def test_longitude(self):
        """Unittest for testing if Place class has longitude attribute\
                that is an empty string"""
        place = Place()
        self.assertTrue(hasattr(place, 'longitude'))
        self.assertEqual(place.longitude, 0)
        self.assertIsInstance(place.longitude, float)

    def test_amenity_ids(self):
        """Unittest for testing if Place class has amenity_ids attribute\
                that is an empty list"""
        place = Place()
        self.assertTrue(hasattr(place, 'amenity_ids'))
        self.assertEqual(place.amenity_ids, [])
        self.assertIsInstance(place.amenity_ids, list)

    def test_save(self):
        """Unittest for testing if Place class's save method works properly"""
        place = Place()
        place.save()
        self.assertNotEqual(place.created_at, place.updated_at)

    def test_to_dict(self):
        """Unittest for testing if Place class's to_dict method works\
        properly"""
        place = Place()
        place.save()
        place_dict = place.to_dict()
        self.assertIsInstance(place_dict, dict)
        self.assertIsInstance(place_dict['created_at'], str)
        self.assertIsInstance(place_dict['updated_at'], str)
        self.assertIsInstance(place_dict['id'], str)

    def test_str(self):
        """Unittest for testing if Place class's str method methods works\
        properly"""
        place = Place()
        string = '[Place] ({}) {}'.format(place.id, place.__dict__)
        self.assertEqual(string, str(place))
