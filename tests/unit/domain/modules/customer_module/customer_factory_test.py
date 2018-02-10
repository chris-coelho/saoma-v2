from unittest import TestCase

from src.domain.modules.customer_module.customer import Customer
from src.domain.modules.customer_module.customer_exceptions import CustomerExceptions
from src.domain.modules.customer_module.customer_factory import CustomerFactory


class CustomerFactoryTest(TestCase):
    def setUp(self):
        self.customer = CustomerFactory.create('72638185400', 'Jose da Silva', 'jose.silva@test.com')
        self.customer_with_id = CustomerFactory.create('72638185400', 'Jose da Silva', 'jose.silva@test.com',
                                                       'b07e1d28b7cf45deb63ff5f19e764f90')
        self.json = {
            "doc_id": "72638185400",
            "name": "Jose da Silva",
            "email": "jose.silva@test.com",
            "_id": "b07e1d28b7cf45deb63ff5f19e764f90"
        }

    def test_create(self):
        self.assertEqual(self.customer.doc_id, '72638185400')
        self.assertEqual(self.customer.name, 'Jose da Silva')
        self.assertEqual(self.customer.email, 'jose.silva@test.com')

        self.assertEqual(self.customer_with_id.doc_id, '72638185400')
        self.assertEqual(self.customer_with_id.name, 'Jose da Silva')
        self.assertEqual(self.customer_with_id.email, 'jose.silva@test.com')
        self.assertEqual(self.customer_with_id._id, 'b07e1d28b7cf45deb63ff5f19e764f90')

    def test_create_from_db(self):
        customer = CustomerFactory.create_from_db(self.json)
        self.assertIsInstance(customer, Customer)
        self.assertEqual(customer._id, self.customer_with_id._id)

    def test_create_invalid_doc_id(self):
        with self.assertRaises(CustomerExceptions) as e:
            CustomerFactory.create(None, 'Jose da Silva', 'jose.silva@test.com')
            e.msg = "required doc_id - expected: None"

        with self.assertRaises(CustomerExceptions) as e:
            CustomerFactory.create('', 'Jose da Silva', 'jose.silva@test.com')
            e.msg = "required doc_id expected: ''"

        with self.assertRaises(CustomerExceptions) as e:
            CustomerFactory.create('12345678900', 'Jose da Silva', 'jose.silva@test.com')
            e.msg = "invalid doc_id - expected: invalid number"

    def test_create_invalid_name(self):
        with self.assertRaises(CustomerExceptions) as e:
            CustomerFactory.create('72638185400', None, 'jose.silva@test.com')
            e.msg = "invalid name - expected: None"

        with self.assertRaises(CustomerExceptions) as e:
            CustomerFactory.create('72638185400', '', 'jose.silva@test.com')
            e.msg = "invalid name - expected: ''"

        with self.assertRaises(CustomerExceptions) as e:
            CustomerFactory.create('72638185400', 'short', 'jose.silva@test.com')
            e.msg = "invalid name - expected: a short name"

    def test_create_invalid_email(self):
        with self.assertRaises(CustomerExceptions) as e:
            CustomerFactory.create('72638185400', 'Jose da Silva', None)
            e.msg = "invalid email - expected: None"

        with self.assertRaises(CustomerExceptions) as e:
            CustomerFactory.create('72638185400', 'Jose da Silva', '')
            e.msg = "invalid email - expected: ''"

        with self.assertRaises(CustomerExceptions) as e:
            CustomerFactory.create('72638185400', 'Jose da Silva', 'jose.silvatest.com')
            e.msg = "invalid email - expected: email with no at"
