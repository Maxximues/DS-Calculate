#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 10:49:58 2018

@author: linuxhan
"""
import numpy as np
import matplotlib.pyplot as plt

data = np.random.random(500)
#plt.hist(data)
counts, bin_edges, _ = plt.hist(data)
bin_size = bin_edges[1] -bin_edges[0]
new_widths = bin_size * counts / counts.max()
plt.bar(bin_edges[:-1], counts, width=new_widths, color=['r','g','b'])
