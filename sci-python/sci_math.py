#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 20:23:36 2018

@author: linuxhan
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def F(y, t):
    dy = [0, 0]
    dy[0] = y[1]
    dy[1] = -y[0]
    return dy


t_min = 0; t_max = 10; dt = 0.1
t = np.arange(t_min, t_max+dt, dt)

initial_condition = [(1.0, 0.0), (0.0, 1.0)]

plt.figure()
for y0 in initial_condition:
    y = odeint(F, y0, t)
    plt.plot(t, y[:, 0], linewidth=2)   

skip = 5
t_test = t[::skip]
plt.plot(t_test, np.cos(t_test), 'bo')
plt.plot(t_test, np.sin(t_test), 'go')
