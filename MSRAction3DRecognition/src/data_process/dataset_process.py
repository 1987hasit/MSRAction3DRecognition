'''
Created on 10 Sep 2014

@author: bliang03
'''

from dataset_configs import msraction_dataset_config
from data_process.msraction_dataset_process import loadMsrActionDepthData

def loadDataset(currentDataset):
    """ load dataset"""
    if currentDataset == 'MSRAction3D':
        depthDataPath = msraction_dataset_config.depthDataPath
        trainConfigFile = msraction_dataset_config.trainConfigFile
        testConfigFile = msraction_dataset_config.testConfigFile
        
        trainMsrActionList = loadMsrActionDepthData(depthDataPath, trainConfigFile)
        testMsrActionList = loadMsrActionDepthData(depthDataPath, testConfigFile)
        
        for trainAction in trainA
        
    else:
        pass

