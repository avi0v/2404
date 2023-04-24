# pure memory
from matplotlib import pyplot as plt 
import numpy as np 
import pandas as pd

#data
a=np.arange(1,11)
b=np.random.uniform(11,15,10)

#seting the plot
fig=plt.figure(figsize=(5,5))

#feeding data
plt.plot(a,b)

#Labeling
plt.xlim(0,12)
plt.ylim(11,16)
plt.xlabel("X AXIS")
plt.ylabel('Y AXIS')
plt.title("FIG 1",size=10)
plt.suptitle("graph 1",size=15)

plt.show()