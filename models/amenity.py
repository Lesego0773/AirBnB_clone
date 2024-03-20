#!/usr/bin/python3
from BaseModel import BaseModel

class Amenity(BaseModel):
    """Amenity class that inherits from BaseModel"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.name = ""
