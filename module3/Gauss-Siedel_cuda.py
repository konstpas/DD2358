#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 19:04:52 2023

@author: konstantinos
"""


from timeit import default_timer
# import numpy as np
from torch import roll, multiply
import torch
# import cythonfn2

def initialize(grid_points):
    x = torch.rand(grid_points,grid_points)
    x = x.cuda()
    x[0,:] = 0
    x[:,0] = 0
    x[grid_points-1,:] = 0
    x[:,grid_points-1] = 0
    return x

def gauss_seidel(grid):
    return (multiply(0.25,
        roll(grid, +1, 0) + 
        roll(grid, -1, 0) +
        roll(grid, +1, 1) + 
        roll(grid, -1, 1)))

if __name__ == "__main__":
    # task2p1()
    grid_points = 100
    iterations = 1000
    x = initialize(grid_points)
    t1 = default_timer()
    for j in range(iterations):    
        # x = cythonfn2.gauss_seidel(np.array(x))
        x = gauss_seidel(x)
    t2 = default_timer();
    print({t2-t1})
    