'''
Created on 10 Sep 2014

@author: bliang03
'''

import config
from data_process.dataset_process import loadDataset

def main():
    ## load dataset
    loadDataset(config.currentDataset)

if __name__ == '__main__':
    main()