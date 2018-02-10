import json
from unittest import TestCase

from src.domain.modules.customer_module.customer import Customer


class CustomerTest(TestCase):
    def setUp(self):
        self.customer = Customer('72638185400', 'Jose da Silva', 'jose.silva@test.com')
        self.customer_with_id = Customer('72638185400', 'Jose da Silva', 'jose.silva@test.com',
                                         'b07e1d28b7cf45deb63ff5f19e764f90')
        self.customer_id = self.customer._id

    def test_create_customer(self):
        self.assertIsNotNone(self.customer._id)
        self.assertEqual(len(self.customer._id), 32)
        self.assertEqual(self.customer.doc_id, '72638185400')
        self.assertEqual(self.customer.name, 'Jose da Silva')
        self.assertEqual(self.customer.email, 'jose.silva@test.com')

    def test_create_customer_with_id(self):
        self.assertEqual(self.customer_with_id._id, 'b07e1d28b7cf45deb63ff5f19e764f90')
        self.assertEqual(self.customer_with_id.doc_id, '72638185400')
        self.assertEqual(self.customer_with_id.name, 'Jose da Silva')
        self.assertEqual(self.customer_with_id.email, 'jose.silva@test.com')

    def test_customer_as_json(self):
        expected = json.dumps({
            "doc_id": "72638185400",
            "name": "Jose da Silva",
            "email": "jose.silva@test.com",
            "_id": self.customer_id
        })

        self.assertEqual(self.customer.as_json(), expected)

    def test_customer_as_json_with_id(self):
        expected = json.dumps({
            "doc_id": "72638185400",
            "name": "Jose da Silva",
            "email": "jose.silva@test.com",
            "_id": "b07e1d28b7cf45deb63ff5f19e764f90"
        })

        self.assertEqual(self.customer_with_id.as_json(), expected)
