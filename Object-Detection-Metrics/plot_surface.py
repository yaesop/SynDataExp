import os, sys
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib.colors as colors
import matplotlib as mpl

#x, y = np.random.rand(2, 100) * 4
#hist, xedges, yedges = np.histogram2d(x, y, bins=15, range=[[5, 80], [5, 80]])

position = sys.argv[1]
#######nano result #####
result_n = []
text_file = open("/home/yaesop/syn_result/output_n_"+position+"_"+"1"+".txt", "r")
lines = text_file.readlines()
k = 0
for line in lines:
    if k%2 ==1:
        tmp = line.split(" ")[1][:-1]
        result_n.append(float(tmp))
    k=k+1
result_n = np.array(result_n)
for name in range(2,5):
    text_file = open("/home/yaesop/syn_result/output_n_"+position+"_"+str(name)+".txt", "r")
    lines = text_file.readlines()
    k = 0
    kk = 0
    for line in lines:
        if k%2 ==1:
            tmp = line.split(" ")[1][:-1]
            result_n[kk] = result_n[kk] + float(tmp)
            kk=kk+1
        k=k+1
print(result_n)

for r in range(len(result_n)):
    result_n[r] = result_n[r]/4

#######small result #####
result_s = []
text_file = open("/home/yaesop/syn_result/output_s_"+position+"_"+"1"+".txt", "r")
lines = text_file.readlines()
k = 0
for line in lines:
    if k%2 ==1:
        tmp = line.split(" ")[1][:-1]
        result_s.append(float(tmp))
    k=k+1
result_s = np.array(result_s, dtype=np.float)
for name in range(2,5):
    text_file = open("/home/yaesop/syn_result/output_s_"+position+"_"+str(name)+".txt", "r")
    lines = text_file.readlines()
    k = 0
    kk =0
    for line in lines:
        if k%2 ==1:
            tmp = line.split(" ")[1][:-1]
            result_s[kk] = result_s[kk] + float(tmp)
            kk=kk+1
        k=k+1
for r in range(len(result_s)):
    result_s[r] = result_s[r]/4

#######medim result #####
result_m = []
text_file = open("/home/yaesop/syn_result/output_m_"+position+"_"+"1"+".txt", "r")
lines = text_file.readlines()
k = 0
for line in lines:
    if k%2 ==1:
        tmp = line.split(" ")[1][:-1]
        result_m.append(float(tmp))
    k=k+1
result_m = np.array(result_m, dtype=np.float)
for name in range(2,5):
    text_file = open("/home/yaesop/syn_result/output_m_"+position+"_"+str(name)+".txt", "r")
    lines = text_file.readlines()
    k = 0
    kk =0
    for line in lines:
        if k%2 ==1:
            tmp = line.split(" ")[1][:-1]
            result_m[kk] = result_m[kk] + float(tmp)
            kk = kk+1
        k=k+1
for r in range(len(result_m)):
    result_m[r] = result_m[r]/4

#######large result #####
result_l = []
text_file = open("/home/yaesop/syn_result/output_l_"+position+"_"+"1"+".txt", "r")
lines = text_file.readlines()
k = 0

for line in lines:
    if k%2 ==1:
        tmp = line.split(" ")[1][:-1]
        result_l.append(float(tmp))
       
    k=k+1
result_l = np.array(result_l, dtype=np.float)
for name in range(2,5):
    text_file = open("/home/yaesop/syn_result/output_l_"+position+"_"+str(name)+".txt", "r")
    lines = text_file.readlines()
    k = 0
    kk =0
    for line in lines:
        if k%2 ==1:
            tmp = line.split(" ")[1][:-1]
            result_l[kk] = result_l[kk] + float(tmp)
            kk = kk+1
        k=k+1
for r in range(len(result_l)):
    result_l[r] = result_l[r]/4

#######xlarge result #####
result_x = []
text_file = open("/home/yaesop/syn_result/output_x_"+position+"_"+"1"+".txt", "r")
lines = text_file.readlines()
k = 0
for line in lines:
    if k%2 ==1:
        tmp = line.split(" ")[1][:-1]
        result_x.append(float(tmp))
    k=k+1
result_x = np.array(result_x, dtype=np.float)
for name in range(2,5):
    text_file = open("/home/yaesop/syn_result/output_x_"+position+"_"+str(name)+".txt", "r")
    lines = text_file.readlines()
    k = 0
    kk = 0
    for line in lines:
        if k%2 ==1:
            tmp = line.split(" ")[1][:-1]
            result_x[kk] = result_x[kk] + float(tmp)
            kk = kk+1
        k=k+1
for r in range(len(result_x)):
    result_x[r] = result_x[r]/4


fig=plt.figure(figsize=(3, 3), dpi=180)
ax1=fig.add_subplot(111, projection='3d')

ylabels = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80])

#xlabels = np.flip(xlabels)
ypos = np.arange(ylabels.shape[0])
xlabels = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80])
#xlabels = np.flip(ylabels)
xpos = np.arange(xlabels.shape[0])

xposM, yposM = np.meshgrid(xpos, ypos, copy=False)

zpos=result_n
zpos = zpos.ravel()

dx=0.3
dy=0.3
dz=zpos
print(len(result_n))
ax1.w_xaxis.set_ticks(xpos + dx/5.)
ax1.w_xaxis.set_ticklabels(xlabels, fontsize = 6.5)

ax1.w_yaxis.set_ticks(ypos + dy/5.)
ax1.w_yaxis.set_ticklabels(ylabels, fontsize = 6.5)
ax1.set_title("")

#values = np.linspace(0.2, 1.,zpos.ravel().shape[0])
result_n = np.reshape(result_n,(16,16))
result_s = np.reshape(result_s,(16,16))
result_m = np.reshape(result_m,(16,16))
result_l = np.reshape(result_l,(16,16))
result_x = np.reshape(result_x,(16,16))

print(result_n)
surface_n = ax1.plot_surface(xposM, yposM, result_n,  rstride=1, cstride=1,alpha=0.5, color='violet', label = "yolov5-nano")
surface_s =ax1.plot_surface(xposM, yposM, result_s,  rstride=1, cstride=1,alpha=0.5 ,color='c', label = "yolov5-small")
surface_m =ax1.plot_surface(xposM, yposM, result_m,  rstride=1, cstride=1 ,alpha=0.6, color='green', label = "yolov5-medium")
surface_l =ax1.plot_surface(xposM, yposM, result_l, rstride=1, cstride=1 ,alpha=0.6, color='blue', label = "yolov5-large")
surface_x =ax1.plot_surface(xposM, yposM, result_x, rstride=1, cstride=1 ,alpha=0.6, color='red', label = "yolov5-xlarge")


surface_n._facecolors2d=surface_n._facecolor3d
surface_n._edgecolors2d=surface_n._edgecolor3d

surface_s._facecolors2d=surface_s._facecolor3d
surface_s._edgecolors2d=surface_s._edgecolor3d

surface_m._facecolors2d=surface_m._facecolor3d
surface_m._edgecolors2d=surface_m._edgecolor3d

surface_l._facecolors2d=surface_l._facecolor3d
surface_l._edgecolors2d=surface_l._edgecolor3d

surface_x._facecolors2d=surface_x._facecolor3d
surface_x._edgecolors2d=surface_x._edgecolor3d



ax1.legend(loc='upper right',bbox_to_anchor=(1, 1), fontsize = 7)
ax1.set_xlabel('Height')
ax1.set_ylabel('Radius')

ax1.set_zlim3d(0,100)


print(sum(sum(result_n))/256)
print(sum(sum(result_s))/256)
print(sum(sum(result_m))/256)
print(sum(sum(result_l))/256)
print(sum(sum(result_x))/256)
#ax1.view_init(0, 0)
#ax1.set_box_aspect

plt.savefig('/home/yaesop/syn_result/surface_'+position+'.png')

plt.show()
