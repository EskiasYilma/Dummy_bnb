#!/usr/bin/python3
"""
Unittest for Console
"""
from contextlib import contextmanager
from io import StringIO
import unittest
from unittest.mock import patch
from datetime import datetime
from console import HBNBCommand
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage


class TestConsole(unittest.TestCase):
    """
    Test cases for the Console class

    Tests all methods and errors for HBNBCommand class
    """

    def setUp(self):
        """
        setUp function docstring

        Setting up the test environment
        """
        self.console = HBNBCommand()
        self.mock_stdout = StringIO()

    def test_do_quit(self):
        """test_do_quit Docstring"""
        with self.assertRaises(SystemExit):
            self.console.do_quit(self.console)

    def test_do_EOF(self):
        """test_do_EOF Docstring"""
        with patch("sys.stdout", self.mock_stdout):
            self.assertTrue(self.console.do_EOF(""))

    def test_emptyline(self):
        """test_emptyline Docstring"""
        with patch("sys.stdout", self.mock_stdout):
            self.assertIsNone(self.console.emptyline())

    def test_do_create_error(self):
        """test_do_create_error Docstring"""
        with patch("sys.stdout", self.mock_stdout):
            self.console.do_create("")
            self.assertEqual("** class name missing **\n",
                             self.mock_stdout.getvalue())

    def test_do_create(self):
        """test_do_create Docstring"""
        with patch("sys.stdout", self.mock_stdout):
            self.console.do_create("BaseModel")
            all_objs = storage.all()
            self.assertTrue(all_objs)
            self.assertTrue("BaseModel." +
                            list(all_objs.values())[0].id in all_objs.keys())

    def test_do_show_instance_not_found(self):
        """test_do_show_instance_not_found Docstring"""
        with patch("sys.stdout", self.mock_stdout):
            self.console.do_show("BaseModel 1234")
            self.assertEqual("** no instance found **\n",
                             self.mock_stdout.getvalue())

    def test_do_show_no_class(self):
        """test_do_show_no_class Docstring"""
        with patch("sys.stdout", self.mock_stdout):
            self.console.do_show("")
            self.assertEqual("** class name missing **\n",
                             self.mock_stdout.getvalue())

    def test_do_show_id_missing(self):
        """test_do_show_id_missing Docstring"""
        with patch("sys.stdout", self.mock_stdout):
            self.console.do_show("BaseModel")
            self.assertEqual("** instance id missing **\n",
                             self.mock_stdout.getvalue())

    def test_do_show_class_doesnt_exist(self):
        """test_do_show_class_doesnt_exist Docstring"""
        with patch("sys.stdout", self.mock_stdout):
            self.console.do_show("JustModel")
            self.assertEqual("** class doesn't exist **\n",
                             self.mock_stdout.getvalue())

    def test_do_show_correct(self):
        """test_do_show_correct Docstring"""
        with patch("sys.stdout", self.mock_stdout):
            self.console.do_create("BaseModel")
            all_objs = storage.all()
            obj_id = list(all_objs.values())[0].id
            self.console.do_show("BaseModel " + obj_id)
            self.assertIn(str(all_objs["BaseModel." + obj_id]),
                          self.mock_stdout.getvalue())

    def test_do_all(self):
        """test_do_all Docstring"""
        with patch("sys.stdout", self.mock_stdout):
            self.console.do_all("")
            self.assertEqual("[]\n",
                             self.mock_stdout.getvalue())

        with patch("sys.stdout", self.mock_stdout):
            self.console.do_create("BaseModel")
            self.console.do_all("BaseModel")
            self.assertIn(str(list(storage.all().values())[0]),
                          self.mock_stdout.getvalue())

    def test_all_error_class_doesnt_exist(self):
        """test_all_error_class_doesnt_exist Docstring"""
        with patch("sys.stdout", self.mock_stdout):
            self.console.do_all("C")
        self.assertEqual(self.mock_stdout.getvalue().strip(),
                         "** class doesn't exist **")

    def test_do_destroy_correct(self):
        """test_do_destroy_correct Docstring"""
        with patch("sys.stdout", self.mock_stdout):
            self.console.do_create("BaseModel")
            all_objs = storage.all()
            obj_id = list(all_objs.values())[0].id
            self.console.do_destroy("BaseModel " + obj_id)
            self.assertTrue("BaseModel." + obj_id not in storage.all().keys())

    def test_destroy_error_class_doesnt_exist(self):
        """test_destroy_error_class_doesnt_exist Docstring"""
        with patch("sys.stdout", self.mock_stdout):
            self.console.do_destroy("d3da85f2-499c-43cb-b33d-3d7935bc808c")
        self.assertEqual(self.mock_stdout.getvalue().strip(),
                         "** class doesn't exist **")

    def test_destroy_error_class_missing(self):
        """test_destroy_error_class_missing Docstring"""
        with patch("sys.stdout", self.mock_stdout):
            self.console.do_destroy("")
        self.assertEqual(self.mock_stdout.getvalue().strip(),
                         "** class name missing **")

    def test_destroy_error_no_instance_found(self):
        """test_destroy_error_no_instance_found Docstring"""
        with patch("sys.stdout", self.mock_stdout):
            self.console.do_destroy("BaseModel 1234")
        self.assertEqual(self.mock_stdout.getvalue().strip(),
                         "** no instance found **")

    def test_destroy_error_id_instance_misssing(self):
        """test_destroy_error_id_instance_misssing Docstring"""
        with patch("sys.stdout", self.mock_stdout):
            self.console.do_destroy("BaseModel")
        self.assertEqual(self.mock_stdout.getvalue().strip(),
                         "** instance id missing **")

    def test_do_update_error(self):
        """test_do_update_error Docstring"""
        with patch("sys.stdout", self.mock_stdout):
            self.console.do_update("BaseModel 1234")
            self.assertEqual("** no instance found **\n",
                             self.mock_stdout.getvalue())

    def test_update_error_class_doesnt_exist(self):
        """test_update_error_class_doesnt_exist Docstring"""
        with patch("sys.stdout", self.mock_stdout):
            self.console.do_update("TEst")
        self.assertEqual(self.mock_stdout.getvalue().strip(),
                         "** class doesn't exist **")

    def test_update_error_class_missing(self):
        """test_update_error_class_missing Docstring"""
        with patch("sys.stdout", self.mock_stdout):
            self.console.do_update("")
        self.assertEqual(self.mock_stdout.getvalue().strip(),
                         "** class name missing **")

    def test_update_error_no_instance_found(self):
        """test_update_error_no_instance_found Docstring"""
        with patch("sys.stdout", self.mock_stdout):
            self.console.do_update("BaseModel 1234")
        self.assertEqual(self.mock_stdout.getvalue().strip(),
                         "** no instance found **")

    def test_update_error_id_instance_misssing(self):
        """test_update_error_id_instance_misssing Docstring"""
        with patch("sys.stdout", self.mock_stdout):
            self.console.do_update("BaseModel")
        self.assertEqual(self.mock_stdout.getvalue().strip(),
                         "** instance id missing **")

    def test_do_update_attr_missing(self):
        """test_do_update_attr_missing Docstring"""
        with patch("sys.stdout", self.mock_stdout):
            self.console.do_create("User")
            all_objs = storage.all()
            obj_id = list(all_objs.values())[0].id
            self.console.do_update("User " + obj_id)
        self.assertEqual(self.mock_stdout.getvalue().strip().split("\n")[1],
                         "** attribute name missing **")

    def test_do_update_attr_value_missing(self):
        """test_do_update_attr_value_missing Docstring"""
        with patch("sys.stdout", self.mock_stdout):
            self.console.do_create("User")
            all_objs = storage.all()
            obj_id = list(all_objs.values())[0].id
            self.console.do_update("User " + obj_id + " first_name")
        self.assertEqual(self.mock_stdout.getvalue().strip().split("\n")[1],
                         "** value missing **")

    def test_do_update_correct(self):
        """test_do_update_correct Docstring"""
        with patch("sys.stdout", self.mock_stdout):
            self.console.do_create("BaseModel")
            all_objs = storage.all()
            obj_id = list(all_objs.values())[0].id
            self.console.do_update("BaseModel " + obj_id + " name 'test'")
            self.assertTrue("test" in getattr(list(storage.all().values())[0],
                            "name"))


if __name__ == "__main__":
    unittest.main()
