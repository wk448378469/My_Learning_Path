# -*- coding: utf-8 -*-
"""
Created on Thu May  4 15:26:58 2017

@author: kaifeng
"""

import numpy as np
import scipy as sp

def loadData(fileName):
    dataMat = []
    labelMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr = line.strip().split('\t')
        dataMat.append([float(lineArr[0]),float(lineArr[1])])
        labelMat.append(float(lineArr[2]))
    return dataMat,labelMat

def selectJrand(i,m):
    j = 1       # 参数а的下标
    while (j==1):
        j = int(np.random.uniform(0,m))     # m是а的数量
    return j

def clipAlpha(aj,H,L):
    # 函数是用于调整大于H或小于L的а值
    if aj > H:
        aj = H
    if L > aj:
        aj = L
    return aj


def smoSimple(dataMatIn,classLabels,C,toler,maxIter):
    dataMatrix = sp.mat(dataMatIn)
    labelIMat = sp.mat(classLabels)
    b = 0
    m,n = np.shape(dataMatrix)
    alphas = sp.mat(np.zeros((m,1)))
    iterm = 0
    while(iterm < maxIter):
        alphaPairsChanged = 0
        for i in range(m):
            fXi = sp.float_(sp.multiply(alphas,labelIMat).T * (dataMatrix*dataMatrix[i,:].T)) + b
            Ei = fXi - sp.float_(labelIMat[0,i])
            if ((labelIMat[0,i]*Ei < -toler) - (alphas[i] < C)).any() or ((labelIMat[0,i]*Ei > toler) - (alphas[i] >0)).any():
                j = selectJrand(i,m)
                fXj = sp.float_(sp.multiply(alphas,labelIMat).T * (dataMatrix*dataMatrix[j,:].T)) + b
                Ej = fXj - sp.float_(labelIMat[0,j])
                alphaIold = alphas[i].copy()
                alphaJold = alphas[j].copy()
                if (labelIMat[0,i] != labelIMat[0,j]):
                    L = max(0,alphas[j]-alphas[i])
                    H = min(C,C+alphas[j]-alphas[i])
                else:
                    L = max(0,alphas[j]+alphas[i]-C)
                    H = min(C,alphas[j]+alphas[i])
                if L==H:
                    print ('L==H')
                continue
                eta = 2.0 * dataMatrix[i,:]*dataMatrix[j,:].T - dataMatrix[i,:]*dataMatrix[i,:].T - dataMatrix[j,:]*dataMatrix[j,:].T
                if eta >= 0:
                    print ('eta>=0')
                continue
                alphas[j] -= labelIMat[0,j]*(Ei-Ej)/eta
                alphas[j] = clipAlpha(alphas[j],H,L)
                if (abs(alphas[j] - alphaJold) < 0.00001):
                    print ('j not moving enough')
                continue
                alphas[i] += labelIMat[0,j] * labelIMat[0,i] * (alphaJold-alphaIold)
                b1 = b - Ei - labelIMat[0,i]*(alphas[i] - alphaIold)*dataMatrix[i,:]*dataMatrix[i,:].T - labelIMat[j]*(alphas[j]-alphaJold)*dataMatrix[i,:]*dataMatrix[j,:].T
                b2 = b - Ej - labelIMat[0,i]*(alphas[i] - alphaIold)*dataMatrix[i,:]*dataMatrix[j,:].T - labelIMat[j]*(alphas[j]-alphaJold)*dataMatrix[j,:]*dataMatrix[j,:].T
                if ((0<alphas[i]) - (C>alphas[i])).any():
                    b = b1
                elif((0<alphas[j]) - (C>alphas[j])).any():
                    b = b2
                else:
                    b = (b1+b2)/2.0
                alphaPairsChanged += 1
                print (iterm,i,alphaPairsChanged)
        if (alphaPairsChanged == 0):
            iterm += 1
        else:
            iterm = 0
        print ('iteratiom number:',iterm)
    return b,alphas
                    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    