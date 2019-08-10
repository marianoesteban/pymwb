from mwb.table import Table
from mwb.view import View

class Schema:
    """Represents a MySQL schema.

    Attributes:
        name: The name of the schema.
        tables: A list of the tables in the schema.
        views: A list of the views in the schema.
    """

    def __init__(self, schema_element):
        """Creates a new schema from the schema_element element.

        Args:
            schema_element: An element containing the schema's data.
        """
        # name
        self.name = schema_element.find('./value[@key="name"]').text

        # tables
        self.tables = []
        table_elements = schema_element.findall('.//value[@struct-name="db.mysql.Table"]')
        for table_element in table_elements:
            self.tables.append(Table(table_element))

        # views
        self.views = []
        view_elements = schema_element.findall('.//value[@struct-name="db.mysql.View"]')
        for view_element in view_elements:
            self.views.append(View(view_element))

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

    def get_view(self, name):
        """Gets the view with the given name, None if it does not exist.

        Args:
            name: The name of the view to get.

        Returns:
            The view with the given name, or None if there is not one with that
            name.
        """
        for view in self.views:
            if view.name == name:
                return view
        return None
