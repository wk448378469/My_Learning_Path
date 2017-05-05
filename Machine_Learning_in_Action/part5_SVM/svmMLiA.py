# -*- coding: utf-8 -*-
"""
Created on Thu May  4 15:26:58 2017

@author: kaifeng
"""

import numpy as np
import scipy as sp

def loadData(fileName):
    # 读取数据的函数
    dataMat = []
    labelMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr = line.strip().split('\t')
        dataMat.append([float(lineArr[0]),float(lineArr[1])])
        labelMat.append(float(lineArr[2]))
    return dataMat,labelMat

def selectJrand(i,m):
    # 随机给出а的下标
    j = i
    while (j==i):
        j = int(np.random.uniform(0,m))     # m是а的数量
    return j

def clipAlpha(aj,H,L):
    '''
        函数是用于调整大于H或小于L的а值
                | H                 if a_new > H
        а_new = | a_new_边界        if L<= a_new <= H
                | L                 uf a_new < L    
    '''
    if aj > H:
        aj = H
    if L > aj:
        aj = L
    return aj


def smoSimple(dataMatIn,classLabels,C,toler,maxIter):
    dataMatrix = sp.mat(dataMatIn)                  # 矩阵化，方便计算
    labelIMat = sp.mat(classLabels).transpose()     # 矩阵化、转置
    b = 0                                           # SVM中的一个参数，类似于截距
    m,n = np.shape(dataMatrix)                      # m是样本数，n是特征数
    alphas = sp.mat(np.zeros((m,1)))                # SVM中另一个参数，是一个矩阵
    iterm = 0                                       # 控制迭代的
    while(iterm < maxIter):
        alphaPairsChanged = 0                       # SMO算法是一次改变两个a的
        for i in range(m):
            # sp.multiply是矩阵元素之间的乘法，不是矩阵乘法
            fXi = sp.float64(sp.multiply(alphas,labelIMat).T * (dataMatrix*dataMatrix[i,:].T)) + b # 计算预测值
            Ei = fXi - sp.float64(labelIMat[i])         # 计算误差
            if ((labelIMat[i]*Ei < -toler).all() and (alphas[i] < C)) or ((labelIMat[i]*Ei > toler).all() and (alphas[i] > 0)):  # 如果参数а可以改进则进入流程
                j = selectJrand(i,m)    # 随机选取第二个参数а，其实应该用启发式的决策而不是随机
                fXj = sp.float64(sp.multiply(alphas,labelIMat).T * (dataMatrix*dataMatrix[j,:].T)) + b # 计算预测值
                Ej = fXj - sp.float64(labelIMat[j])     # 计算误差
                alphaIold = alphas[i].copy()        # 记录下来两个参数的这次修改前的值
                alphaJold = alphas[j].copy()
                if (labelIMat[i] != labelIMat[j]):
                    L = max(0,alphas[j]-alphas[i])  # 计算L和H，其实这两个应该用另外的方式计算，作用是保证а在[0,C]范围内
                    H = min(C,C+alphas[j]-alphas[i])
                else:
                    L = max(0,alphas[j]+alphas[i]-C)
                    H = min(C,alphas[j]+alphas[i])
                if L==H: print ('L==H') ;continue        # 直接进入下次for循环
                # 参数更新公式：a_new = a + y(Ei-Ej)/η    eta=η
                eta = 2.0 * dataMatrix[i,:]*dataMatrix[j,:].T - dataMatrix[i,:]*dataMatrix[i,:].T - dataMatrix[j,:]*dataMatrix[j,:].T
                if eta >= 0: print ('eta>=0') ;continue
                alphas[j] -= labelIMat[j]*(Ei-Ej)/eta           # 更新一
                alphas[j] = clipAlpha(alphas[j],H,L)            # 更新二，是否超出边界看
                if (abs(alphas[j] - alphaJold) < 0.00001): print ('j not moving enough') ;continue
                alphas[i] += labelIMat[j] * labelIMat[i] * (alphaJold-alphas[j])    # i的更新公式 a_new  = a_old+y1*y2*(aj-a_更新二后)
                
                # 参数b的更新公式和满足条件
                b1 = b - Ei - labelIMat[i]*(alphas[i] - alphaIold)*dataMatrix[i,:]*dataMatrix[i,:].T - labelIMat[j]*(alphas[j]-alphaJold)*dataMatrix[i,:]*dataMatrix[j,:].T
                b2 = b - Ej - labelIMat[i]*(alphas[i] - alphaIold)*dataMatrix[i,:]*dataMatrix[j,:].T - labelIMat[j]*(alphas[j]-alphaJold)*dataMatrix[j,:]*dataMatrix[j,:].T
                if (0 < alphas[i]) and (C > alphas[i]):
                    b = b1
                elif(0 < alphas[j]) and (C > alphas[j]):
                    b = b2
                else:
                    b = (b1+b2)/2.0
                
                alphaPairsChanged += 1
                print ("iter: %d i:%d, pairs changed %d" % (iterm,i,alphaPairsChanged))
        if (alphaPairsChanged == 0):
            iterm += 1
        else:
            iterm = 0
        print ("iteration number: %d" % iterm)
    return b,alphas
    
    
    
    
    
    
    
    
    
    
    
    
    
    