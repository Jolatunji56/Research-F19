import readcol
import matplotlib.pyplot as plt

file = readcol.readcol('times.list')
time = file[:,0]
redshift = file[:,1]

plt.plot(time,redshift)
plt.tick_params(axis="x",labelcolor="r")
plt.xlabel("Time")
plt.ylabel("Redshift")
plt.legend()
plt.show()
