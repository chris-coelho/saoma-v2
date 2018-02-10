import json
from unittest import TestCase

from src.domain.modules.vehicle_module.brand import Brand
from src.domain.modules.vehicle_module.model import Model


class ModelTest(TestCase):
    def setUp(self):
        self.brand = Brand('Honda')
        self.model = Model('Civic EXR 2.0', self.brand)
        self.model_with_id = Model('Civic EXR 2.0', self.brand, 'b07e1d28b7cf45deb63ff5f19e764f90')
        self.model_id = self.model._id

    def test_create_model(self):
        self.assertIsNotNone(self.model._id)
        self.assertEqual(len(self.model._id), 32)
        self.assertEqual(self.model.name, 'Civic EXR 2.0')
        self.assertEqual(self.model.brand.name, 'Honda')

    def test_create_model_with_id(self):
        self.assertEqual(self.model_with_id._id, 'b07e1d28b7cf45deb63ff5f19e764f90')
        self.assertEqual(self.model_with_id.name, 'Civic EXR 2.0')
        self.assertEqual(self.model_with_id.brand.name, 'Honda')

    def test_model_as_json(self):
        expected = json.dumps({
            "name": "Civic EXR 2.0",
            "brand": {
                "name": "Honda",
                "_id": self.brand._id
            },
            "_id": self.model_id
        })

        self.assertEqual(self.model.as_json(), expected)

    def test_model_as_json_with_id(self):
        expected = json.dumps({
            "name": "Civic EXR 2.0",
            "brand": {
                "name": "Honda",
                "_id": self.brand._id
        },
            "_id": "b07e1d28b7cf45deb63ff5f19e764f90"
        })

        self.assertEqual(self.model_with_id.as_json(), expected)
