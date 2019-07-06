import os

def get_absolute_path(filename):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), 'fixtures', filename))
