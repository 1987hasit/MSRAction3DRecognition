'''
Created on 10 Sep 2014

@author: bliang03
'''
import numpy as np
from scipy.misc.pilutil import bytescale  # @UnresolvedImport
import math

def mat2gray(mat):
    """ convert matrix to gray image (0-255) """
    mat = mat.astype(np.uint16)
    depthGray = bytescale(mat)
    
    return depthGray


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

def getWorldCoordinates(width, height, depthData):
    """ get world coordinates from  """
    fx = 525.0  # focal length x
    fy = 525.0  # focal length y
    cx = 319.5  # optical center x
    cy = 239.5  # optical center y
    
    height, width = depthData.size()
    
    xwList = []
    ywList = []
    zwList = []
    
    for v in xrange(height):
        for u in xrange(width):
            zw = depthData(v,u);
            xw = (u - cx) * zw / fx
            yw = (v - cy) * zw / fy
            
            xwList.append(xw)
            ywList.append(yw)
            zwList.append(zw)
            
    return xwList, ywList, zwList
    