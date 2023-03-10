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
from ast import literal_eval


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand Class Docstring

    Defines the entry point of the command interpreter
    """
    __all_models = {"BaseModel": BaseModel, "User": User,
                    "State": State, "Review": Review,
                    "Place": Place, "City": City, "Amenity": Amenity}
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        quit()

    def do_EOF(self, arg):
        """Quit command to exit the program\n"""
        print('')
        return True

    def emptyline(self):
        """an empty line + ENTER shouldn’t execute anything"""
        pass

    def do_create(self, arg):
        """Usage:\n\t create <model_name>"""
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
        """Usage:\n\t show <model_name>"""
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
                            return

            if len(str(arg).split(" ")) == 1:
                cls = str(arg).split(" ")[0]
                if cls not in self.__all_models.keys():
                    print("** class doesn't exist **")
                else:
                    print("** instance id missing **")

        else:
            print("** class name missing **")

    def do_all(self, arg):
        """Usage:\n\t all <model_name>\n\t all"""
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
                            return
        else:
            all_objs = storage.all()
            print([str(val) for obj, val in all_objs.items()])

    def do_destroy(self, arg):
        """Usage:\n\t destroy <model_name> <id>"""
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
        """Usage:\n\t update <model_name> <id> <attr_name> <attr_value>\n"""
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

    def do_BaseModel(self, arg):
        """Usage:
        BaseModel.all() - display all objects of BaseModel
        BaseModel.count() - display the number of objects in BaseModel
        BaseModel.show(<id>) - display objects by id for BaseModel
        BaseModel.destroy(<id>) - delete object by id for BaseModel
        BaseModel.update(<id>, <attribute name>, <attribute value>) - Update
        BaseModel.update(<id>, {<attribute name>:<attribute value>}) - Update
        """
        self.class_actions('BaseModel', arg)

    def do_User(self, arg):
        """Usage:
        User.all() - display all objects of User
        User.count() - display the number of objects in User
        User.show(<id>) - display objects by id for User
        User.destroy(<id>) - delete object by id for User
        User.update(<id>, <attribute name>, <attribute value>) - Update
        User.update(<id>, {<attribute name>:<attribute value>}) - Update
        """
        self.class_actions('User', arg)

    def do_Amenity(self, arg):
        """Usage:
        Amenity.all() - display all objects of Amenity
        Amenity.count() - display the number of objects in Amenity
        Amenity.show(<id>) - display objects by id for Amenity
        Amenity.destroy(<id>) - delete object by id for Amenity
        Amenity.update(<id>, <attribute name>, <attribute value>) - Update
        Amenity.update(<id>, {<attribute name>:<attribute value>}) - Update
        """
        self.class_actions('Amenity', arg)

    def do_Place(self, arg):
        """Usage:
        Place.all() - display all objects of Place
        Place.count() - display the number of objects in Place
        Place.show(<id>) - display objects by id for Place
        Place.destroy(<id>) - delete object by id for Place
        Place.update(<id>, <attribute name>, <attribute value>) - Update
        Place.update(<id>, {<attribute name>:<attribute value>}) - Update
        """
        self.class_actions('Place', arg)

    def do_City(self, arg):
        """Usage:
        City.all() - display all objects of City
        City.count() - display the number of objects in City
        City.show(<id>) - display objects by id for City
        City.destroy(<id>) - delete object by id for City
        City.update(<id>, <attribute name>, <attribute value>) - Update
        City.update(<id>, {<attribute name>:<attribute value>}) - Update
        """
        self.class_actions('City', arg)

    def do_Review(self, arg):
        """Usage:
        Review.all() - display all objects of Review
        Review.count() - display the number of objects in Review
        Review.show(<id>) - display objects by id for Review
        Review.destroy(<id>) - delete object by id for Review
        Review.update(<id>, <attribute name>, <attribute value>) - Update
        Review.update(<id>, {<attribute name>:<attribute value>}) - Update
        """
        self.class_actions('Review', arg)

    def do_State(self, arg):
        """Usage:
        State.all() - display all objects of State
        State.count() - display the number of objects in State
        State.show(<id>) - display objects by id for State
        State.destroy(<id>) - delete object by id for State
        State.update(<id>, <attribute name>, <attribute value>) - Update
        State.update(<id>, {<attribute name>:<attribute value>}) - Update
        """
        self.class_actions('State', arg)

    def class_actions(self, cls, arg):
        """Retrieve all instances of a class by using: <class name>.action()"""
        if arg[:6] == ".all()":
            self.do_all(cls)
        if arg[:8] == ".count()":
            all_objs = storage.all()
            obj = {}
            for obj_id, obj_val in all_objs.items():
                if cls == obj_id.split(".")[0]:
                    obj[obj_id] = obj_val
            print(len(obj))
        if arg[:6] == ".show(":
            self.do_show(cls + ' ' + arg[6:-1])

        if arg[:9] == ".destroy(":
            self.do_destroy(cls + ' ' + arg[9:-1])

        if arg[:8] == ".update(":
            if "{" in arg and "}" in arg:
                arg1 = arg[8:-1].split("{")
                arg1[1] = "{" + arg1[1]
            else:
                arg1 = arg[8:-1].split(", ")
            if len(arg1) == 3:
                arg1 = " ".join(arg1).replace("\"", "").replace("  ", " ")
                self.do_update(cls + " " + arg1)
            if len(arg1) == 2:
                try:
                    my_dict = literal_eval(arg1[1])
                except Exception:
                    return
                for i, j in my_dict.items():
                    self.do_update(cls + " " +
                                   arg1[0][0:-2] + " " +
                                   str(i) + " " + str(j))
            else:
                return
        else:
            print("Not a valid command")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
