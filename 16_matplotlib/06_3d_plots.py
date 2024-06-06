import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np

x= np.arange(-5,5,0.25)
y= np.arange(-5,5,0.25)
x,y=np.meshgrid(x,y) #alle mit allem mischen
z=np.sin(np.sqrt(x**2+y**2))

fig=plt.figure()
axes1=fig.add_subplot(1,2,1, projection="3d")
surf = axes1.plot_surface(x,y,z,rstride=1, cstride=1, cmap=cm.viridis, linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=5)
axes2 = fig.add_subplot(1,2,2,projection="3d")
axes2.plot_wireframe(x,y,z, rstride=2, cstride=2)
plt.show()