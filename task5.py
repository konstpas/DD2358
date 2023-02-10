#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 20:04:23 2023

@author: konstantinos
"""

from math import pi, sqrt
import logging
from timeit import default_timer
import numpy as np
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.INFO, file="sample.log")


# @profile
def get_dft_matrix(size):
    """get_dft_matrix(size) generate the DFT matrix for a given size"""
    i, j = np.meshgrid(np.arange(size), np.arange(size))
    omega = np.exp(-2 * pi * 1j / size)
    out = np.power(omega, i * j) / sqrt(size)
    return out

if __name__ == "__main__":
    SIZE = 1024
    time = np.empty((SIZE), dtype=object)
    for k in range(8,SIZE):
        input_signal = np.random.rand(k)
        t1 = default_timer()
        dft_matrix = get_dft_matrix(k)
        output_signal = np.matmul(input_signal, dft_matrix)
        t2 = default_timer()
        time[k] = t2-t1

    plt.plot(range(SIZE), time[:])
    plt.xlabel('Array elements')
    plt.ylabel('Time [s]')

    logging.info("The DFT of {input_signal} is {output_signal}, the DFT matrix is {dft_matrix}")
