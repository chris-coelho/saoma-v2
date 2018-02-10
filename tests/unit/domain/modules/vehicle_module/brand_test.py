import json
from unittest import TestCase

from src.domain.modules.vehicle_module.brand import Brand


class BrandTest(TestCase):
    def setUp(self):
        self.brand = Brand('Honda')
        self.brand_with_id = Brand('Ford', 'b07e1d28b7cf45deb63ff5f19e764f90')
        self.brand_id = self.brand._id

    def test_create_brand(self):
        self.assertIsNotNone(self.brand._id)
        self.assertEqual(len(self.brand._id), 32)
        self.assertEqual(self.brand.name, 'Honda')

    def test_create_brand_with_id(self):
        self.assertEqual(self.brand_with_id._id, 'b07e1d28b7cf45deb63ff5f19e764f90')
        self.assertEqual(self.brand_with_id.name, 'Ford')

    def test_brand_as_json(self):
        expected = json.dumps({
            "name": "Honda",
            "_id": self.brand_id
        })

        self.assertEqual(self.brand.as_json(), expected)

    def test_brand_as_json_with_id(self):
        expected = json.dumps({
            "name": "Ford",
            "_id": "b07e1d28b7cf45deb63ff5f19e764f90"
        })

        self.assertEqual(self.brand_with_id.as_json(), expected)
