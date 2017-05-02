# -*- coding: utf-8 -*-
"""
Created on Tue May  2 14:05:03 2017

@author: kaifeng
"""

from math import log
import operator

def calcShannonEnt(dataSet):
    '''
    计算信息熵
    '''
    numEntries =len(dataSet)        # 数据集的长度，包含多少个样本
    labelCounts = {}
    for feetVec in dataSet:             
        currentLabel = feetVec[-1]          # 当前标签
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    # 为所有可能的分类创建字典
    
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries        # 计算所有分类的出现概率
        shannonEnt -= prob * log(prob,2)                # 计算以2为底求对数
    
    return shannonEnt

def creatDataSet():
    dataSet = [
            [1,1,'yes'],
            [1,1,'yes'],
            [1,0,'no'],
            [0,1,'no'],
            [0,1,'no']]
    labels = ['no surfacing','flippers']
    return dataSet,labels

def splitDataSet(dataSet,axis,value):       # 三个参数：数据集、列的参数、特征值
    retDataSet = []                 
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec =featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
            # 把每个样本中，指定列的值等于value(特征的值提取提取出来)，但是去掉了原有的列
            # append 可以在列表添加任意元素甚至是元组
            # extend 只能添加列表
    return retDataSet

def chooseBestFeatureToSplit(dataSet):
    numFeature = len(dataSet[0]) -1             # 第一列，除去标签的特征数
    baseEntropy = calcShannonEnt(dataSet)       # 计算每个特征的信息熵 
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(numFeature):
        feaList = [example[i] for example in dataSet]
        uniqueVals = set(feaList)               # 去重
        newEntropy = 0.0
        
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet,i,value)
            prob = len(subDataSet)/float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy
        # 计算每个特征的信息熵
        
        if infoGain > bestInfoGain:
            bestInfoGain = infoGain
            bestFeature = i 
    return bestFeature
    
def majorityCnt(classList):
    '''
        创建一个字典，字典包含标签和对应标签的样本数量
    '''
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1
        sortedClassCount = sorted(classCount.items(), key = operator.itemgetter(1) , reverse = True)
    return sortedClassCount[0][0]

    
def createTree(dataSet,labels):
    classList = [example[-1] for example in dataSet]        # 把所有标签生成一个列表
    if classList.count(classList[0]) == len(classList):     # 判断标签是不是全一样了
        return classList[0]     
    if len(dataSet[0]) == 1:                                # 如果特征只剩下一个，则不迭代了
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]                        # 得到最好的特征的名称
    myTree = {bestFeatLabel:{}}
    
    del(labels[bestFeat])
    
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    # 得到列表包含的所有属性值
    
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet,bestFeat,value),subLabels)
        
    return myTree
    
    
def classify(inputTree,featLabels,testVec):
    firstStr = list(inputTree.keys())[0]        # 返回第一个键
    secondDict = inputTree[firstStr]            # 第一个键对应的值
    featIndex = featLabels.index(firstStr)      # 把字符串转换成索引位
    for key in secondDict.keys():
        if testVec[featIndex] == key:
            if type(secondDict[key]).__name__ == 'dict':
                classLabel = classify(secondDict[key],featLabels,testVec)
            else:
                classLabel = secondDict[key]
            # 遍历整棵树，比较遍历的值和树节点的值，如果到达节点，则返回对应的分类标签
            
    return classLabel

def storeTree(inputTree,filename):
    '''
        以文件形式存储分类器
    '''
    import pickle
    fw = open(filename,'wb+')
    pickle.dump(inputTree,fw)
    fw.close()
    
    
def grabTree(filename):
    '''
        读取分类器
    '''
    import pickle
    fr = open(filename,'rb+')
    return pickle.load(fr)


def lensesTest():
    fr = open('lenses.txt')
    lenses = [inst.strip().split('\t') for inst in fr.readlines()]
    lensesLabels = ['agr','prescript','astigmatic','tearrate']
    lensesTree = createTree(lenses,lensesLabels)
    return lensesTree    
    
    
    