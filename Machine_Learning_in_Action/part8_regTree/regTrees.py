# -*- coding: utf-8 -*-
"""
Created on Sat May 13 10:26:55 2017

@author: 凯风
"""

import numpy as np

def loadDataSet(filename):
    # 读取数据
    dataMat = []
    fr = open(filename)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        fltLine = list(map(float,curLine))       # 将每行映射成浮点数
        dataMat.append(fltLine)
    return dataMat

def binSplitDataSet(dataSet,feature,value):
    # 将数据集按某个特征的某个值进行切分
    mat0 = dataSet[np.nonzero(dataSet[:,feature] > value)[0],:]
    mat1 = dataSet[np.nonzero(dataSet[:,feature] <= value)[0],:]
    return mat0,mat1

def regLeaf(dataSet):
    # 生成叶节点
    return np.mean(dataSet[:,-1])

def regErr(dataSet):
    # 误差估计
    return np.var(dataSet[:,-1]) * np.shape(dataSet)[0]

def chooseBestSplit(dataSet , leafType=regLeaf , errType=regErr , ops=(1,4)):
    # 核心，找到最佳的分割策略，二元的
    tolS = ops[0]   # 误差下限
    tolN = ops[1]   # 切分的最小样本数
    if len(set(dataSet[:,-1].T.tolist()[0])) == 1:  # 目标变量值唯一，停止
        return None , leafType(dataSet)
    m,n = np.shape(dataSet)
    S = errType(dataSet)    # 计算数据集误差
    bestS = np.inf
    bestIndex = 0
    bestValue = 0
    for featIndex in range(n-1):    # 遍历每个特征
        for splitVal in set((dataSet[:, featIndex].T.A.tolist())[0]):   # 遍历每个特征中的不同值
            mat0,mat1 = binSplitDataSet(dataSet,featIndex,splitVal)     # 对每个特征进行二元切分
            if (np.shape(mat0)[0] < tolN) or (np.shape(mat1)[0] < tolN):    # 切分后如果小于最小样本数就继续
                continue
            newS = errType(mat0) + errType(mat1)    # 计算新的误差评估
            if newS < bestS:
                bestIndex = featIndex
                bestValue = splitVal
                bestS = newS
    if (S - bestS) < tolS:      # 误差减少小于下限时，停止
        return None , leafType(dataSet)
    mat0,mat1 = binSplitDataSet(dataSet,bestIndex,bestValue)
    if (np.shape(mat0)[0] < tolN) or (np.shape(mat1)[0] < tolN):    # 数据集数量过少时，停止
        return None , leafType(dataSet)
    return bestIndex,bestValue


def createTree(dataSet , leafType=regLeaf , errType=regErr , ops=(1,4)):
    # 树构建函数，参数有数据集、叶节点类型、错误类型、其他...
    feat,val = chooseBestSplit(dataSet,leafType,errType,ops)    # 调用一个方法来划分数据集，如果是回归树，val是常熟、模型树val是一个线性方程
    if feat == None:    # 满足条件则返回叶节点的值
        return val
    retTree = {}    # 创建一个空的用来保存树结构的字典
    retTree['spInd'] = feat     # 特征
    retTree['spVal'] = val      # 特征值
    lSet,rSet = binSplitDataSet(dataSet,feat,val)   # 根据特征和特征值，将数据集划分两瓣
    retTree['left'] = createTree(lSet,leafType,errType,ops)     # 递归
    retTree['right'] = createTree(rSet,leafType,errType,ops)
    return retTree


def isTree(obj):
    # 判断传入的对象是不否是字典，返回布尔值
    return (type(obj).__name__=='dict')

def getMean(tree):
    # 塌陷处理？返回平均值
    if isTree(tree['right']): tree['right'] = getMean(tree['right'])
    if isTree(tree['left']): tree['left'] = getMean(tree['left'])
    return (tree['left']+tree['right'])/2.0
    
def prune(tree, testData):
    # 待剪枝的树和测试数据
    if np.shape(testData)[0] == 0: # 判断测试数据及是否为空
        return getMean(tree) 
    if (isTree(tree['right']) or isTree(tree['left'])):     # 左右分支是否为树，还是节点
        lSet, rSet = binSplitDataSet(testData, tree['spInd'], tree['spVal'])
    if isTree(tree['left']): 
        tree['left'] = prune(tree['left'], lSet)
    if isTree(tree['right']):
        tree['right'] =  prune(tree['right'], rSet)
    if not isTree(tree['left']) and not isTree(tree['right']):  # 如果都不再是子树
        lSet, rSet = binSplitDataSet(testData, tree['spInd'], tree['spVal'])
        errorNoMerge = sum(np.power(lSet[:,-1] - tree['left'],2)) +\
                          sum(np.power(rSet[:,-1] - tree['right'],2))   # 合并
        treeMean = (tree['left']+tree['right'])/2.0
        errorMerge = sum(np.power(testData[:,-1] - treeMean,2))
        if errorMerge < errorNoMerge:   # 判断合并后误差
            print("merging")
            return treeMean
        else: return tree
    else: return tree
    
