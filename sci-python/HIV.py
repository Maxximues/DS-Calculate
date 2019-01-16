#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 11:27:10 2018

@author: linuxhan
"""
import numpy as np
import matplotlib.pyplot as plt

# Standard data
standard_data = np.load('set/Datasets/01HIVseries/HIVseries.npz')
standard_time = standard_data[:, 0]
standard_virtal_load = standard_data[:, 1]
plt.plot(standard_time, standard_virtal_load, 'r:o')

# curve fitting
Inclination = np.sum(standard_time[9:]*standard_virtal_load[9:])/7
curve_virtal_load = Inclination/standard_time[5:]
plt.plot(standard_time[5:], curve_virtal_load, 'b:o')
# time = standard_time
# virtal_load = A*np.exp(-alpha*time)+B*np.exp(-beta*time)
