import os
import numpy as np
import matplotlib.pyplot as plt

plt.figure()
data = np.loadtxt("0.1ex.dat")
plt.plot(data[:,0], data[:,1])
data = np.loadtxt("0.01ex.dat")
plt.plot(data[:,0], data[:,1])
data = np.loadtxt("1ex.dat")
plt.plot(data[:,0], data[:,1])
plt.axis('square')
#plt.xlim([-25, 25])
#plt.ylim([-25, 25])
plt.xlabel('x')
plt.ylabel('y')
plt.savefig("primerorden.png")