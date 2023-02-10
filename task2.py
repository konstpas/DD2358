#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 10:36:13 2023

@author: konstantinos
"""
from timeit import default_timer as timer
import sys
import matplotlib.pyplot as plt
import numpy as np
from array import array


def benchmark_list(STREAM_ARRAY_SIZE):
    # a = [[0.0] for i in range(STREAM_ARRAY_SIZE)]
    # b = [[0.0] for i in range(STREAM_ARRAY_SIZE)]
    # c = [[0.0] for i in range(STREAM_ARRAY_SIZE)]
    a = list(range(i))
    b = list(range(i))
    c = list(range(i))
    times = [0 for i in range(4)]
    scalar = 2.0    
    for j in range(STREAM_ARRAY_SIZE):
        a[j] = 1.0
        b[j] = 2.0
        c[j] = 0.0
    
    # copy
    times[0] = timer()
    for j in range(STREAM_ARRAY_SIZE):
          c[j] = a[j]
    times[0] = timer() - times[0]
    
    # scale
    times[1] = timer()
    for j in range(STREAM_ARRAY_SIZE):
         b[j] = scalar*c[j]
    times[1] = timer() - times[1]
    
    #sum
    times[2] = timer()
    for j in range(STREAM_ARRAY_SIZE):
         c[j] = a[j]+b[j]
    times[2] = timer() - times[2]
    
    # triad
    times[3] = timer()
    for j in range(STREAM_ARRAY_SIZE):
        a[j] = b[j]+scalar*c[j]
    times[3] = timer() - times[3]
    return times


def benchmark_array(STREAM_ARRAY_SIZE):
    # a = [[0.0] for i in range(STREAM_ARRAY_SIZE)]
    # b = [[0.0] for i in range(STREAM_ARRAY_SIZE)]
    # c = [[0.0] for i in range(STREAM_ARRAY_SIZE)]
    a = array('d', range(i))
    b = array('d', range(i))
    c = array('d', range(i))
    times = [0 for i in range(4)]
    scalar = 2.0    
    for j in range(STREAM_ARRAY_SIZE):
        a[j] = 1.0
        b[j] = 2.0
        c[j] = 0.0
    
    # copy
    times[0] = timer()
    for j in range(STREAM_ARRAY_SIZE):
          c[j] = a[j]
    times[0] = timer() - times[0]
    
    # scale
    times[1] = timer()
    for j in range(STREAM_ARRAY_SIZE):
         b[j] = scalar*c[j]
    times[1] = timer() - times[1]
    
    #sum
    times[2] = timer()
    for j in range(STREAM_ARRAY_SIZE):
         c[j] = a[j]+b[j]
    times[2] = timer() - times[2]
    
    # triad
    times[3] = timer()
    for j in range(STREAM_ARRAY_SIZE):
        a[j] = b[j]+scalar*c[j]
    times[3] = timer() - times[3]
    return times

def benchmark_numpy(STREAM_ARRAY_SIZE):
    a = np.empty(STREAM_ARRAY_SIZE, dtype=object)
    b = np.empty(STREAM_ARRAY_SIZE, dtype=object)
    c = np.empty(STREAM_ARRAY_SIZE, dtype=object)
    scalar = 2.0    
    times = [0 for i in range(4)]
    for j in range(STREAM_ARRAY_SIZE):
        a[j] = 1.0
        b[j] = 2.0
        c[j] = 0.0
    
    # copy
    times[0] = timer()
    # for j in range(STREAM_ARRAY_SIZE):
    #       c[j] = a[j]
    c = a
    times[0] = timer() - times[0]
    
    # scale
    times[1] = timer()
    # for j in range(STREAM_ARRAY_SIZE):
    #      b[j] = scalar*c[j]
    b = scalar*c
    times[1] = timer() - times[1]
    
    #sum
    times[2] = timer()
    # for j in range(STREAM_ARRAY_SIZE):
    #      c[j] = a[j]+b[j]
    c = a + b
    times[2] = timer() - times[2]
    
    # triad
    times[3] = timer()
    # for j in range(STREAM_ARRAY_SIZE):
    #     a[j] = b[j]+scalar*c[j]
    a = b+scalar*c
    times[3] = timer() - times[3]
    return times



if __name__ == "__main__":
    max_size = 4096 
    times = [0 for i in range(4)]
    bw = [0 for i in range(max_size)]
    for i in range(max_size):
        times = benchmark_array(i)
        data_size = 10*sys.getsizeof(i)*i
        bw[i] = data_size*1e-9/(times[0]+times[1]+times[2]+times[3])
    plt.plot(range(max_size), bw)
    plt.xlabel('Array elements')
    plt.ylabel('Bandwidth [GB/s]')
    for i in range(max_size):
        times = benchmark_numpy(i)
        data_size = 10*sys.getsizeof(i)*i
        bw[i] = data_size*1e-9/(times[0]+times[1]+times[2]+times[3])
    plt.plot(range(max_size), bw)
    plt.xlabel('Array elements')
    plt.ylabel('Bandwidth [GB/s]')
    for i in range(max_size):
        times = benchmark_list(i)
        data_size = 10*sys.getsizeof(i)*i
        bw[i] = data_size*1e-9/(times[0]+times[1]+times[2]+times[3])
    plt.plot(range(max_size), bw)
    plt.xlabel('Array elements')
    plt.ylabel('Bandwidth [GB/s]')
    