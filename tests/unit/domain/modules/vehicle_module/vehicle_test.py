import json
from unittest import TestCase

from src.domain.modules.customer_module.customer import Customer
from src.domain.modules.vehicle_module.brand import Brand
from src.domain.modules.vehicle_module.model import Model
from src.domain.modules.vehicle_module.vehicle import Vehicle


class VehicleTest(TestCase):
    def setUp(self):
        self.owner = Customer('76244717104', 'Antonio Azevedo', 'tony@test.com')
        self.brand = Brand('Honda')
        self.model = Model('Civic EXR 2.0', self.brand)
        self.vehicle = Vehicle('ABC1234', self.owner, self.model, 2016)
        self.vehicle_with_id = Vehicle('ABC1234', self.owner, self.model, 2016, 'b07e1d28b7cf45deb63ff5f19e764f90')
        self.vehicle_id = self.vehicle._id

    def test_create_vehicle(self):
        self.assertIsNotNone(self.vehicle._id)
        self.assertEqual(len(self.vehicle._id), 32)
        self.assertEqual(self.vehicle.plate, 'ABC1234')
        self.assertEqual(self.vehicle.owner.name, 'Antonio Azevedo')
        self.assertEqual(self.vehicle.model.name, 'Civic EXR 2.0')
        self.assertEqual(self.vehicle.model.brand.name, 'Honda')
        self.assertEqual(self.vehicle.model_year, 2016)

    def test_create_vehicle_with_id(self):
        self.assertEqual(self.vehicle_with_id._id, 'b07e1d28b7cf45deb63ff5f19e764f90')
        self.assertEqual(self.vehicle_with_id.plate, 'ABC1234')
        self.assertEqual(self.vehicle_with_id.owner.name, 'Antonio Azevedo')
        self.assertEqual(self.vehicle_with_id.model.name, 'Civic EXR 2.0')
        self.assertEqual(self.vehicle_with_id.model.brand.name, 'Honda')
        self.assertEqual(self.vehicle_with_id.model_year, 2016)

    def test_vehicle_as_json(self):
        expected = json.dumps({
            "plate": "ABC1234",
            "owner": {
                "doc_id": "76244717104",
                "name": "Antonio Azevedo",
                "email": "tony@test.com",
                "_id": self.owner._id
            },
            "model": {
                "name": "Civic EXR 2.0",
                "brand": {
                    "name": "Honda",
                    "_id": self.brand._id
                },
                "_id": self.model._id
            },
            "model_year": 2016,
            "_id": self.vehicle._id
        })

        self.assertEqual(self.vehicle.as_json(), expected)

    def test_vehicle_as_json_with_id(self):
        expected = json.dumps({
            "plate": "ABC1234",
            "owner": {
                "doc_id": "76244717104",
                "name": "Antonio Azevedo",
                "email": "tony@test.com",
                "_id": self.owner._id
            },
            "model": {
                "name": "Civic EXR 2.0",
                "brand": {
                    "name": "Honda",
                    "_id": self.brand._id
                },
                "_id": self.model._id
            },
            "model_year": 2016,
            "_id": "b07e1d28b7cf45deb63ff5f19e764f90"
        })

        self.assertEqual(self.vehicle_with_id.as_json(), expected)
