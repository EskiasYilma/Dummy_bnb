#!/usr/bin/python3
"""
Unittest for Place class
"""
import os
import uuid
import unittest
import json
from models.base_model import BaseModel
from models.place import Place
from datetime import datetime


class Test_Place(unittest.TestCase):
    """
    Test cases for the Place class
    """

    def setUp(self):
        """
        setUp function docstring

        Setting up the test environment
        """
        self.model_1 = Place()

        args = {'created_at': datetime(2023, 3, 8, 19, 30, 48, 436849),
                'updated_at': datetime(2023, 3, 8, 19, 30, 48, 436966),
                'id': 'd42f98a5-71d3-4237-83f3-f480c9dc3c18',
                'name': 'model_1'}
        self.model_2 = Place(**args)
        self.model_2.save()

    def tearDown(self):
        """
        tearDown function docstring

        Clean up the test environment.
        """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_place_init(self):
        """
        test_place_init function docstring

        tests for initialization and parent class inhertances
        """
        self.assertIsInstance(self.model_1, Place)
        self.assertTrue(hasattr(self.model_1, "created_at"))
        self.assertTrue(hasattr(self.model_1, "id"))
        self.assertFalse(hasattr(self.model_1, "updated_at"))

    def test_place_attribute_init(self):
        """
        test_place_attribute_init function docstring

        tests for initialization and Place class attributes
        """
        self.assertTrue(hasattr(self.model_1, "city_id"))
        self.assertTrue(hasattr(self.model_1, "user_id"))
        self.assertTrue(hasattr(self.model_1, "name"))
        self.assertTrue(hasattr(self.model_1, "description"))
        self.assertTrue(hasattr(self.model_1, "number_rooms"))
        self.assertTrue(hasattr(self.model_1, "number_bathrooms"))
        self.assertTrue(hasattr(self.model_1, "max_guest"))
        self.assertTrue(hasattr(self.model_1, "price_by_night"))
        self.assertTrue(hasattr(self.model_1, "latitude"))
        self.assertTrue(hasattr(self.model_1, "longitude"))
        self.assertTrue(hasattr(self.model_1, "amenity_ids"))

    def test_place_attribute_value_init(self):
        """
        test_place_attribute_value_init function docstring

        tests for initialization and Place class attributes init values
        """
        self.assertEqual(self.model_1.city_id, "")
        self.assertEqual(self.model_1.user_id, "")
        self.assertEqual(self.model_1.name, "")
        self.assertEqual(self.model_1.description, "")
        self.assertEqual(self.model_1.number_rooms, 0)
        self.assertEqual(self.model_1.number_bathrooms, 0)
        self.assertEqual(self.model_1.max_guest, 0)
        self.assertEqual(self.model_1.price_by_night, 0)
        self.assertEqual(self.model_1.latitude, 0.0)
        self.assertEqual(self.model_1.longitude, 0.0)
        self.assertEqual(self.model_1.amenity_ids, [])

    def test_place_re_init(self):
        """
        test_place_re_init function docstring

        tests for reinitialization
        """
        self.assertIsInstance(self.model_2, Place)
        self.assertEqual(self.model_2.id,
                         'd42f98a5-71d3-4237-83f3-f480c9dc3c18')
        self.assertEqual(self.model_2.created_at,
                         datetime(2023, 3, 8, 19, 30, 48, 436849))

    def test_place_id(self):
        """
        test_place_id function docstring

        tests for id attribute of Place
        """
        self.assertIsNotNone(self.model_1.id)
        self.assertEqual(len(self.model_1.id), 36)
        self.assertIsInstance(self.model_1.id, str)

    def test_place_created_at(self):
        """
        test_place_created_at function docstring

        tests for created_at attribute of Place
        """
        self.assertIsInstance(self.model_1.created_at, datetime)

    def test_place_updated_at(self):
        """
        test_place_updated_at function docstring

        tests for updated_at attribute of Place
        """
        self.assertFalse(hasattr(self.model_1, "updated_at"))
        self.model_1.save()
        self.assertTrue(hasattr(self.model_1, "updated_at"))
        self.assertIsInstance(self.model_1.updated_at, datetime)
        self.assertTrue(hasattr(self.model_1, "city_id"))
        self.assertTrue(hasattr(self.model_1, "user_id"))
        self.assertTrue(hasattr(self.model_1, "name"))
        self.assertTrue(hasattr(self.model_1, "description"))
        self.assertTrue(hasattr(self.model_1, "number_rooms"))
        self.assertTrue(hasattr(self.model_1, "number_bathrooms"))
        self.assertTrue(hasattr(self.model_1, "max_guest"))
        self.assertTrue(hasattr(self.model_1, "price_by_night"))
        self.assertTrue(hasattr(self.model_1, "latitude"))
        self.assertTrue(hasattr(self.model_1, "longitude"))
        self.assertTrue(hasattr(self.model_1, "amenity_ids"))

    def test_place_str(self):
        """
        test_place_str function docstring

        tests for the string representation of Place
        """
        self.assertIsInstance(str(self.model_1), str)
        self.assertEqual(str(self.model_1),
                         "[Place] ({}) {}".format(self.model_1.id,
                                                  self.model_1.__dict__))

    def test_place_to_dict(self):
        """
        test_place_to_dict function docstring

        tests for the dictionary representation of Place
        """
        json_file = self.model_1.to_dict()
        self.assertTrue(isinstance(json_file, dict))
        self.assertNotEqual(self.model_1.__dict__, json_file)
        self.assertEqual(json_file["__class__"], "Place")
        self.assertEqual(json_file["created_at"],
                         self.model_1.created_at.isoformat())

    def test_place_from_dict(self):
        """
        test_place_from_dict function docstring

        Test the to_dict method of the Place class
        """
        json_file = self.model_2.to_dict()
        model_copy = Place(**json_file)
        self.assertIsInstance(model_copy, Place)
        self.assertEqual(self.model_2.id, model_copy.id)
        self.assertEqual(self.model_2.created_at, model_copy.created_at)
        self.assertEqual(self.model_2.updated_at, model_copy.updated_at)
        self.assertNotEqual(self.model_2.__dict__, json_file)
        self.assertNotIsInstance(json_file["created_at"], datetime)
        self.assertNotIsInstance(json_file["updated_at"], datetime)
        self.assertTrue(hasattr(json_file, "__class__"))

    def test_place_eq(self):
        """
        test_place_eq function docstring

        tests for model equality
        """
        self.assertTrue(self.model_1 != self.model_2)
        self.assertTrue(self.model_2 == self.model_2)

    def test_place_kwargs(self):
        """
        test_place_kwargs function docstring

        tests for kwargs init in Place
        """
        self.assertIsInstance(self.model_1, Place)
        self.assertTrue(hasattr(self.model_1, "created_at"))
        self.assertTrue(hasattr(self.model_1, "id"))
        self.assertFalse(hasattr(self.model_1, "updated_at"))
        self.assertTrue(hasattr(self.model_1, "city_id"))
        self.assertTrue(hasattr(self.model_1, "user_id"))
        self.assertTrue(hasattr(self.model_1, "name"))
        self.assertTrue(hasattr(self.model_1, "description"))
        self.assertTrue(hasattr(self.model_1, "number_rooms"))
        self.assertTrue(hasattr(self.model_1, "number_bathrooms"))
        self.assertTrue(hasattr(self.model_1, "max_guest"))
        self.assertTrue(hasattr(self.model_1, "price_by_night"))
        self.assertTrue(hasattr(self.model_1, "latitude"))
        self.assertTrue(hasattr(self.model_1, "longitude"))
        self.assertTrue(hasattr(self.model_1, "amenity_ids"))

        args = {'created_at': datetime(2023, 3, 8, 19, 30, 48, 436849),
                'id': 'd42f98a5-71d3-4237-83f3-f480c9dc3c18',
                'name': 'model_3'}
        self.model_3 = Place(**args)
        self.assertFalse(hasattr(self.model_3, "updated_at"))
        self.assertTrue(hasattr(self.model_3, "city_id"))
        self.assertTrue(hasattr(self.model_3, "user_id"))
        self.assertTrue(hasattr(self.model_3, "name"))
        self.assertTrue(hasattr(self.model_3, "description"))
        self.assertTrue(hasattr(self.model_3, "number_rooms"))
        self.assertTrue(hasattr(self.model_3, "number_bathrooms"))
        self.assertTrue(hasattr(self.model_3, "max_guest"))
        self.assertTrue(hasattr(self.model_3, "price_by_night"))
        self.assertTrue(hasattr(self.model_3, "latitude"))
        self.assertTrue(hasattr(self.model_3, "longitude"))
        self.assertTrue(hasattr(self.model_3, "amenity_ids"))


if __name__ == "__main__":
    unittest.main()
