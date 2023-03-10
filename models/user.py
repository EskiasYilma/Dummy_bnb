#!/usr/bin/python3
"""
User Model Docstring
Inherites from BaseModel

"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    User Class Docstring

    Public class attributes:

        email: string - empty string
        password: string - empty string
        first_name: string - empty string
        last_name: string - empty string

    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        init Function Docstring

        Initialize parent class (BaseModel)

        """
        super().__init__(*args, **kwargs)
