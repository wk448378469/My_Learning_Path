# -*- coding: utf-8 -*-
"""
Created on Thu May 11 16:32:22 2017

@author: 凯风
"""
from imp import reload
import adaboost
import scipy as sp
import numpy as np


datMat,classLabels = adaboost.loadSimpData()

reload(adaboost)
D = sp.mat(np.ones((5,1))/5)
adaboost.buildStump(datMat,classLabels,D)


reload(adaboost)
classifierArray = adaboost.adaBoostTrainDS(datMat,classLabels,9)


reload(adaboost)
datArr,labelArr = adaboost.loadSimpData()
classifierArr = adaboost.adaBoostTrainDS(datArr,labelArr,30)
adaboost.adaClassify([0,0],classifierArr)
adaboost.adaClassify([[5,5],[0,0]],classifierArr)


reload(adaboost)
datArr,labelArr = adaboost.loadDataSet('horseColicTraining2.txt')
classifierArray = adaboost.adaBoostTrainDS(datArr,labelArr,10)

testArr,testLabelArr = adaboost.loadDataSet('horseColicTest2.txt')
prediction10 = adaboost.adaClassify(testArr,classifierArray)
errArr = sp.mat(np.ones((67,1)))
errArr[prediction10 != sp.mat(testLabelArr).T].sum()


reload(adaboost)
datArr,labelArr = adaboost.loadDataSet('horseColicTraining2.txt')
classifierArray,aggClassEst = adaboost.adaBoostTrainDS(datArr,labelArr,10)
adaboost.plotROC(aggClassEst.T,labelArr)

