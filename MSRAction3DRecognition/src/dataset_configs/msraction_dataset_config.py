'''
Created on 10 Sep 2014

@author: bliang03
'''

import os

## Data dir
datasetPath = "C:/MSRAction_dataset/"
depthDataPath = os.path.join(datasetPath, "depth")
skeletonDataPath = os.path.join(datasetPath, "skeleton")
mappedSkeletonDataPath = os.path.join(datasetPath, "mapped_skeleton")
datasetConfigPath = "./dataset_configs/msraction_configs/"

depthFileExtension = "_sdepth.bin"
skeletonFileExtension = "_skeleton3D.txt"
mappedSkeletonFileExtension = "_skeleton.txt"


## Experiment settings
# "t1", "t2", "t3" (cross subject test)
testType = "t3"

# "as1", "as2", "as3"    
subsetType = "as1" 

# split train test file
tmpTrainConfigFile = "%s_%s_train.txt" %(testType, subsetType)
tmpTestConfigFile = "%s_%s_test.txt" %(testType, subsetType)

trainConfigFile = os.path.join(datasetConfigPath, tmpTrainConfigFile)
testConfigFile = os.path.join(datasetConfigPath, tmpTestConfigFile)

actionCateogory = ['a01', 'a02', 'a03', 'a04', 'a05', 
                   'a06', 'a07', 'a08', 'a09', 'a10',
                   'a11', 'a12', 'a13', 'a14', 'a15',
                   'a16', 'a17', 'a18', 'a19', 'a20']


