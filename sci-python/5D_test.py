#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 20:05:03 2018

@author: linuxhan
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x_vals = np.linspace(-1, 1, 10)
y_vals = np.linspace(-1, 1, 10)
X, Y = np.meshgrid(x_vals, y_vals)
Z = X**2 + Y**2
ax = Axes3D(plt.figure())
ax.plot_surface(X, Y, Z, cmap= 'bone')
