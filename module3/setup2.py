#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 10:29:19 2023

@author: konstantinos
"""

from distutils.core import setup
from Cython.Build import cythonize
import numpy

# setup(ext_modules=cythonize("cythonfn.pyx", 
#                             compiler_directives={"language_level": "3"}))
setup(ext_modules=cythonize("cythonfn2.pyx", 
                            compiler_directives={"language_level": "3"}),
                            include_dirs=[numpy.get_include()])