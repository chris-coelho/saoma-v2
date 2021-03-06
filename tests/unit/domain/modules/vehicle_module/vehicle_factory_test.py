from unittest import TestCase

import datetime

from src.domain.modules.customer_module.customer import Customer
from src.domain.modules.vehicle_module.brand import Brand
from src.domain.modules.vehicle_module.model import Model
from src.domain.modules.vehicle_module.vehicle import Vehicle
from src.domain.modules.vehicle_module.vehicle_exceptions import VehicleExceptions
from src.domain.modules.vehicle_module.vehicle_factory import VehicleFactory


class VehicleFactoryTest(TestCase):
    def setUp(self):
        self.vehicle = VehicleFactory.create('ABC1234',
                                             Customer('58355843690', 'Marcia Garcia', 'marcia.garcia@test.com',
                                                      '76e67f3c40024dfd94bdb71976022839'),
                                             Model('HRV EX 1.8', Brand('Honda',
                                                                       'e29ed583b9a246a8a7f1596593bb7888'),
                                                   'b49aa1cb2082476bb3b6af601ec3ef9b'),
                                             2018)
        self.vehicle_with_id = VehicleFactory.create('ABC1234',
                                                     Customer('58355843690', 'Marcia Garcia', 'marcia.garcia@test.com',
                                                              '76e67f3c40024dfd94bdb71976022839'),
                                                     Model('HRV EX 1.8', Brand('Honda',
                                                                               'e29ed583b9a246a8a7f1596593bb7888'),
                                                           'b49aa1cb2082476bb3b6af601ec3ef9b'),
                                                     2018, '9fd11778695b44368fd03258cbcc7b17')
        self.json = {
            "plate": "ABC1234",
            "owner": {
                "doc_id": "58355843690",
                "name": "Marcia Garcia",
                "email": "marcia.garcia@test.com",
                "_id": "76e67f3c40024dfd94bdb71976022839"
            },
            "model": {
                "name": "HRV EX 1.8",
                "brand": {
                    "name": "Honda",
                    "_id": "e29ed583b9a246a8a7f1596593bb7888"
                },
                "_id": "b49aa1cb2082476bb3b6af601ec3ef9b"
            },
            "model_year": 2018,
            "_id": "9fd11778695b44368fd03258cbcc7b17"
        }

    def test_create(self):
        self.assertEqual(self.vehicle.plate, 'ABC1234')
        self.assertEqual(self.vehicle.owner.name, 'Marcia Garcia')
        self.assertEqual(self.vehicle.model.name, 'HRV EX 1.8')
        self.assertEqual(self.vehicle.model.brand.name, 'Honda')
        self.assertEqual(self.vehicle.model_year, 2018)

        self.assertEqual(self.vehicle_with_id.plate, 'ABC1234')
        self.assertEqual(self.vehicle_with_id.owner.name, 'Marcia Garcia')
        self.assertEqual(self.vehicle_with_id.model.name, 'HRV EX 1.8')
        self.assertEqual(self.vehicle_with_id.model.brand.name, 'Honda')
        self.assertEqual(self.vehicle_with_id.model_year, 2018)
        self.assertEqual(self.vehicle_with_id._id, '9fd11778695b44368fd03258cbcc7b17')

        self.assertIsInstance(self.vehicle.owner, Customer)
        self.assertIsInstance(self.vehicle.model, Model)
        self.assertIsInstance(self.vehicle.model.brand, Brand)

    def test_create_from_db(self):
        vehicle = VehicleFactory.create_from_db(self.json)
        self.assertIsInstance(vehicle, Vehicle)
        self.assertEqual(vehicle._id, self.vehicle_with_id._id)

    def test_create_invalid_plate(self):
        with self.assertRaises(VehicleExceptions) as e:
            VehicleFactory.create(None,
                                  Customer('58355843690', 'Marcia Garcia', 'marcia.garcia@test.com',
                                           '76e67f3c40024dfd94bdb71976022839'),
                                  Model('HRV EX 1.8', Brand('Honda',
                                                            'e29ed583b9a246a8a7f1596593bb7888'),
                                        'b49aa1cb2082476bb3b6af601ec3ef9b'),
                                  2018)
            e.msg = "invalid plate - expected: None"

        with self.assertRaises(VehicleExceptions) as e:
            VehicleFactory.create('AAB14',
                                  Customer('58355843690', 'Marcia Garcia', 'marcia.garcia@test.com',
                                           '76e67f3c40024dfd94bdb71976022839'),
                                  Model('HRV EX 1.8', Brand('Honda',
                                                            'e29ed583b9a246a8a7f1596593bb7888'),
                                        'b49aa1cb2082476bb3b6af601ec3ef9b'),
                                  2018)
            e.msg = "invalid plate - expected: a short plate"

        with self.assertRaises(VehicleExceptions) as e:
            VehicleFactory.create('AB234',
                                  Customer('58355843690', 'Marcia Garcia', 'marcia.garcia@test.com',
                                           '76e67f3c40024dfd94bdb71976022839'),
                                  Model('HRV EX 1.8', Brand('Honda',
                                                            'e29ed583b9a246a8a7f1596593bb7888'),
                                        'b49aa1cb2082476bb3b6af601ec3ef9b'),
                                  2018)
            e.msg = "invalid plate - expected: a plate that no matching with format AAA1111 - 3 letters and 4 numbers"

    def test_create_invalid_model(self):
        with self.assertRaises(VehicleExceptions) as e:
            VehicleFactory.create('ABC1234',
                                  Customer('58355843690', 'Marcia Garcia', 'marcia.garcia@test.com',
                                           '76e67f3c40024dfd94bdb71976022839'),
                                  None,
                                  2018)
            e.msg = "invalid model - expected: None"

    def test_create_valid_model_year(self):
        vehicle_year_none = VehicleFactory.create('ABC1234',
                                                  Customer('58355843690', 'Marcia Garcia', 'marcia.garcia@test.com',
                                                           '76e67f3c40024dfd94bdb71976022839'),
                                                  Model('HRV EX 1.8', Brand('Honda',
                                                                            'e29ed583b9a246a8a7f1596593bb7888'),
                                                        'b49aa1cb2082476bb3b6af601ec3ef9b'),
                                                  None)
        vehicle_next_year = VehicleFactory.create('ABC1234',
                                                  Customer('58355843690', 'Marcia Garcia', 'marcia.garcia@test.com',
                                                           '76e67f3c40024dfd94bdb71976022839'),
                                                  Model('HRV EX 1.8', Brand('Honda',
                                                                            'e29ed583b9a246a8a7f1596593bb7888'),
                                                        'b49aa1cb2082476bb3b6af601ec3ef9b'),
                                                  datetime.date.today().year + 1)
        vehicle_old = VehicleFactory.create('ABC1234',
                                            Customer('58355843690', 'Marcia Garcia', 'marcia.garcia@test.com',
                                                     '76e67f3c40024dfd94bdb71976022839'),
                                            Model('HRV EX 1.8', Brand('Honda', 'e29ed583b9a246a8a7f1596593bb7888'),
                                                  'b49aa1cb2082476bb3b6af601ec3ef9b'),
                                            datetime.date.today().year - 5)  # 5 years old
        self.assertIsInstance(vehicle_year_none, Vehicle)
        self.assertIsInstance(vehicle_next_year, Vehicle)
        self.assertIsInstance(vehicle_old, Vehicle)

    def test_create_model_year_greater_than_limit(self):
        with self.assertRaises(VehicleExceptions) as e:
            VehicleFactory.create('ABC1234',
                                  Customer('58355843690', 'Marcia Garcia', 'marcia.garcia@test.com',
                                           '76e67f3c40024dfd94bdb71976022839'),
                                  Model('HRV EX 1.8', Brand('Honda',
                                                            'e29ed583b9a246a8a7f1596593bb7888'),
                                        'b49aa1cb2082476bb3b6af601ec3ef9b'),
                                  2020)
            e.msg = "invalid model year - expected: > current year + 1"

    def test_create_model_year_less_than_limit(self):
        with self.assertRaises(VehicleExceptions) as e:
            VehicleFactory.create('ABC1234',
                                  Customer('58355843690', 'Marcia Garcia', 'marcia.garcia@test.com',
                                           '76e67f3c40024dfd94bdb71976022839'),
                                  Model('HRV EX 1.8', Brand('Honda',
                                                            'e29ed583b9a246a8a7f1596593bb7888'),
                                        'b49aa1cb2082476bb3b6af601ec3ef9b'),
                                  1899)
            e.msg = "invalid model year - expected: a very old year"

    def test_create_model_year_as_string(self):
        with self.assertRaises(VehicleExceptions) as e:
            VehicleFactory.create('ABC1234',
                                  Customer('58355843690', 'Marcia Garcia', 'marcia.garcia@test.com',
                                           '76e67f3c40024dfd94bdb71976022839'),
                                  Model('HRV EX 1.8', Brand('Honda',
                                                            'e29ed583b9a246a8a7f1596593bb7888'),
                                        'b49aa1cb2082476bb3b6af601ec3ef9b'),
                                  'new')
            e.msg = "invalid model year - expected: a string"
