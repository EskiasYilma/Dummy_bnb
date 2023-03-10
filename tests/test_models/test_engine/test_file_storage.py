#!/usr/bin/python3
"""
Unittest for FileStorage class
"""
import unittest
import os.path
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.place import Place
from models.engine.file_storage import FileStorage
import doctest


class TestFileStorage(unittest.TestCase):
    """
    Test cases for the FileStorage class.
    """

    def setUp(self):
        """
        setUp function docstring

        Set up the test environment.
        """
        self.storage = FileStorage()
        self.json_file_length = 0
        if os.path.isfile("file.json"):
            self.json_file_length = len(self.storage.all())

    def tearDown(self):
        """
        tearDown function docstring

        Clean up the test environment.
        """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_FS_docstrings(self):
        """
        test_FS_docstrings function docstring

        Test if all classes and methods in FileStorage have docstrings
        """
        failure_count, test_count = doctest.testmod()
        self.assertEqual(failure_count,
                         0,
                         f"{failure_count}/{test_count} tests failed")

    def test_all(self):
        """
        test_all function docstring

        Test that the all method returns the expected dictionary.
        """

        self.assertEqual(len(self.storage.all()), self.json_file_length)

    def test_new(self):
        """
        test_new function docstring

        Test that the new method adds an object to the __objects dictionary.
        """
        model = BaseModel()
        self.storage.new(model)
        key = "{}.{}".format(model.__class__.__name__, model.id)
        self.assertIn(key, self.storage.all().keys())
        self.assertEqual(len(self.storage.all()), self.json_file_length + 1)

    def test_save(self):
        """
        test_save function docstring

        Test that the save method saves the objects to the JSON file.
        """
        self.json_file_length = len(self.storage.all())
        self.assertEqual(len(self.storage.all()), self.json_file_length)
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        self.assertTrue(os.path.exists("file.json"))
        self.assertEqual(len(self.storage.all()), self.json_file_length + 1)

        model_place = Place()
        self.storage.new(model_place)
        self.storage.save()
        self.assertTrue(os.path.exists("file.json"))
        self.assertEqual(len(self.storage.all()), self.json_file_length + 2)

    def test_reload(self):
        """
        test_reload function docstring

        Test that the reload method loads the objects from the JSON file.
        """
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        self.storage.reload()
        key = "{}.{}".format(model.__class__.__name__, model.id)
        self.assertIn(key, self.storage.all().keys())


if __name__ == "__main__":
    unittest.main()
