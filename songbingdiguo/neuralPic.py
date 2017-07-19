#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 17:26:02 2017

@author: kaifeng
"""

from randomModel import randomModel
import os
import urllib

def neuralPic(picurl):
    usedModel = randomModel()             # random chose a trained model
    
    picname = picurl.split('/')[-1]
    currentDirectory = os.path.dirname(__file__)
    picpath = os.path.join(currentDirectory,'evalPic/img/'+picname)
    
    urllib.urlretrieve(picurl,picpath)     # save user pic
    usedFile = os.path.join(currentDirectory,'evalPic/myeval.py')
    
    returnFile = os.path.join(currentDirectory,'generated/'+picname)
    
    try:
        # generate pic
        os.system('python %s --model_file %s --image_file %s' % (usedFile,usedModel,picpath))
        # generate pic in evalPic/generated/picname
        return returnFile
    except:
        return None