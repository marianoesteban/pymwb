from mwb.column import Column

class Table:
    """Represents a MySQL table.

    Attributes:
        name: The name of the table.
        columns: The columns of the table.
    """

    def __init__(self, table_element):
        """Creates a new table from the table_element element.

        Args:
            table_element: An element containing the table's data.
        """
        self.name = table_element.find('./value[@key="name"]').text
        self.columns = []
        column_elements = table_element.findall('.//value[@struct-name="db.mysql.Column"]')
        for column_element in column_elements:
            self.columns.append(Column(column_element))

    def get_column(self, name):
        """Gets the column with the given name.

        Args:
            name: The name of the column to get.

        Returns:
            The column with the given name, or None if there is not a column
            with that name.
        """
        for column in self.columns:
            if column.name == name:
                return column
        return None
