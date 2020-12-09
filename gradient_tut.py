import scipy.ndimage as nd
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import sys

x = np.arange(0, 10)
y = np.arange(0, 10)
X, Y = np.meshgrid(x, y)
Z = np.sin(X-1) + np.cos(Y-1)
#
Z2 = nd.laplace(Z, output=None, mode='wrap')
Z2[0,]=Z2[1,]
Z2[-1,]=Z2[-2,]
Z2[:,0]=Z2[:,1]
Z2[:,-1]=Z2[:,-2]
#
grady, gradx = np.gradient(Z, 1, 1)
#
sys.exit()
fig = plt.figure()
cs = plt.contourf(X, Y, gradx, cmap=cm.PuBu_r)
cbar = fig.colorbar(cs)
plt.show()
#
