#!/usr/bin/python3

from BaseModel import BaseModel

class User(BaseModel):
    """User data for the Air BnB Clone"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""


