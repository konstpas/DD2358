#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 15:17:13 2023

@author: konstantinos
"""
import numpy as np
cimport numpy as np

def gauss_seidel(double[:,:] f):
    cdef double [:,:] newf = f.copy()
    cdef unsigned int i, j
    # newf = f.copy()
    for i in range(1,newf.shape[0]-1):
        for j in range(1,newf.shape[1]-1):
            newf[i,j] = 0.25 * (newf[i,j+1] + newf[i,j-1] +
                                   newf[i+1,j] + newf[i-1,j])
    return newf