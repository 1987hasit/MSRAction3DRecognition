'''
Created on 10 Sep 2014

@author: bliang03
'''
import numpy as np
from scipy.misc.pilutil import bytescale  # @UnresolvedImport
import math
import cv2
from cv2 import applyColorMap

def mat2gray(mat):
    """ convert matrix to gray image (0-255) """
#     mat = mat.astype(np.uint16)
#     depthGray = bytescale(mat)
    minItem = mat.min()
    maxItem = mat.max()
    
    grayImg = mat.copy()
    if (maxItem - minItem) != 0:
        tmpMat = (mat - minItem) / float(maxItem - minItem) # scale to [0-1]
        grayImg = tmpMat * 255
        grayImg = grayImg.astype(np.uint8)
    
    return grayImg


def getEstimatedKinectFocalLength(width, height):
    """ get kinect focal length from given width and height of depth map """
    verticalAngle = 43
    horizontalAngle = 57
    
    # focal length along x direction
    # fx = (w/2) / tan(hori_angle / 2)
    fx = (width / 2.0) / math.tan(math.radians(horizontalAngle/2.0))
    
    # focal length along y direction
    # fy = (h/2) / tan(vertical_angle / 2)
    fy = (height / 2.0) / math.tan(math.radians(verticalAngle/2.0))
    
    return fx, fy
