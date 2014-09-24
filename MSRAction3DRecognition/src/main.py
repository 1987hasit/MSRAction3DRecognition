'''
Created on 10 Sep 2014

@author: bliang03
'''

from data_process.dataset_process import loadTrainDataset, loadDepthData
import pickle
from point_cloud.points_utils import getProjectionImages
    
from utils import mat2gray
from representation.motion_history import calWinDepthMHIList,\
    cropAndResizeImageList

def main():
    ## flags
    isLoadDepthData = False
    
    ## sliding window
    winSize = 5
    winStep = 3
    
    ## load depth data and save to file
    if isLoadDepthData:
        loadDepthData()
    
    ## load dataset
    trainActionList = loadTrainDataset()
    
    ## process for training
    for trainAction in trainActionList:
        ifile = open(trainAction.depthSequenceFile, 'r')
        depthSequence = pickle.load(ifile)
        ifile.close()
        
        xoyImgList = []
        xozImgList = []
        yozImgList = []
        
        # get xoy, xoz and yoz images from depth data
        for depthData in depthSequence:
#             # depth image visualization
#             # color map image
#             grayImg = mat2gray(depthData)
#             colorMapImg = applyColorMap(grayImg, cv2.COLORMAP_JET)  
#             cv2.imshow('', colorMapImg)
#             cv2.waitKey()
            
#             # point cloud visualization
#             points = getWorldCoordinates(depthData)
#             visualizePointCloud(points)
            
            xoyImg = mat2gray(depthData)
            xozImg, yozImg = getProjectionImages(depthData)
            
            xoyImgList.append(xoyImg)
            xozImgList.append(xozImg)
            yozImgList.append(yozImg)
        
        trainAction.xoyImgList = xoyImgList
        trainAction.xozImgList = xozImgList
        trainAction.yozImgList = yozImgList
        
        # windowed DMHI
        xoyDmhiList = calWinDepthMHIList(trainAction.xoyImgList, winSize, winStep)
        xozDmhiList = calWinDepthMHIList(trainAction.xozImgList, winSize, winStep)
        yozDmhiList = calWinDepthMHIList(trainAction.yozImgList, winSize, winStep)
        
        # post processing, crop and resize
        postXoyDmhiList = cropAndResizeImageList(xoyDmhiList)
        postXozDmhiList = cropAndResizeImageList(xozDmhiList)
        postYozDmhiList = cropAndResizeImageList(yozDmhiList)
        
            

if __name__ == '__main__':
    main()