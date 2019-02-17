#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 16:32:14 2019

@author: linuxhan
"""
import numpy as np
import matplotlib.pyplot as plt

courses = ['python', 'Mental ealth education','collge english', 'Electrotechnics', 'ACCESS', 'Physics', 'Physics experiment', 'Math-pythsics methods', 'PE', 'Linear algebra', 'History']

scores = [90, 90, 89, 93, 94, 95, 73, 94, 85, 95, 87]

datalength = len(scores)

# angles数组把圆括等分为datalength份
angles = np.linspace(0, 2*np.pi, datalength, endpoint=False)
scores.append(scores[0])
angles = np.append(angles, angles[0])

# 绘制雷达图
plt.polar(angles, scores, 'rv--', linewidth=2)

# 设置角度网络标签
plt.thetagrids(angles*180/np.pi, courses)

# 填充雷达内部
plt.fill(angles, scores, facecolor='r', alpha=0.6)
plt.show()
