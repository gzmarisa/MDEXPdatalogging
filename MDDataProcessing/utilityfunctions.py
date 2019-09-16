# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 14:00:39 2019

@author: Kyle Boyer
"""

import os
import pandas as pd
import numpy as np
from pandas.plotting import register_matplotlib_converters
import time

register_matplotlib_converters()


global debugprint
global verboseprint

debugprint = lambda *a, **k: None # No Debug Printing
verboseprint = lambda *a, **k: None # No Verbose Printing

def enableDebugPrinting(debug: bool = True):
    global debugprint
    debugprint = print if debug else lambda *a, **k: None # Debug Printing

def enableVerbosePrinting(verbose: bool = True):
    global verboseprint
    verboseprint = print if verbose else lambda *a, **k: None # Verbose Printing



defaultFileLocation = '.'
defaultExtension = '' # Change to '.' to require an extension to be present


def getFileNames(loc: str = defaultFileLocation, ext: str = defaultExtension):
    """Returns a list of filenames from location loc with extension ext"""
    filenames = [f for f in os.listdir(loc) if ext in f]
    return filenames

def getCSVFileNames(loc: str = '.'):
    """Returns a list of filenames from location loc with extension '.csv'"""
    return getFileNames(loc,'.csv')

def getNPZFileNames(loc: str = '.'):
    """Returns a list of filenames from location loc with extension '.npz'"""
    return getFileNames(loc,'.npz')



def getFilePaths(loc: str = '.', ext: str = '.'):
    """Returns a list of file paths from location loc with extension ext"""
    filepaths = [os.path.abspath(os.path.join(loc,f)) for f in os.listdir(loc) if ext in f]
    return filepaths

def splitFilePath(path: str):
    path,name = os.path.split(path)
    name,ext = os.path.splitext(name)
    return {'path':path,'name':name,'ext':ext}

def loadDataFromNPZFile(filename):
    """"Load data from zipped numpy file and place in Pandas DataFrame"""
    start = time.time()
    df = pd.DataFrame()
    with np.load(filename) as data:
        for key in [key for key in data]:
            if key != 'DK':
                df[key] = data[key]
            elif key == 'DK':
                dk = data['DK']
    end = time.time()
    verboseprint('Loaded file "',filename,'" in {:2.3f} seconds'.format(end-start),sep='')
    return df, dk

def loadDataFromNPZFiles(filenames, loc: str = '.'):
    start = time.time()
    ldf = []
    for filename in filenames:
        if '.npz' in filename:
            npzFileName = os.path.join(loc, filename)
            ldf.append(loadDataFromNPZFile(npzFileName))
    end = time.time()
    verboseprint('Loaded',len(filenames),' files in {:2.3f} seconds\n'.format(end-start),sep='')
    return ldf

def saveDataToNPZFile(filepath, df, dk = None):
    start = time.time()
    name = splitFilePath(filepath)['name']
    toSave = {}
    for key in df:
        toSave[key]=df[key]
    if dk is not None:
        toSave['DK'] = dk
    else:
        toSave['DK'] = {}
        for key in df:
            toSave['DK'][key] = key
        toSave['DK']['DK'] = 'Data Key'
        toSave['DK']['filename'] = name

    np.savez(
            filepath,
            **toSave
            )
    end = time.time()
    verboseprint('Saved file "',name,'" in {:2.3f} seconds'.format(end-start),sep='')



if __name__ == "__main__":
    # execute only if run as a script
    print('The rest of this line should be blank: ', end='')
    verboseprint('Test Failed')
    print('\nThe rest of this line should be blank: ', end='')
    debugprint('Test Failed')
