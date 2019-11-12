import os
import numpy as np
import matplotlib.pyplot as plt

plt.figure()
plt.subplot(1,2,1)
data = np.loadtxt("0.1ex.dat")
plt.plot(data[:,0], data[:,1], label="delta=0.1")
data = np.loadtxt("0.01ex.dat")
plt.plot(data[:,0], data[:,1], label="delta=0.01")
data = np.loadtxt("1ex.dat")
plt.plot(data[:,0], data[:,1], label="delta=1")
plt.axis('square')
plt.legend()
plt.title("EXPLICITO")
#plt.ylim([0, 5])
plt.xlabel('x')
plt.ylabel('y')
plt.savefig("primerorden.png")