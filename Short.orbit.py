import readcol
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3d

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')

file = readcol.readcol('short.orbit')


Unit_conversion = 50000.0
x = file[:,4] * Unit_conversion
y = file[:,5] * Unit_conversion
z = file[:,6] * Unit_conversion

ax1.plot(x,y,z)
ax1.set_xlabel('x axis')
ax1.set_ylabel('y axis')
ax1.set_zlabel('z axis')

plt.show()

