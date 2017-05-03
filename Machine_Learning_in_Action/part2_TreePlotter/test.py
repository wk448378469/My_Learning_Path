# -*- coding: utf-8 -*-
"""
Created on Wed May  3 11:08:25 2017

@author: kaifeng
"""

import trees

# 读取测试数据
myData,labels = trees.creatDataSet()
myData
labels

# 调用函数，指定列，划分数据用的
trees.splitDataSet(myData,0,1)
trees.splitDataSet(myData,0,0)

# 调用函数，获取最好的数据集划分方式，使用熵来计算
trees.chooseBestFeatureToSplit(myData)

# 调用决策树函数
myTree = trees.createTree(myData,labels)
myTree

# 在测试数据上看决策树效果
myData,labels = trees.creatDataSet()
trees.classify(myTree,labels,[1,0])
trees.classify(myTree,labels,[1,1])

# 调用存储决策树的函数
trees.storeTree(myTree,'classifierStore.txt')

# 调用存储为文件形式的决策树
trees.grabTree('classifierStore.txt')

# 生成隐形眼镜的类型的函数
fr = open('lenses.txt')
lenses = [inst.strip().split('\t') for inst in fr.readlines()]
lensesLabels = ['age','prescript','astigmatic','tearRate']
lensesTree = trees.createTree(lenses,lensesLabels)
lensesTree

