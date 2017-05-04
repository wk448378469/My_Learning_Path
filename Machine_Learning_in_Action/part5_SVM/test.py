# -*- coding: utf-8 -*-
"""
Created on Thu May  4 15:39:02 2017

@author: kaifeng
"""

import svmMLiA
from imp import reload 

# 读取下数据，SVM中label一般是-1和1如果二分的话
dataArr,labelArr = svmMLiA.loadData('testSet.txt')
labelArr   


# 
reload(svmMLiA)
b,alphas = svmMLiA.smoSimple(dataArr, labelArr, 0.6, 0.001, 40)
