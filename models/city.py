#!/usr/bin/python3
"""
City Model Docstring
Inherites from BaseModel

"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    City Class Docstring

    Public class attributes:

        state_id: string - empty string: it will be the State.id
        name: string - empty string

    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """
        init Function Docstring

        Initialize parent class (BaseModel)

        """
        super().__init__(*args, **kwargs)
