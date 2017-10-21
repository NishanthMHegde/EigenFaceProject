import numpy as np
import matplotlib.pyplot as plt
t = [0,7,13,19,25,31,37,43]
s =[0.682,0.15125,0.233,0.306,0.347,0.4,0.5,0.51]
y=[0.61,0.593,0.448,0.417,0.363,0.334,0.254]
plt.plot(t,s,'r')
plt.axis([0,50,0,1])
plt.xlabel("Threshold")
plt.ylabel("Succesful Face Match")
plt.show()
