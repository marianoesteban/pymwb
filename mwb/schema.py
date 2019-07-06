from mwb.table import Table

class Schema:
    """Represents a MySQL schema.

    Attributes:
        name: The name of the schema.
        tables: A list of the tables in the schema.
    """

    def __init__(self, schema_element):
        """Creates a new schema from the schema_element element.

        Args:
            schema_element: An element containing the schema's data.
        """
        self.name = schema_element.find('./value[@key="name"]').text
        self.tables = []
        table_elements = schema_element.findall('.//value[@struct-name="db.mysql.Table"]')
        for table_element in table_elements:
            self.tables.append(Table(table_element))

    def get_table(self, name):
        """Gets the table with the given name, None if it does not exist.

        Args:
            name: The name of the table to get.

        Returns:
            The table with the given name, or None if there is not one with that
            name.
        """
        for table in self.tables:
            if table.name == name:
                return table
        return None
