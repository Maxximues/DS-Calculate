import numpy as np
import matplotlib.pyplot as plt


U = np.arange(-13.70, 12.90, 0.2)

I = np.array([-1.6, -1.1, -0.6, -0.2, 0.2, 0.7, 1.2, 1.6, 2.0, 2.5, 3.0, 3.5, 3.9, 4.4, 4.9, 4.9, 4.8, 4.7, 4.7, 4.6,\
               4.5, 4.4, 4.3, 4.2, 4.1, 4.1, 4.0, 3.9, 3.8, 3.7, 3.7, 3.6, 3.5, 3.4, 3.3, 3.3, 3.2, 3.1, 3.0, 2.9, 2.8, \
               2.8, 2.7, 2.6, 2.5, 2.4, 2.3, 2.3, 2.2, 2.1, 2.0, 1.9, 1.9, 1.8, 1.7, 1.7, 1.6, 1.5, 1.4, 1.3, \
               1.2, 1.1, 0.9, 0.8, 0.6, 0.5, 0.3, 0.1, 0.0, -0.1, -0.3, -0.4, -0.6, -0.7, -0.9, -1.0, -1.2, -1.3, -1.4, -1.5, -1.6, -1.7, -1.7,\
               -1.8, -1.9, -2.0, -2.1, -2.2, -2.3, -2.4, -2.5, -2.5, -2.6, -2.7, \
               -2.8, -2.9, -3.0, -3.0, -3.1, -3.2, -3.3, -3.4, -3.4, -3.5, -3.6, -3.7, -3.8, -3.9, -4.0, -4.0, -4.1, -4.2, -4.3, \
               -4.4, -4.4, -4.5, -4.6, -4.7, -4.6, -4.2, -3.8, -3.4, -3.0, -2.6, -2.2, \
               -1.7, -1.3, -0.9, -0.4, 0.0, 0.4, 0.8, 1.3])

avg_oum = (13.70+13.50+13.30+13.10+12.90+12.70+12.50+12.3+12.1+11.9+11.7+11.5+11.3+11.1+10.9+10.7)/(1.6+1.1+0.6+0.2+0.2+0.2+0.7+1.2+1.6+2.0+2.5+3.0+3.5+3.9+4.4+4.9+4.9)
avg_oum2 = (9.9+9.7+9.5+9.3+9.1+8.9+8.7+8.5+8.3+8.1+7.9+7.7+7.5+7.3+7.1+6.9+6.7+6.5+6.3+6.1+5.9+5.7+5.5+5.3+5.1+4.9+4.7+4.5+4.3+4.1)/(4.6+4.5+4.4+4.3+4.2+4.1+4.1+4.0+3.9+3.8+3.7+3.7+3.6+3.5+3.4+3.3+3.3+3.2+3.1+3.0+2.9+2.8+2.8+2.7+2.6+2.5+2.4+2.3+2.3+2.2)
avg_oum3 = (2.5+2.3+2.1+1.9+1.7+1.5+1.3+1.1+0.9+0.7+0.5+0.3+0.1)/(1.6+1.5+1.4+1.3+1.2+1.1+0.9+0.8+0.6+0.5+0.3+0.1+0.0)
avg_oum4 = (2.5+2.7+2.9+3.1+3.3+3.5+3.7+3.9+4.1+4.3+.5+4.7+4.9+5.1+5.3+5.5+5.7+5.9+6.1+6.3+6.5+6.7+6.9+7.1+7.3+7.5+7.7+7.9+8.1+8.3+8.5+8.7+8.9+9.1+9.3+9.5+9.7)/(1.7+1.7+1.8+1.9+2.0+2.1+2.2+2.3+2.4+2.5+2.5+2.6+2.7+2.8+2.9+3.0+3.0+3.1+3.2+3.3+3.4+3.4+3.5+3.5+3.6+3.7+3.8+3.9+4.0+4.1+4.2+4.3+4.4+4.4+4.5+4.6+4.7)
avg_oum5 = (10.10+10.3+10.5+10.7+10.9+11.1+11.3+11.5+11.7+11.9+12.1+12.3+12.5+12.7+12.9)/(4.2+3.8+3.4+3.0+2.6+2.2+1.7+1.3+0.9+0.4+0.0+0.4+0.8+0.8+1.3+1.7)
print(avg_oum5)
plt.plot(U, I)

plt.show()
