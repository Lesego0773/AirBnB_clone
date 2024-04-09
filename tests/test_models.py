import unittest

from tests.test_models import BaseModel, User, State, Review, Place, City, Amenity, FileStorage


class TestModels(unittest.TestCase):
    def test_user_instance(self):
        user = User()
        self.assertIsInstance(user, BaseModel)
        self.assertIsInstance(user, User)

    def test_state_instance(self):
        state = State()
        self.assertIsInstance(state, BaseModel)
        self.assertIsInstance(state, State)

    def test_review_instance(self):
        review = Review()
        self.assertIsInstance(review, BaseModel)
        self.assertIsInstance(review, Review)

    def test_place_instance(self):
        place = Place()
        self.assertIsInstance(place, BaseModel)
        self.assertIsInstance(place, Place)

    def test_city_instance(self):
        city = City()
        self.assertIsInstance(city, BaseModel)
        self.assertIsInstance(city, City)

    def test_amenity_instance(self):
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)
        self.assertIsInstance(amenity, Amenity)

class TestStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage("test_storage.json")

    def test_save_load(self):
        data = {'test_key': 'test_value'}
        self.storage.save(data)
        loaded_data = self.storage.load()
        self.assertEqual(data, loaded_data)

if __name__ == '__main__':
    unittest.main()

