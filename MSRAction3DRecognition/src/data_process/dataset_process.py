'''
Created on 10 Sep 2014

@author: bliang03
'''

from dataset_configs.dataset_config import depthFileExtension, depthDataPath, \
    trainConfigFile, testConfigFile, loadedDepthDataPath,\
    loadedDepthDataFileExtension
import os
import numpy as np
from domain.action_domain import Action
import pickle
from cv2 import applyColorMap
import cv2
from utils import mat2gray


def loadDepthData():
    """Load dpeth data and save to file """
    print "Loading depth data...\n"
    
    depthFiles = os.listdir(depthDataPath)
    for depthFile in depthFiles:
        print depthFile
        
        depthSequence = readDepthFile(os.path.join(depthDataPath, depthFile))
        saveFileName = os.path.splitext(depthFile)[0] + ".pkl"
        ofile = open(os.path.join(loadedDepthDataPath, saveFileName), 'w')
        pickle.dump(depthSequence, ofile)
        ofile.close()
        
    print "Done!"
    

def loadTrainDataset():
    """ load train dataset"""
    trainActionList = loadActions(loadedDepthDataPath, trainConfigFile)
    
    return trainActionList


def loadTestDataset():
    """ load test dataset"""
    # otherwise load from the original dataset, and then save to files
    testActionList = loadActions(loadedDepthDataPath, testConfigFile)
        
    return testActionList


def loadActions(loadedDepthDataPath, configFile):
    """ load depth data from given path and config file  """
    
    # load data from configFile
    f = open(configFile)
    lines = f.readlines()
    f.close()
    
    actionList = []
    
    for line in lines:
        # remove '\n' at the end, and append file extension
        filename = line[:-1] + loadedDepthDataFileExtension
        
        # construct action object
        action = Action(filename)
        action.depthSequenceFile = os.path.join(loadedDepthDataPath, filename)
        actionList.append(action)
        
        # print info
        print "%s loaded." % filename
        
    return actionList


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

        #show frame
#         # gray image
#         grayImg = mat2gray(depthData)
#         cv2.imshow('', grayImg)
#         cv2.waitKey(150)
#         
#         # color map image
#         grayImg = mat2gray(depthData)
#         colorMapImg = applyColorMap(grayImg, cv2.COLORMAP_JET)  
#         cv2.imshow('', colorMapImg)
#         cv2.waitKey(150)

    return depthSequence