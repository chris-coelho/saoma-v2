from unittest import TestCase

from src.domain.modules.entity_base import EntityBase


class EntityBaseTest(TestCase):
    def test_get_id_none(self):
        id = EntityBase.get_id(None)
        self.assertIsNotNone(id)
        self.assertEqual(len(id), 32)

    def test_get_id_with_value(self):
        id = EntityBase.get_id('b07e1d28b7cf45deb63ff5f19e764f90')
        self.assertEqual(id, 'b07e1d28b7cf45deb63ff5f19e764f90')


