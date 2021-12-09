import os, sys
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib.colors as colors

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

fig=plt.figure(figsize=(6, 6), dpi=180)
ax1=fig.add_subplot(111, projection='3d')

ylabels = np.array([5, 10, 15, 20, 25, 30])

#xlabels = np.flip(xlabels)
ypos = np.arange(ylabels.shape[0])
xlabels = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
#xlabels = np.flip(ylabels)
xpos = np.arange(xlabels.shape[0])

xposM, yposM = np.meshgrid(xpos, ypos, copy=False)

zpos=result
zpos = zpos.ravel()

dx=0.3
dy=0.25
dz=zpos

ax1.w_xaxis.set_ticks(xpos + dx/5.)
ax1.w_xaxis.set_ticklabels(xlabels)

ax1.w_yaxis.set_ticks(ypos + dy/5.)
ax1.w_yaxis.set_ticklabels(ylabels)
ax1.set_title("")

#values = np.linspace(0.2, 1.,zpos.ravel().shape[0])

colors_val = cm.jet_r(zpos/max(zpos))

ax1.bar3d(xposM.ravel(), yposM.ravel(), dz*0, dx, dy, dz, color=colors_val)
ax1.set_xlabel('Height')
ax1.set_ylabel('Radius')
ax1.set_zlim3d(0,100)
#ax1.view_init(0, 0)
#ax1.set_box_aspect
colourMap = plt.cm.ScalarMappable(cmap=plt.cm.jet_r)
colourMap.set_array(zpos)
colourMap.set_clim(0,100)
fig.colorbar(colourMap, shrink=0.4)
name = sys.argv[1]
plt.savefig('nano_standing_'+name+'.png')

#plt.show()
