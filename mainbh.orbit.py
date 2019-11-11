import readcol
import matplotlib.pyplot as plt
ebh = readcol.readcol('/home/shared/data/h148/eatenbh.orbit')
file = readcol.readcol('/home/shared/data/h148/mainbh.orbit')
X = file[:,4] 
x = ebh[:,4]
Y = file[:,5]
y = ebh[:,5]

plt.plot(X,Y)
plt.plot(x,y)
plt.tick_params(axis="x",labelcolor="g")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
