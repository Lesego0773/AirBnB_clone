#!/usr/bin/python3

import uuid
import datetime as dt

class BaseModel():

    def __init__(self, *args, **kwargs):
        if kwargs:  # Condition to check if kwargs is not empty
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, dt.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = dt.datetime.now()
            self.updated_at = self.created_at  # Initialize updated_at attribute

    def __str__(self) -> str:
        if hasattr(self, 'updated_at'):
            return f"ID: {self.id}, Created at: {self.created_at}, Updated at: {self.updated_at}"
        else:
            return f"ID: {self.id}, Created at: {self.created_at}, Updated at: None"

    def save(self):
        self.updated_at = dt.datetime.now()
        # storage.save() # Calling storage
        print(f"Object saved. Updated at: {self.updated_at}")

    def to_dict(self):
        return {
            'id': self.id,
            'created_at': self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f'),
            'updated_at': self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        }


