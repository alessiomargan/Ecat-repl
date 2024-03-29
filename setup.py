#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io
import re

from setuptools import setup

with io.open("README.md", "rt", encoding="utf8") as f:
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
        "protobuf",
        "protobuf3-to-dict",
        "PyYAML",
        "pyzmq",
    ],
    extras_require={
        "dotenv": ["python-dotenv"],
        "dev": [
            "pytest>=3",
            "coverage",
            "tox",
            "sphinx",
            "pallets-sphinx-themes",
            "sphinxcontrib-log-cabinet",
        ],
        "docs": ["sphinx", "pallets-sphinx-themes", "sphinxcontrib-log-cabinet"],
    },
)
