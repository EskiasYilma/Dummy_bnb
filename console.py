#!/usr/bin/python3
"""
Console Module Docstring

Defines the entry point of the command interpreter
"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.review import Review
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.engine.file_storage import FileStorage
from models import storage
from datetime import datetime

class HBNBCommand(cmd.Cmd):
	"""
	HBNBCommand Class Docstring

	Defines the entry point of the command interpreter
	"""
	__all_models = {"BaseModel": BaseModel, "User":User, "State":State, "Review":Review, "Place":Place, "City":City, "Amenity":Amenity}
	prompt = "(hbnb) "

	def do_quit(self, arg):
		"""Quit command to exit the program\n"""
		return True

	def do_EOF(self, arg):
		"""Quit command to exit the program\n"""
		return True

	def emptyline(self):
		"""an empty line + ENTER shouldn’t execute anything"""
		pass

	def do_create(self, arg):
		"""Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id.\nUsage:\n\tcreate <model_name>
		"""
		# self.__all_models = {"BaseModel": BaseModel}

		if arg:
			if str(arg) in self.__all_models.keys():
				model = self.__all_models[arg]()
				model.save()
				print(model.id)
			else:
				print("** class doesn't exist **")
		else:
			print("** class name missing **")

	def do_show(self, arg):
		"""Prints the string representation of an instance based on the class name and id. Ex: $ show BaseModel
		"""
		if arg:
			if len(str(arg).split(" ")) == 2:
				cls, id = str(arg).split(" ")
				if cls not in self.__all_models.keys():
					print("** class doesn't exist **")
				if id not in [y.id for x, y in storage.all().items()]:
					print("** no instance found **")
				else:
					all_objs = storage.all()
					for obj_id, obj_val in all_objs.items():
						if str(id) == str(obj_val.id):
							obj = all_objs[obj_id]
							print(obj)

			if len(str(arg).split(" ")) == 1:
				cls = str(arg).split(" ")[0]
				if cls not in self.__all_models.keys():
					print("** class doesn't exist **")
				else:
					print("** instance id missing **")

		else:
			print("** class name missing **")

	def do_all(self, arg):
		"""Prints all string representation of all instances based or not on the class name\n\nUsage: all <model_name>\n       all\n"""
		if arg:
			if len(str(arg).split(" ")) > 1:
				return
			if len(str(arg).split(" ")) == 1:
				cls = str(arg).split(" ")[0]
				if cls not in self.__all_models.keys():
					print("** class doesn't exist **")
				else:
					all_objs = storage.all()
					for obj_id in all_objs.keys():
						if cls == obj_id.split(".")[0]:
							obj = all_objs[obj_id]
							print(obj)
		else:
			all_objs = storage.all()
			print([str(val) for obj, val in all_objs.items()])

	def do_destroy(self, arg):
		"""Deletes an instance based on the class name and id (save the change into the JSON file\n\nUsage: destroy <model_name> <id>"""
		if arg:
			if len(str(arg).split(" ")) == 2:
				cls, id = str(arg).split(" ")
				if cls not in self.__all_models.keys():
					print("** class doesn't exist **")
				if id not in [y.id for x, y in storage.all().items()]:
					print("** no instance found **")
				else:
					all_objs = storage.all()
					for obj_id, obj_val in all_objs.items():
						if str(id) == str(obj_val.id):
							all_objs.pop(obj_id)
							break
					storage.save()
					storage.reload()

			if len(str(arg).split(" ")) == 1:
				cls = str(arg).split(" ")[0]
				if cls not in self.__all_models.keys():
					print("** class doesn't exist **")
				else:
					print("** instance id missing **")
		else:
			print("** class name missing **")

	def do_update(self, arg):
		"""Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file"""
		if arg:
			if len(str(arg).split(" ")) == 4:
				cls, id, attr_nm, attr_val = str(arg).split(" ")
				if cls not in self.__all_models.keys():
					print("** class doesn't exist **")
				if id not in [y.id for x, y in storage.all().items()]:
					print("** no instance found **")
					return
				else:
					all_objs = storage.all()
					for obj_id, obj_val in all_objs.items():
						if str(id) == str(obj_val.id):
							setattr(obj_val, attr_nm, attr_val)
							setattr(obj_val, "updated_at", datetime.now())
							storage.save()
							return

			if len(str(arg).split(" ")) == 3:
				cls, id, attr_nm = str(arg).split(" ")
				if cls not in self.__all_models.keys():
					print("** class doesn't exist **")
				if id not in [y.id for x, y in storage.all().items()]:
					print("** no instance found **")
				else:
					print("** value missing **")

			if len(str(arg).split(" ")) == 2:
				cls, id = str(arg).split(" ")
				if cls not in self.__all_models.keys():
					print("** class doesn't exist **")
				if id not in [y.id for x, y in storage.all().items()]:
					print("** no instance found **")
				else:
					print("** attribute name missing **")

			if len(str(arg).split(" ")) == 1:
				cls = str(arg).split(" ")[0]
				if cls not in self.__all_models.keys():
					print("** class doesn't exist **")
				else:
					print("** instance id missing **")
		else:
			print("** class name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
