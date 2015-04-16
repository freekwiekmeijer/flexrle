# coding:utf-8

from setuptools import setup, find_packages

common_properties = {
    "short_description": "Run length encoding and decoding library",
    "author": "Freek Wiekmeijer",
    "license": "Apache Licence, Version 2.0",
}

long_description = """\
%(short_description)s.
Implements run length encoding and decoding with variable word sizes.
Copyright (c) 2015, %(author)s.
License: %(license)s
""" % common_properties

setup(
    author=common_properties["author"],
    author_email='community@rbiv.nl',
    # Trove classifiers: see https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Archiving :: Compression',
    ],
    description=common_properties["short_description"],
    install_requires=[],
    license=common_properties["license"],
    long_description=long_description,
    name='flexrle',
    packages=find_packages(),
    platforms='any',
    url='http://github.com/freekwiekmeijer/flexrle',
    version='0.0.2',
)