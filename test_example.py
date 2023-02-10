#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 19:28:58 2023

@author: konstantinos
"""
import pytest #make sure to start function name with test

def sum(num1, num2):
    """It returns sum of two numbers"""
    return num1 + num2


def test_sum():
    assert sum(1, 2) == 3