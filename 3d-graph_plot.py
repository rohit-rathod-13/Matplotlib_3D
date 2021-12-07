#3D Graph Plot
#importing the mplot3d toolkit, included with the main Matplotlib installation
from mpl_toolkits import mplot3d

%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

# a three-dimensional axes can be created by passing the 
#keyword projection='3d' to any of the normal axes creation routines
fig = plt.figure()
ax = plt.axes(projection='3d')
