#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 19:16:42 2023

@author: konstantinos
"""

from functools import wraps
import statistics
import numpy as np
from timeit import default_timer
import pytest 
from array import array
import matplotlib.pyplot as plt


def timefn(fn):
    @wraps(fn)
    def measure_time(*args, **kwargs):
        dt = []
        for i in range(5):
            t1 = default_timer()
            result = fn(*args, **kwargs)
            t2 = default_timer()
            dt.append(t2-t1)
            # print(f"@timefn: {fn.__name__} took {t2 - t1} seconds")
        deviation = statistics.stdev(dt)
        average = statistics.mean(dt)
        # print(f"@timefn: {fn.__name__} deviation {deviation}")
        # print(f"@timefn: {fn.__name__} On average took {average}")
        measurments = [0,0]
        measurments[0] = average
        measurments[1] = deviation
        return measurments
        # return result
    return measure_time


def test_dgemm_np():
    a = np.matrix('1 3 5; 2 4 6')
    b = np.matrix('1 6; 3 9; 5 11')
    c = np.matrix('1 2; 3 4')
    cf = np.matrix('0 0; 0 0')
    result = np.matrix('36, 90; 47, 118')
    cf = dgemm_np(a,b,c);
    assert np.allclose(result,cf)
    # np.testing.assert_allclose(result, cf)


def test_dgemm_list():
    a = [[x+2*y for x in range(2)] for y in range(2)]
    b = [[x+2*y for x in range(2)] for y in range(2)]
    c = [[x+2*y for x in range(2)] for y in range(2)]
    cf = [[0.0, 0.0], [0.0, 0.0]]
    result = [[2.0, 4.0], [8.0, 14.0]]
    cf = dgemm_lists(a,b,c);
    assert np.allclose(result,cf)
    
    
def test_dgemm_array():
    a =  array('d', range(4))
    b = array('d', range(4))
    c = array('d', range(4))
    cf = array('d', range(4))
    result = array('d', [2, 4, 8, 14])
    cf = dgemm_array(a,b,c);
    assert np.allclose(result,cf)
    
    
@timefn
def dgemm_np(a,b,c):
    c += np.matmul(a,b)
    return c


@timefn
def dgemm_lists(a,b,c):
    N = len(c)
    for i in range(N):
        for j in range(N):
            for k in range(N):
                c[i][j] = c[i][j] + a[i][k]*b[k][j]
    return c


@timefn
def dgemm_array(a,b,c):
    N = len(c)
    for i in range(N):
        for j in range(N):
            for k in range(N):
                c[i*N + j] = c[i*N + j] + a[i*N + k]*b[k*N+j]
    return c


if __name__ == "__main__":
    
    N = 1024
    time_np = np.empty((N,2), dtype=object)
    time_list = np.empty((N,2), dtype=object)
    time_array = np.empty((N,2), dtype=object)
    
    for i in range(N):
        # anp = np.empty((i,i), dtype=object)
        # bnp = np.empty((i,i), dtype=object)
        # cnp = np.empty((i,i), dtype=object)
        
        anp = np.random.rand(i,i)
        bnp = np.random.rand(i,i)
        cnp = np.random.rand(i,i)
        time_np[i] = dgemm_np(anp,bnp,cnp)     
        # test_dgemm_np()
        
        
        # alist = [[np.random.rand() for x in range(i)] for y in range(i)] 
        # blist = [[np.random.rand() for x in range(i)] for y in range(i)] 
        # clist = [[np.random.rand() for x in range(i)] for y in range(i)] 
        # time_list[i] = dgemm_lists(alist,blist,clist) 
        # # test_dgemm_list()
        
        # # Since the array.array type does not support
        # # 2D data, we store them in 1D of N^2 elements
        # # assuming a row-major way
        # aarray = array('d', range(i*i))
        # barray = array('d', range(i*i))
        # carray = array('d', range(i*i))
        # time_array[i] =  dgemm_array(aarray,barray,carray)     
        # # test_dgemm_array()

    # plt.figure(0)
    # plt.plot(range(N), time_array[:,0])
    # plt.plot(range(N), time_array[:,0]+time_array[:,1])
    # plt.plot(range(N), time_array[:,0]-time_array[:,1])
    # plt.xlabel('Array elements')
    # plt.ylabel('Time [s]')
    
    # plt.figure(1)
    # plt.plot(range(N), time_list[:,0])
    # plt.plot(range(N), time_list[:,0]+time_list[:,1])
    # plt.plot(range(N), time_list[:,0]-time_list[:,1])
    # plt.xlabel('List elements')
    # plt.ylabel('Time [s]')
    
    plt.figure(2)
    plt.plot(range(N), time_np[:,0])
    plt.plot(range(N), time_np[:,0]+time_np[:,1])
    plt.plot(range(N), time_np[:,0]-time_np[:,1])
    plt.xlabel('Numpy array elements')
    plt.ylabel('Time [s]')