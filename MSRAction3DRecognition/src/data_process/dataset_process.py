'''
Created on 10 Sep 2014

@author: bliang03
'''

from dataset_configs import dataset_config
from dataset_configs.dataset_config import depthFileExtension
import os
import numpy as np
from argparse import Action

def loadDataset():
    """ load dataset"""
    depthDataPath = dataset_config.depthDataPath
    trainConfigFile = dataset_config.trainConfigFile
    testConfigFile = dataset_config.testConfigFile
    
    trainActionList = loadActions(depthDataPath, trainConfigFile)
    testActionList = loadActions(depthDataPath, testConfigFile)
    

def loadActions(depthDataPath, configFile):
    """ load depth data from given path and config file  """
    
    # load data from configFile
    f = open(configFile)
    lines = f.readlines()
    f.close()
    
    msrActionList = []
    
    for line in lines:
        # remove '\n' at the end, and append file extension
        depthFile = line[:-1] + depthFileExtension
        msrAction = readDepthFile(os.path.join(depthDataPath, depthFile))
        msrActionList.append(msrAction)
        
    return msrActionList

def readDepthFile(depthFile):
    """ read depth file"""
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
    action = Action(filename)
    action.depthSequence = depthSequence
    
    return action