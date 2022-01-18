import numpy as np
import matplotlib.pyplot as plt
import glob, os
import sys

def plot_polar(data, max_value, step=180, name="", model="", position=""):
    print(model," ",position , " ", name,": "  ,sum(data))
    ttl = name+'\n'+str(int(sum(data)))+"/"+str(180*32) +" ( "+ str(round((sum(data)/(180*32))*100,2))+"% )"
    
    plt.figure(figsize=(10, 6))
    
    data = data.tolist()
    data.append(data[0])
    ax = plt.subplot(polar=True)
    
    if(max_value != 0):
        ax.set_ylim(0, max_value)
        ax.set_yticks(np.arange(0, max_value, step))
    
    ax.set_theta_zero_location("N")
    ax.set_theta_direction(-1)
    ax.set_rgrids([5, 10, 15, 20, 25, 30])
    ax.set_title(ttl)
    degree_sign = u'\N{DEGREE SIGN}'
    theta = np.linspace(2*np.pi/len(data), 2 * np.pi, len(data))
    width = (2*np.pi / len(theta))*0.9
    angle = [str(a * 2) if (a * 2) %10 == 0 else "" for a in list(range(180))]
    lines, labels = plt.thetagrids(range(0, 360, int(360/len(angle))), (angle))
    plt.xticks(np.arange(0,2 * np.pi,  np.pi/4 ))
    ax.set_xticklabels(['0'+ degree_sign, '45'+ degree_sign, '90'+ degree_sign, '135'+ degree_sign, '180'+ degree_sign, '225'+ degree_sign, '270'+ degree_sign, '315'+ degree_sign])
    #plt.plot(theta, data, linewidth=0)
    #plt.fill(theta, data, alpha=0.4)
    ax.bar(theta, data, width=width, bottom=0, alpha=0.4, linewidth=0)
    ax.set_ylim ((0, 32))
    #plt.title(title)
    #plt.show()
    plt.savefig('/home/yaesop/syn_result/'+model+'_'+position+'_polar_'+name+'.png')


    
def get_iou(bb1, bb2):
    """
    Calculate the Intersection over Union (IoU) of two bounding boxes.

    Parameters
    ----------
    bb1 : dict
        Keys: {'x1', 'x2', 'y1', 'y2'}
        The (x1, y1) position is at the top left corner,
        the (x2, y2) position is at the bottom right corner
    bb2 : dict
        Keys: {'x1', 'x2', 'y1', 'y2'}
        The (x, y) position is at the top left corner,
        the (x2, y2) position is at the bottom right corner

    Returns
    -------
    float
        in [0, 1]
    """
    #assert bb1['x1'] < bb1['x2']
    #assert bb1['y1'] < bb1['y2']
    #assert bb2['x1'] < bb2['x2']
    #assert bb2['y1'] < bb2['y2']
    if bb1['x1']==0.0 and bb1['x2']==0.0:
        return 0
    if bb1['y1']==0.0 and bb1['y2']==0.0:
        return 0
    # determine the coordinates of the intersection rectangle
    x_left = max(bb1['x1'], bb2['x1'])
    y_top = max(bb1['y1'], bb2['y1'])
    x_right = min(bb1['x2'], bb2['x2'])
    y_bottom = min(bb1['y2'], bb2['y2'])

    #if x_right < x_left or y_bottom < y_top:
    #    return 0.0

    # The intersection of two axis-aligned bounding boxes is always an
    # axis-aligned bounding box
    intersection_area = abs(x_right - x_left) * abs(y_bottom - y_top)

    # compute the area of both AABBs
    bb1_area = abs(bb1['x2'] - bb1['x1']) * abs(bb1['y2'] - bb1['y1'])
    bb2_area = abs(bb2['x2'] - bb2['x1']) * abs(bb2['y2'] - bb2['y1'])

    # compute the intersection over union by taking the intersection
    # area and dividing it by the sum of prediction + ground-truth
    # areas - the interesection area
    if float(bb1_area + bb2_area - intersection_area)==0:
        return 0
    
    iou = intersection_area / float(bb1_area + bb2_area - intersection_area)

    return iou

# Opening JSON file
test = np.zeros(180)
imgs = glob.glob('../Object-Detection-Metrics/detections/*.txt')
gt = glob.glob('../Object-Detection-Metrics/groundtruths/*.txt')
#print(len(imgs), len(gt))
imgs.sort()
gt.sort()

#xywh -> 1,2,3,4
k =0
for i in range(len(imgs)):
    #print(imgs[i])
    if True:
        flag = True
        f = open(imgs[i],"r")
        k= k+1
        f_gt_file = open(gt[i], "r")
        f_gt = f_gt_file.readline()
        b_gt = { \
            'x1' : float(f_gt.split(" ")[1])-float(f_gt.split(" ")[3])/2, \
            'x2' : float(f_gt.split(" ")[1])+float(f_gt.split(" ")[3])/2, \
            'y1' : float(f_gt.split(" ")[2])-float(f_gt.split(" ")[4])/2, \
            'y2' : float(f_gt.split(" ")[2])+float(f_gt.split(" ")[4])/2 \
        }
        
        for fLine in f:

            f_ft = { \
                'x1' : float(fLine.split(" ")[2])-float(fLine.split(" ")[4])/2, \
                'x2' : float(fLine.split(" ")[2])+float(fLine.split(" ")[4])/2, \
                'y1' : float(fLine.split(" ")[3])-float(fLine.split(" ")[5])/2, \
                'y2' : float(fLine.split(" ")[3])+float(fLine.split(" ")[5])/2 \
            }
            
            if get_iou(b_gt, f_ft)>0.5  and flag==True:
                angle = int(int(imgs[i].split('/')[3].split('.')[0].split("_")[-3])/2)
                #print(angle)
                test[angle] = test[angle]+1
                flag= False

#print(test)
#print(k)
plot_polar(test, max_value=32, step=15, name= "( H:" + sys.argv[1] +"  R:" + sys.argv[2]+" )" , model =sys.argv[3], position = sys.argv[4] )



