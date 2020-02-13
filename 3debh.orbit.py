import readcol
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')

ebh = readcol.readcol('/home/shared/data/h148/eatenbh.orbit')

Unit_conversion = 50000.0

X = ebh[:,4] * Unit_conversion
Y = ebh[:,5] * Unit_conversion
Z = ebh[:,6] * Unit_conversion

ax1.plot(X,Y,Z)
ax1.set_xlabel('x axis')
ax1.set_ylabel('y axis')
ax1.set_zlabel('z axis')

plt.show()

