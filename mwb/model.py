import xml.etree.ElementTree as ET
from zipfile import ZipFile

from mwb.schema import Schema

class Model:
    """Represents a MySQL Workbench model.

    Attributes:
        schemas: A list of the schemas contained in this model.
    """

    def __init__(self, filename):
        """Creates a new model from the specified file.

        Args:
            filename: The name of the file from which to create the model.
        """
        with ZipFile(filename, 'r') as mwb_file:
            document_xml = mwb_file.read('document.mwb.xml')
            root = ET.fromstring(document_xml)
            model_element = root.find('.//value[@struct-name="workbench.physical.Model"]')
            self.schemas = []
            schema_elements = model_element.findall('.//value[@struct-name="db.mysql.Schema"]')
            for schema_element in schema_elements:
                self.schemas.append(Schema(schema_element))

    def get_schema(self, name):
        """Gets the schema with the given name, None if it does not exist.

        Args:
            name: The name of the schema to get.

        Returns:
            The schema with the given name, None if there is not a schema with
            that name.
        """
        for schema in self.schemas:
            if schema.name == name:
                return schema
        return None
