class View:
    """Represents a MySQL view.

    Attributes:
        name: The name of the view.
        sql_definition: The SQL statement used to create the view.
    """

    def __init__(self, view_element):
        """Creates a new view from the view_element element.

        Args:
            view_element: An element containing the view's data.
        """
        self.name = view_element.find('./value[@key="name"]').text
        self.sql_definition = view_element.find('./value[@key="sqlDefinition"]').text
