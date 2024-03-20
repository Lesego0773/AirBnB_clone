#!/usr/bin/python3
from BaseModel import BaseModel

class City(BaseModel):
    """City class that inherits from BaseModel"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.name = ""
        self.state_id = ""
