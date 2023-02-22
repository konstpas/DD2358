#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 12:14:24 2023

@author: konstantinos
"""


import statistics
import h5py
from functools import wraps
from timeit import default_timer
import numpy as np
import cythonfn2
import matplotlib.pyplot as plt

def timefn(fn):
    @wraps(fn)
    def measure_time(*args, **kwargs):
        dt = []
        for i in range(10):
            t1 = default_timer()
            result = fn(*args, **kwargs)
            t2 = default_timer()
            dt.append(t2-t1)
            # print(f"@timefn: {fn.__name__} took {t2 - t1} seconds")
        deviation = statistics.stdev(dt)
        average = statistics.mean(dt)
        print(f"@timefn: {fn.__name__} deviation {deviation}")
        print(f"@timefn: {fn.__name__} On average took {average}")
        measurments = [0,0]
        measurments[0] = average
        measurments[1] = deviation
        # return measurments
        return result
    return measure_time

# @timefn
def gauss_seidel(f):
    # newf = f.copy()    
    # for i in range(1,grid_points-1):
    #     for j in range(1,grid_points-1):
    #         newf[i][j] = 0.25 * (newf[i][j+1] + newf[i][j-1] +
    #                                newf[i+1][j] + newf[i-1][j])
    
    newf = f.copy()
    for i in range(1,newf.shape[0]-1):
        for j in range(1,newf.shape[1]-1):
            newf[i,j] = 0.25 * (newf[i,j+1] + newf[i,j-1] +
                                   newf[i+1,j] + newf[i-1,j])
    
    return newf

# @timefn
def initialize(grid_points):
    x = np.random.rand(grid_points,grid_points)
    x[0,:] = 0
    x[:,0] = 0
    x[grid_points-1,:] = 0
    x[:,grid_points-1] = 0
    return x

def task2p1():
    time_cython = np.empty((100), dtype=object)
    time_pure = np.empty((100), dtype=object)
    for i in range(50,100):
        grid_points = i
        iterations = 5
        grid_shape = (grid_points, grid_points)
        xmax, ymax = grid_shape
        x = initialize(grid_points)
        
        t1= default_timer()
        for j in range(iterations):    
            x = cythonfn2.gauss_seidel(np.array(x))
        t2= default_timer()
        time_cython[i] = t2 - t1
        
        x = initialize(grid_points)
        t1= default_timer()
        for j in range(iterations):    
            x = gauss_seidel(np.array(x))
        t2= default_timer()
        time_pure[i] = t2 - t1
        
    fig1, ax1 = plt.subplots()
    plt.plot(range(50,100), time_cython[50:100])
    plt.xlabel('Array elements')
    plt.ylabel('Time [s]')
    
    fig2, ax1 = plt.subplots()
    plt.plot(range(50,100), time_pure[50:100])
    plt.xlabel('Array elements')
    plt.ylabel('Time [s]')

def ngbr_average(grid):
    return (np.multiply(0.25,
        np.roll(grid, +1, 0) + 
        np.roll(grid, -1, 0) +
        np.roll(grid, +1, 1) + 
        np.roll(grid, -1, 1)))

# @timefn
if __name__ == "__main__":
    # task2p1()
    grid_points = 100
    iterations = 100
    grid_shape = (grid_points, grid_points)
    xmax, ymax = grid_shape
    x = initialize(grid_points)
    for j in range(iterations):    
        x = cythonfn2.gauss_seidel(np.array(x))
        
    # Save x to HDF5
    # file_object  = open("/poisson_homogenious_dirichlet.hdf5", "w+")
    # file_object.close()
    f = h5py.File("./poisson_homogenious_dirichlet.hdf5", "w") 
    f["/x-values"] = x 
    
    