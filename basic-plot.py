# 10. Write a program that displays a plot of the functions x, x2 and 2x in the range [0, 4].

import matplotlib.pyplot as plt 
import numpy as np


## plot 1 data
x1 = np.arange(0,4)
y1 = x1

## plot 2 data
x2 = np.arange(0,4)
y2 = x2*2

## plot 3 data
x2 = np.arange(0,4)
y2 = 2*x

## plotting them
plt.plot(x1, y1)
plt.plot(x2,y2)

## setting the limits on the x-axis and y-axis
plt.xlim(0,4)
plt.ylim(0,4)

plt.show()

#reference https://stepik.org/lesson/44680/step/1?unit=22723