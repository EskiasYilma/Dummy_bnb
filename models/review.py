#!/usr/bin/python3
"""
Review Model Docstring
Inherites from BaseModel

"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review Class Docstring

    Public class attributes:

        place_id: string - empty string
        user_id: string - empty string
        text: string - empty string
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """
        init Function Docstring

        Initialize parent class (BaseModel)

        """
        super().__init__(*args, **kwargs)
