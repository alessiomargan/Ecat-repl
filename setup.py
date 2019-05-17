#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io
import re

from setuptools import setup

with io.open("README.txt", "rt", encoding="utf8") as f:
    readme = f.read()

with io.open("ecat_repl/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r"__version__ = \"(.*?)\"", f.read()).group(1)

setup(
    name='ecat_repl',
    version=version,
    author='Alessio Margan',
    author_email='alessio.margan@gmail.com',
    packages=['ecat_repl', 'ecat_repl.test'],
    url='http://pypi.python.org/pypi/PackageName/',
    license='LICENSE.txt',
    description='An awesome package that does something',
    long_description=readme,
    install_requires=[
        "protobuf>=3.7.0",
        "protobuf3-to-dict>=0.1.5",
        "PyYAML>=3.13",
        "pyzmq==18.0.1",
        "pytest",
    ],
)
