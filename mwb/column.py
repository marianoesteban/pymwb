from ast import literal_eval

class Column:
    """Represents a column of a MySQL table.

    Attributes:
        name: The name of the column.
        datatype: The datatype of the column.
        length: The length of the column, or None if it has no length.
        precision: The precision of the column, or None if it has no precision.
        scale: The scale of the column, or None if it has no scale.
        explicit_parameters: A tuple containing the explicit parameters of the
            datatype.
    """

    def __init__(self, column_element):
        """Creates a new column from the column_element element.

        Args:
            column_element: An element containing the column's data.
        """
        # name
        self.name = column_element.find('./value[@key="name"]').text

        # datatype
        simple_type_element = column_element.find('./link[@key="simpleType"]')
        if simple_type_element is not None:
            self.datatype = simple_type_element.text
        else:
            self.datatype = column_element.find('./link[@key="userType"]').text
        self.datatype = self.datatype[self.datatype.rindex('.')+1:].upper()
        if self.datatype.rfind('_') != -1:
            self.datatype = self.datatype[:self.datatype.rfind('_')]

        # length
        self.length = int(column_element.find('./value[@key="length"]').text)
        if self.length == -1:
            self.length = None

        # precision
        self.precision = int(column_element.find('./value[@key="precision"]').text)
        if self.precision == -1:
            self.precision = None

        # scale
        self.scale = int(column_element.find('./value[@key="scale"]').text)
        if self.scale == -1:
            self.scale = None

        # explicit parameters
        datatype_explicit_params = column_element.find('./value[@key="datatypeExplicitParams"]').text
        if datatype_explicit_params is not None:
            self.explicit_parameters = literal_eval(datatype_explicit_params) # convert string to tuple
        else:
            self.explicit_parameters = ()
