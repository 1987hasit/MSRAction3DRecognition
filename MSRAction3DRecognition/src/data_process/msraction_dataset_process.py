'''
Created on 10 Sep 2014

@author: bliang03
'''
import os
import numpy as np
from dataset_configs.msraction_dataset_config import depthFileExtension
import cv2
from utils import mat2gray
from cv2 import applyColorMap
from domain.msraction_domain import MsrAction

def loadMsrActionDepthData(depthDataPath, configFile):
    """ load msr action depth data from given path and config file  """
    
    # load data from configFile
    f = open(configFile)
    lines = f.readlines()
    f.close()
    
    msrActionList = []
    
    for line in lines:
        # remove '\n' at the end, and append file extension
        depthFile = line[:-1] + depthFileExtension
        msrAction = readMSrActionDepthSequence(os.path.join(depthDataPath, depthFile))
        msrActionList.append(msrAction)
        
    return msrActionList
    

def readMSrActionDepthSequence(depthFile):
    """ read msr action depth sequence from give depth file """
    f = open(depthFile)
    fileData = np.fromfile(f, dtype = np.int)
    f.close()
    
    # number of frames
    numFrames = fileData[0]
    numCols = fileData[1]
    numRows = fileData[2]
    sizeFrame = numCols * numRows
    
    # depth sequence
    depthSequence = []
    
    for i in xrange(numFrames):
        startIdx = 3 + i * sizeFrame
        endIdx = 3 + i * sizeFrame + sizeFrame
        
        depthData = fileData[startIdx:endIdx]
        depthData = np.resize(depthData, (numRows, numCols)) 
        depthSequence.append(depthData)

#         #show frame
#         # gray image
#         grayImg = mat2gray(depthData)
#         cv2.imshow('', grayImg)
#         
#         # color map image
#         colorMapImg = applyColorMap(grayImg, cv2.COLORMAP_JET)  
#         cv2.imshow('', colorMapImg)
#         cv2.waitKey(200)

    # construct msr action object
    filename = os.path.basename(depthFile)
    msrAction = MsrAction(filename)
    msrAction.depthSequence = depthSequence
    
    return msrAction