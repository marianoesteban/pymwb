import unittest

import mwb

from tests.common import get_absolute_path

class TestTwoSchemas(unittest.TestCase):
    def setUp(self):
        filename = get_absolute_path('two_schemas.mwb')
        self.model = mwb.Model(filename)

    def test_model(self):
        self.assertEqual(len(self.model.schemas), 2)
        self.assertIsNotNone(self.model.get_schema('db1'))
        self.assertIsNotNone(self.model.get_schema('db2'))

    def test_schemas(self):
        db1_schema = self.model.get_schema('db1')
        self.assertEqual(db1_schema.name, 'db1')
        self.assertEqual(len(db1_schema.tables), 0)

        db2_schema = self.model.get_schema('db2')
        self.assertEqual(db2_schema.name, 'db2')
        self.assertEqual(len(db2_schema.tables), 0)
