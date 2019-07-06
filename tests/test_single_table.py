import unittest

import mwb

from tests.common import get_absolute_path

class TestSingleTable(unittest.TestCase):
    def setUp(self):
        filename = get_absolute_path('single_table.mwb')
        self.model = mwb.Model(filename)

    def test_model(self):
        self.assertEqual(len(self.model.schemas), 1)
        self.assertIsNotNone(self.model.get_schema('mydb'))

    def test_schema(self):
        mydb_schema = self.model.get_schema('mydb')
        self.assertEqual(mydb_schema.name, 'mydb')
        self.assertEqual(len(mydb_schema.tables), 1)
        self.assertIsNotNone(mydb_schema.get_table('person'))

    def test_table(self):
        person_table = self.model.get_schema('mydb').get_table('person')
        self.assertEqual(person_table.name, 'person')
        self.assertEqual(len(person_table.columns), 4)
        self.assertIsNotNone(person_table.get_column('person_id'))
        self.assertIsNotNone(person_table.get_column('first_name'))
        self.assertIsNotNone(person_table.get_column('last_name'))
        self.assertIsNotNone(person_table.get_column('date_of_birth'))

    def test_columns(self):
        person_table = self.model.get_schema('mydb').get_table('person')

        person_id_column = person_table.get_column('person_id')
        self.assertEqual(person_id_column.name, 'person_id')
        self.assertEqual(person_id_column.datatype, 'INT')
        self.assertIsNone(person_id_column.length)
        self.assertIsNone(person_id_column.precision)
        self.assertIsNone(person_id_column.scale)
        self.assertFalse(person_id_column.explicit_parameters)

        first_name_column = person_table.get_column('first_name')
        self.assertEqual(first_name_column.name, 'first_name')
        self.assertEqual(first_name_column.datatype, 'VARCHAR')
        self.assertEqual(first_name_column.length, 45)
        self.assertIsNone(first_name_column.precision)
        self.assertIsNone(first_name_column.scale)
        self.assertFalse(first_name_column.explicit_parameters)

        last_name_column = person_table.get_column('last_name')
        self.assertEqual(last_name_column.name, 'last_name')
        self.assertEqual(last_name_column.datatype, 'VARCHAR')
        self.assertEqual(last_name_column.length, 45)
        self.assertIsNone(last_name_column.precision)
        self.assertIsNone(last_name_column.scale)
        self.assertFalse(last_name_column.explicit_parameters)

        date_of_birth_column = person_table.get_column('date_of_birth')
        self.assertEqual(date_of_birth_column.name, 'date_of_birth')
        self.assertEqual(date_of_birth_column.datatype, 'DATE')
        self.assertIsNone(date_of_birth_column.length)
        self.assertIsNone(date_of_birth_column.precision)
        self.assertIsNone(date_of_birth_column.scale)
        self.assertFalse(date_of_birth_column.explicit_parameters)
