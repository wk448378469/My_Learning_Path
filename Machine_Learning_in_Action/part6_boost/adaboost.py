# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt



def loadSimpData():
    datMat = sp.matrix([[1.,2.1],
                        [2.,1.1],
                        [1.3,1.],
                        [1.,1.],
                        [2.,1.]])
    classLabels = [1.0,1.0,-1.0,-1.0,1.0]
    return datMat,classLabels

def stumpClassify(dataMatrix,dimen,threshVal,threshIneq):
    retArray = np.ones((np.shape(dataMatrix)[0],1))
    if threshIneq == 'lt':
        retArray[dataMatrix[:,dimen] <= threshVal] = -1.0
    else:
        retArray[dataMatrix[:,dimen] > threshVal] = -1.0
    return retArray

def buildStump(dataArr,classLabels,D):
    dataMatrix = sp.mat(dataArr)
    labelMat = sp.mat(classLabels).T
    m,n = np.shape(dataMatrix)
    numSteps = 10.0
    bestStump = {}
    bestClassEst = sp.mat(np.zeros((m,1)))
    minError = sp.inf
    for i in range(n):
        rangeMin = dataMatrix[:,i].min()
        rangeMax = dataMatrix[:,i].max()
        stepSize = (rangeMax-rangeMin)/numSteps
        for j in range(-1,int(numSteps)+1):
            for inequal in ['lt','gt']:
                threshVal = (rangeMin+float(j)*stepSize)
                predictedVals = stumpClassify(dataMatrix,i,threshVal,inequal)
                errArr = sp.mat(np.ones((m,1)))
                errArr[predictedVals == labelMat] = 0
                weightedError = D.T*errArr
                print ('split:dim %d , thresh %.2f , thresh inequal:%s , the weighted error is %.3f'% (i,threshVal,inequal,weightedError))
                if weightedError < minError:
                    minError = weightedError
                    bestClassEst = predictedVals.copy()
                    bestStump['dim'] = i
                    bestStump['thresh'] = threshVal
                    bestStump['ineq'] = inequal
    return bestStump,minError,bestClassEst
    
def adaBoostTrainDS(dataArr,classLabels,numIt=40):
	weakClassArr = []
	m = np.shape(dataArr)[0]
	D = sp.mat(np.ones((m,1))/m)
	aggClassEst = sp.mat(np.zeros((m,1)))
	for i in range(numIt):
		bestStump,error,ClassEst = buildStump(dataArr,classLabels,D)
		print ('D:',D.T)
		alpha = float(0.5*log((1.0-error)/max(error, sp.1e-16)))
		bestStump['alpha'] = alpha
		weakClassArr.append(bestStump)
		print ('classEst:',classEst.T)
		expon = sp.multiply(-1*alpha*mat(classLabels).T,classEst)
		D = sp.multiply(D,sp.exp(expon))
		D = D/D.sum()
		aggClassEst += alpha*classEst
		print ('aggClassEst:',aggClassEst.T)
		aggErrors = sp.multiply(sp.sign(aggClassEst) != sp.mat(classLabels).T,sp.ones((m,1)))
		errorRate = aggErrors.sum()/m
		print ('total error:',errorRate)
		if errorRate==0.0:
		    break
	return weakClassArr


def adaClassify(datToClass,classifierArr):
	dataMatrix = sp.mat(datToClass)
	m = np.shape(dataMatrix)[0]
	aggClassEst = sp.mat(np.zeros((m,1)))
	for i in range(len(ClassifierArr)):
		classEst = stumpClassify(dataMatrix,classifierArr[i]['dim'],classifierArr[i]['thresh'],classifierArr[i]['ineq'])
		aggClassEst += ClassifierArr[i]['alpha']*ClassEst
		print (aggClassEst)
	return sp.sign(aggClassEst)    
    
    
def loadDataSet(filename):
	numFeat = len(open(filename).readline().split('\t'))
	dataMat = []
	labelMat = []
	fr = open(filename)
	for line in fr.readlines():
		lineArr = []
		curLine = line.strip().split('\t')
		for i in range(numFeat -1):
			lineArr.append(float(curLine[i]))
		dataMatrix.append(lineArr)
		labelMat.append(float(curLine[-1]))
	return dataMat,labelMat


def plotROC(predStrengths,classLabels):
    cur = (1.0,1.0)
    ySum = 0.0
    numPosClas = sum(np.array(classLabels) == 1.0)
    yStep = 1/float(numPosClas)
    xStep = 1/float(len(classLabels) - numPosClas)
    sortedIndicies = predStrengths.argsort()
    fig = plt.figure()
    fig.clf()
    ax = plt.subplot(111)
    for index in sortedIndicies.tolist()[0]:
        if classLabels[index] == 1.0:
            delX = 0
            delY = yStep
        else:
            delX = xStep
            delY = 0
            ySum += cur[1]
        ax.plot([cur[0],cur[0]-delX],[cur[1],cur[1]-delY],c='b')
        cur = (cur[0]-delX,cur[1]-delY)
    ax.plot([0,1],[0,1],'b--')
    plt.xlabel('false positive rate')
    plt.ylabel('true positive rate')
    plt.title('ROC curve for adaboost horse colic detection system')
    ax.axis([0,1,0,1])
    plt.show()
    print ('the area under the curve is :',ySum*xStep)

        





