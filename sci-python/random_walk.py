#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 10:39:14 2018

@author: linuxhan
"""
from numpy.random import random as rng
import matplotlib.pyplot as plt

num_steps = 500
x_steps = rng(num_steps) > 0.5
y_steps = rng(num_steps) > 0.5
x_step = x_steps*2 -1
y_step = x_steps*2 -1
# np.cumsum(x_step)
# np.cumsum(y_step)
plt.plot(np.cumsum(x_step), np.cumsum(x_step), "ro")
