#!/usr/bin/python3
"""
Module Docstring
"""
from models import storage
from models.base_model import BaseModel
import random

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
my_model = BaseModel()
x = random.randint(1, 98)
my_model.name = "Model_{}".format(x)
my_model.my_number = x
my_model.save()
print(my_model)
