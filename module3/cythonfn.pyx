#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 18:50:55 2023

@author: konstantinos
"""
from timeit import default_timer as timer
import numpy as np
cimport numpy as np

def benchmark_numpy(unsigned int STREAM_ARRAY_SIZE):

    cdef double [:] a = np.ones(STREAM_ARRAY_SIZE, dtype=np.float64)
    cdef double [:] b = np.full(STREAM_ARRAY_SIZE, 2.0, dtype=np.float64)
    cdef double [:] c = np.zeros(STREAM_ARRAY_SIZE, dtype=np.float64)
    cdef double [:] times = np.empty(4, dtype=np.float64)
    cdef double scalar 
    scalar = 2.0 
    
    # copy
    times[0] = timer()
    c = np.copy(a)
    times[0] = timer() - times[0]
    
    # scale
    times[1] = timer()
    b = np.multiply(scalar,b)
    times[1] = timer() - times[1]
    
    #sum
    times[2] = timer()
    c = np.add(a,b)
    times[2] = timer() - times[2]
    
    # triad
    times[3] = timer()
    # a = b+scalar*c
    c = np.add(b,np.multiply(scalar,c))
    times[3] = timer() - times[3]
    return times