#!/usr/bin/python3
from BaseModel import BaseModel

class Review(BaseModel):
    """Review class for the user that inherits from Basemodel"""

    def __init__(self, *args, **kwargs):
        """Initializing the review instant"""
        super().__init__(*args, **kwargs)

        self.place_identity = ""
        self.user_identity = ""
        self.text = ""
