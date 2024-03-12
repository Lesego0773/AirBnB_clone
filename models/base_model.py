#!/usr/bin/python3
import uuid
import datetime as dt

class BaseModel():

    def __init__(self, create_at=None, update_at=None, id=None) -> None:
        self.id = id if id else str(uuid.uuid4())
        self.create_at = create_at if create_at else dt.datetime.now()
        self.update_at = update_at if update_at else dt.datetime.now()

    def __str__(self) -> str:
        return f"ID: {self.id}, Created at: {self.create_at}, Updated at: {self.update_at}"

    def save(self):
        self.update_at = dt.datetime.now()
        print(f"Object saved. Updated at: {self.update_at}")

    def to_dict(self):
        return {
            'id': self.id,
            'create_at': self.create_at.isoformat(),
            'update_at': self.update_at.isoformat()
        }

# Creating an instance of the BaseModel class
basemodel = BaseModel()

# Converting an object to a dictionary representation
model_dict = basemodel.to_dict()

# Displaying the dictionary representation
print(model_dict)

# Reconstructing the object from the dictionary
recon_model = BaseModel(
    create_at=dt.datetime.fromisoformat(model_dict['create_at']),
    update_at=dt.datetime.fromisoformat(model_dict['update_at']),
    id=model_dict['id']
)

print(recon_model)
print(recon_model.id)
print(recon_model.create_at)
print(recon_model.update_at)

# Saving the object
recon_model.save()

