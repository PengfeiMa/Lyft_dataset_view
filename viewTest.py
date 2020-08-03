# -*- coding:utf-8 -*-
import cv2
from math import *
import numpy as np
import time,math
import os
import json
from nuscenes.nuscenes import NuScenes
from nuscenes.utils.geometry_utils import view_points

nusc = NuScenes(version='v1.02-train', dataroot='/Users/pengfeima/Desktop/Lyft/v1.02-train', verbose=False)


def draw_projected_box3d(image, qs, color=(255,0,255), thickness=2):
    ''' Draw 3d bounding box in image
        qs: (8,3) array of vertices for the 3d box in following order:
            1 -------- 0
           /|         /|
          2 -------- 3 .
          | |        | |
          . 5 -------- 4
          |/         |/
          6 -------- 7
    '''
    #qs = qs.astype(np.int32)
    for k in range(0,4):
       # Ref: http://docs.enthought.com/mayavi/mayavi/auto/mlab_helper_functions.html
        i,j=k,(k+1)%4
       # use LINE_AA for opencv3
        p1, p2 = (qs[i, 0], qs[i, 1]), (qs[j, 0], qs[j, 1])
        cv2.line(image, (int(p1[0]),int(p1[1])), (int(p2[0]),int(p2[1])), color, thickness)


        i,j=k+4,(k+1)%4 + 4
        p1, p2 = (qs[i, 0], qs[i, 1]), (qs[j, 0], qs[j, 1])
        cv2.line(image, (int(p1[0]), int(p1[1])), (int(p2[0]), int(p2[1])), color, thickness)

        i,j=k,k+4
        p1, p2 = (qs[i, 0], qs[i, 1]), (qs[j, 0], qs[j, 1])
        cv2.line(image, (int(p1[0]), int(p1[1])), (int(p2[0]), int(p2[1])), color, thickness)

    return image


# point cloud files 18634
for sample in nusc.sample: 
    data_path, boxes, camera_intrinsic = nusc.get_sample_data(sample['data']['CAM_FRONT'])
    print(data_path)
    imgSrc = cv2.imread(data_path)
    for box in boxes:        
        corners = view_points(box.corners(), camera_intrinsic, True)[:2, :]
        draw_projected_box3d(imgSrc, corners.T)
        #print(corners)
    cv2.imshow("img", imgSrc)
    cv2.waitKey(0)
    

'''
data_path = '/Users/pengfeima/Desktop/Lyft/v1.02-train/images/host-a011_cam0_1232752793451142006.jpeg'
imgSrc = cv2.imread(data_path)
coners = [[525.80343502, 565.51836037, 566.38930843, 526.65233718, 511.35076501,
  556.15155187, 557.12845825, 512.29961551],
 [535.92502909, 534.81009855, 567.08649073, 568.18968932, 536.64177939,
  535.38420589, 571.80186123, 573.04449972]]
coners = np.array(coners)
draw_projected_box3d(imgSrc, coners.T)
cv2.imshow("img", imgSrc)
cv2.waitKey(0)
'''