#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 14:33:03 2018

@author: linuxhan
"""
import numpy as np
import matplotlib.pyplot as plt

# Standard Data
standard_data = np.load('set/Datasets/15novick/g149novickB.npy')
standard_time = standard_data[:, 0]
standard_W = standard_data[:, 1]
plt.plot(standard_time, standard_W, 'ro')

# new_fiting
standard_time_copy = standard_time[12:]
standard_W_copy = standard_W[12:]
Inclination = (np.sum(standard_W_copy[4:])-np.sum(standard_W_copy[:4])) / (np.sum(standard_time_copy[4:])-np.sum(standard_time_copy[:4]))
fitting_y = -0.0100 # standard_W_copy[5] - Inclination*standard_time_copy[5]
fitting_Y = Inclination*standard_time + fitting_y
plt.plot(standard_time, fitting_Y, "bo")

# fitting
time = standard_data[:, 0]
tau = (fitting_Y[-1]-fitting_y)/(fitting_y)
A = tau*fitting_y
W = A*(np.exp(-time/tau)-1+1/tau)
plt.plot(time, W, 'go')
