#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

version = '0.0.1'


setup(name="birman",  # Nombre
      version=version,  # Versión de desarrollo
      description="Paquete para ordenamiento causal",  # Descripción del funcionamiento
      author="Adrian Sosa",  # Nombre del autor
      author_email='asosam91@gmail.com',  # Email del autor
 #     license="GPL",  # Licencia: MIT, GPL, GPL 2.0...
      url="http://github.com/asosam91/Grafos",
      packages =  find_packages(),
      include_package_data=False,
      zip_safe=False,
)