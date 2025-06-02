#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name='radicale-sql',
    version='0.1.0',
    packages=['radicale_sql'],
    description='A SQL backed storage for radicale.',
    url='https://github.com/koalyorg/radicale-sql',
    install_requires=[
        "requests",
        "sqlalchemy",
    ],

)
