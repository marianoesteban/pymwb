import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='pymwb',
    version='0.1',
    author='Mariano Esteban',
    description='A library for reading MySQL Workbench MWB files',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    test_suite='tests',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developer',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries'
    ]
)
