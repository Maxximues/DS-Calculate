import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize


def func(x, A, B):
    return A*x+B

def plot_test():
    plt.figure()
    #points
    x0 = [0.5, 1.0, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
    y0 = [14.2, 28.15, 42.25, 56.35, 70.38, 84.48, 98.45, 112.58, 126.58, 140.7]

    #print points
    plt.scatter(x0[:], y0[:], 25 , "red")
    #line 
    A1, B1 = optimize.curve_fit(func, x0, y0)[0]
    x1 = np.arange(0.5, 6, 0.5)
    y1 = A1*x1 +B1
    plt.plot(x1, y1, "blue")
    plt.show()

plot_test()
