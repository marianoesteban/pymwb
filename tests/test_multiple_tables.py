import unittest

import mwb

from tests.common import get_absolute_path

class TestMultipleTables(unittest.TestCase):
    def setUp(self):
        filename = get_absolute_path('multiple_tables.mwb')
        self.model = mwb.Model(filename)

    def test_model(self):
        self.assertEqual(len(self.model.schemas), 1)
        self.assertIsNotNone(self.model.get_schema('mydb'))

    def test_schema(self):
        mydb_schema = self.model.get_schema('mydb')
        self.assertEqual(mydb_schema.name, 'mydb')
        self.assertEqual(len(mydb_schema.tables), 4)
        self.assertIsNotNone(mydb_schema.get_table('article'))
        self.assertIsNotNone(mydb_schema.get_table('country'))
        self.assertIsNotNone(mydb_schema.get_table('user'))
        self.assertIsNotNone(mydb_schema.get_table('product'))

    def test_tables(self):
        mydb_schema = self.model.get_schema('mydb')

        article_table = mydb_schema.get_table('article')
        self.assertEqual(article_table.name, 'article')
        self.assertEqual(len(article_table.columns), 4)
        self.assertIsNotNone(article_table.get_column('article_id'))
        self.assertIsNotNone(article_table.get_column('title'))
        self.assertIsNotNone(article_table.get_column('content'))
        self.assertIsNotNone(article_table.get_column('creation_date'))

        country_table = mydb_schema.get_table('country')
        self.assertEqual(country_table.name, 'country')
        self.assertEqual(len(country_table.columns), 3)
        self.assertIsNotNone(country_table.get_column('country_id'))
        self.assertIsNotNone(country_table.get_column('name'))
        self.assertIsNotNone(country_table.get_column('continent'))

        user_table = mydb_schema.get_table('user')
        self.assertEqual(user_table.name, 'user')
        self.assertEqual(len(user_table.columns), 4)
        self.assertIsNotNone(user_table.get_column('user_id'))
        self.assertIsNotNone(user_table.get_column('username'))
        self.assertIsNotNone(user_table.get_column('registration_date'))
        self.assertIsNotNone(user_table.get_column('premium_user'))

        product_table = mydb_schema.get_table('product')
        self.assertEqual(product_table.name, 'product')
        self.assertEqual(len(product_table.columns), 4)
        self.assertIsNotNone(product_table.get_column('product_id'))
        self.assertIsNotNone(product_table.get_column('name'))
        self.assertIsNotNone(product_table.get_column('description'))
        self.assertIsNotNone(product_table.get_column('price'))

    def test_columns(self):
        mydb_schema = self.model.get_schema('mydb')

        article_table = mydb_schema.get_table('article')

        article_id_column = article_table.get_column('article_id')
        self.assertEqual(article_id_column.name, 'article_id')
        self.assertEqual(article_id_column.datatype, 'INT')
        self.assertIsNone(article_id_column.length)
        self.assertIsNone(article_id_column.precision)
        self.assertIsNone(article_id_column.scale)
        self.assertFalse(article_id_column.explicit_parameters)

        title_column = article_table.get_column('title')
        self.assertEqual(title_column.name, 'title')
        self.assertEqual(title_column.datatype, 'VARCHAR')
        self.assertEqual(title_column.length, 100)
        self.assertIsNone(title_column.precision)
        self.assertIsNone(title_column.scale)
        self.assertFalse(title_column.explicit_parameters)

        content_column = article_table.get_column('content')
        self.assertEqual(content_column.name, 'content')
        self.assertEqual(content_column.datatype, 'TEXT')
        self.assertIsNone(content_column.length)
        self.assertIsNone(content_column.precision)
        self.assertIsNone(content_column.scale)
        self.assertFalse(content_column.explicit_parameters)

        creation_date_column = article_table.get_column('creation_date')
        self.assertEqual(creation_date_column.name, 'creation_date')
        self.assertEqual(creation_date_column.datatype, 'DATETIME')
        self.assertIsNone(creation_date_column.length)
        self.assertIsNone(creation_date_column.precision)
        self.assertIsNone(creation_date_column.scale)
        self.assertFalse(creation_date_column.explicit_parameters)

        country_table = mydb_schema.get_table('country')

        country_id_column = country_table.get_column('country_id')
        self.assertEqual(country_id_column.name, 'country_id')
        self.assertEqual(country_id_column.datatype, 'INT')
        self.assertIsNone(country_id_column.length)
        self.assertIsNone(country_id_column.precision)
        self.assertIsNone(country_id_column.scale)
        self.assertFalse(country_id_column.explicit_parameters)

        country_name_column = country_table.get_column('name')
        self.assertEqual(country_name_column.name, 'name')
        self.assertEqual(country_name_column.datatype, 'VARCHAR')
        self.assertEqual(country_name_column.length, 45)
        self.assertIsNone(country_name_column.precision)
        self.assertIsNone(country_name_column.scale)
        self.assertFalse(country_name_column.explicit_parameters)

        continent_column = country_table.get_column('continent')
        self.assertEqual(continent_column.name, 'continent')
        self.assertEqual(continent_column.datatype, 'ENUM')
        self.assertIsNone(continent_column.length)
        self.assertIsNone(continent_column.precision)
        self.assertIsNone(continent_column.scale)
        self.assertEqual(len(continent_column.explicit_parameters), 6)
        self.assertIn('Africa', continent_column.explicit_parameters)
        self.assertIn('Asia', continent_column.explicit_parameters)
        self.assertIn('Europe', continent_column.explicit_parameters)
        self.assertIn('North America', continent_column.explicit_parameters)
        self.assertIn('Oceania', continent_column.explicit_parameters)
        self.assertIn('South America', continent_column.explicit_parameters)

        user_table = mydb_schema.get_table('user')

        user_id_column = user_table.get_column('user_id')
        self.assertEqual(user_id_column.name, 'user_id')
        self.assertEqual(user_id_column.datatype, 'INT')
        self.assertIsNone(user_id_column.length)
        self.assertIsNone(user_id_column.precision)
        self.assertIsNone(user_id_column.scale)
        self.assertFalse(user_id_column.explicit_parameters)

        username_column = user_table.get_column('username')
        self.assertEqual(username_column.name, 'username')
        self.assertEqual(username_column.datatype, 'VARCHAR')
        self.assertEqual(username_column.length, 45)
        self.assertIsNone(username_column.precision)
        self.assertIsNone(username_column.scale)
        self.assertFalse(username_column.explicit_parameters)

        registration_date_column = user_table.get_column('registration_date')
        self.assertEqual(registration_date_column.name, 'registration_date')
        self.assertEqual(registration_date_column.datatype, 'DATE')
        self.assertIsNone(registration_date_column.length)
        self.assertIsNone(registration_date_column.precision)
        self.assertIsNone(registration_date_column.scale)
        self.assertFalse(registration_date_column.explicit_parameters)

        premium_user_column = user_table.get_column('premium_user')
        self.assertEqual(premium_user_column.name, 'premium_user')
        self.assertEqual(premium_user_column.datatype, 'TINYINT')
        self.assertIsNone(premium_user_column.length)
        self.assertEqual(premium_user_column.precision, 1)
        self.assertIsNone(premium_user_column.scale)
        self.assertFalse(premium_user_column.explicit_parameters)

        product_table = mydb_schema.get_table('product')

        product_id_column = product_table.get_column('product_id')
        self.assertEqual(product_id_column.name, 'product_id')
        self.assertEqual(product_id_column.datatype, 'INT')
        self.assertIsNone(product_id_column.length)
        self.assertIsNone(product_id_column.precision)
        self.assertIsNone(product_id_column.scale)
        self.assertFalse(product_id_column.explicit_parameters)

        product_name_column = product_table.get_column('name')
        self.assertEqual(product_name_column.name, 'name')
        self.assertEqual(product_name_column.datatype, 'VARCHAR')
        self.assertEqual(product_name_column.length, 255)
        self.assertIsNone(product_name_column.precision)
        self.assertIsNone(product_name_column.scale)
        self.assertFalse(product_name_column.explicit_parameters)

        description_column = product_table.get_column('description')
        self.assertEqual(description_column.name, 'description')
        self.assertEqual(description_column.datatype, 'TEXT')
        self.assertIsNone(description_column.length)
        self.assertIsNone(description_column.precision)
        self.assertIsNone(description_column.scale)
        self.assertFalse(description_column.explicit_parameters)

        price_column = product_table.get_column('price')
        self.assertEqual(price_column.name, 'price')
        self.assertEqual(price_column.datatype, 'DECIMAL')
        self.assertIsNone(price_column.length)
        self.assertEqual(price_column.precision, 9)
        self.assertEqual(price_column.scale, 2)
        self.assertFalse(price_column.explicit_parameters)
