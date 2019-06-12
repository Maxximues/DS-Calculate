#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 16:54:07 2019

@author: linuxhan
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()  # 定义新的三维坐标轴
ax3 = Axes3D(fig)

# 定义三维数据
xx = np.arange(0, 49, 7)
yy = np.arange(0, 49, 7)
X, Y = np.meshgrid(xx, yy)

Z = np.arange([1.026, 1.026, 1.025, 1.025, 1.024, 1.021, 1.015,
               1.026, 1.026, 1.026, 1.024, 1.025, 1.023, 1.016,
               1.025, 1.025, 1.024, 1.024, 1.023, 1.021, 1.017,
               1.026, 1.026, 1.027, 1.027, 1.028, 1.029, 1.029,
               1.022, 1.024, 1.027, 1.028, 1.030, 1.028, 1.024,
               1.022, 1.023, 1.025, 1.027, 1.030, 1.033, 1.035,
               1.021, 1.022, 1.025, 1.029, 1.033, 1.037, 1.040
               ])

# 作图
ax3.plot_surface(X, Y, Z, cmap='rainbow')
# ax3.contour(X,Y,Z, zdim='z',offset=-2，cmap='rainbow)   #等高线图，要设置offset，为Z的最小值
plt.show()
