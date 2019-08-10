# pymwb

A simple library to read MySQL Workbench MWB files.

## Requirements

* Python 3.7

## Installation

You can clone the repository and install the package:

```bash
$ git clone https://github.com/marianoesteban/pymwb.git
$ cd pymwb
$ python setup.py install
```

## Usage

Here is an example that prints the basic contents of an MWB file:

```python
import mwb

example_model = mwb.Model('example_file.mwb')

for schema in example_model.schemas:
    print('Schema:', schema.name)
    for table in schema.tables:
        print('\tTable:', table.name)
        for column in table.columns:
            print('\t\t' + column.name + ':', column.datatype)
    for view in schema.views:
        print('\tView:', view.name)
```

## Missing features

The following features are not yet implemented:

* Primary keys
* Foreign keys
* Relationships
* Column attributes (not null, unique, binary, etc.)
* User types
