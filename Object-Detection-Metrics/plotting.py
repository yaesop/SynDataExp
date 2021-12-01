
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm

#x, y = np.random.rand(2, 100) * 4
#hist, xedges, yedges = np.histogram2d(x, y, bins=15, range=[[5, 80], [5, 80]])

result = []
text_file = open("output.txt", "r")
lines = text_file.readlines()
k = 0
for line in lines:
    if k%2 ==1:
        tmp = line.split(" ")[1][:-1]
        result.append(float(tmp))
    k=k+1
result = np.array(result, dtype=np.int)

fig=plt.figure(figsize=(5, 5), dpi=150)
ax1=fig.add_subplot(111, projection='3d')

ylabels = np.array([5, 10, 15, 20, 25, 30])

#xlabels = np.flip(xlabels)
ypos = np.arange(ylabels.shape[0])
xlabels = np.array([ 5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
#xlabels = np.flip(ylabels)
xpos = np.arange(xlabels.shape[0])

xposM, yposM = np.meshgrid(xpos, ypos, copy=False)

zpos=result
zpos = zpos.ravel()

dx=0.5
dy=0.5
dz=zpos

ax1.w_xaxis.set_ticks(xpos + dx/2.)
ax1.w_xaxis.set_ticklabels(xlabels)

ax1.w_yaxis.set_ticks(ypos + dy/2.)
ax1.w_yaxis.set_ticklabels(ylabels)

values = np.linspace(0.5, 1., xposM.ravel().shape[0])
colors = cm.rainbow(values)
ax1.bar3d(xposM.ravel(), yposM.ravel(), dz*0, dx, dy, dz, color=colors)
ax1.set_xlabel('Altitude')
ax1.set_ylabel('Radius')
ax1.set_zlabel('AP')
plt.show()
