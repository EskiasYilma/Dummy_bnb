#!/usr/bin/python3
"""
Amenity Model Docstring
Inherites from BaseModel

"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity Class Docstring

    Public class attributes:

        name: string - empty string

    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        init Function Docstring

        Initialize parent class (BaseModel)

        """
        super().__init__(*args, **kwargs)
