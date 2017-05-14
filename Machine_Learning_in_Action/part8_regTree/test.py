# -*- coding: utf-8 -*-
"""
Created on Sat May 13 11:29:41 2017

@author: 凯风
"""

import regTrees
import numpy as np
from imp import reload

# 调用二元切分看下切分效果
reload(regTrees)
testMat = np.mat(np.eye(4))
testMat
mat0,mat1 = regTrees.binSplitDataSet(testMat,1,0.5)
mat0
mat1


# 根据数据集生成回归树
reload(regTrees)
myDat = regTrees.loadDataSet('ex00.txt')
myMat = np.mat(myDat)
regTrees.createTree(myMat)

# 根据数据生成回归树，不过特征数多些。。。就多一个
myDat1 = regTrees.loadDataSet('ex0.txt')
myMat1 = np.mat(myDat1)
regTrees.createTree(myMat1) # 如果不画图基本上不是人看的....

# 看看其他的参数对模型的影响,隐含的就是通过参数设置来裁剪树，俗称前剪枝
regTrees.createTree(myMat,ops=(0,1))    # ops的第二个参数是最小切分的样本数，所以基本上每个样本一个叶节点了。。。

myDat2 = regTrees.loadDataSet('ex2.txt')
myMat2 = np.mat(myDat2)
regTrees.createTree(myMat2)     # 默认是(1,4)
regTrees.createTree(myMat2,ops=(10000,4))                   
                
# 后剪枝
reload(regTrees)
myTree = regTrees.createTree(myMat2,ops=(0,1))
myDatTest = regTrees.loadDataSet('ex2test.txt')
myMat2Test = np.mat(myDatTest)
regTrees.prune(myTree,myMat2Test)   # 你真的剪了么。。。。

# 模型树部分了
reload(regTrees)
myMat2 = np.mat(regTrees.loadDataSet('exp2.txt'))
regTrees.createTree(myMat2,regTrees.modelLeaf,regTrees.modelErr,(1,10))    # 区别就是调用方法时选择不同的生成叶节点的方法和误差计算


# 模型比较
reload(regTrees)
trainMat = np.mat(regTrees.loadDataSet('bikeSpeedVsIq_train.txt'))
testMat = np.mat(regTrees.loadDataSet('bikeSpeedVsIq_test.txt'))
myTree = regTrees.createTree(trainMat,ops=(1,20))
yHat = regTrees.createForeCast(myTree,testMat[:,0]) # 创建一个回归树
np.corrcoef(yHat,testMat[:,1],rowvar=0)[0,1]

myTree = regTrees.createTree(trainMat,regTrees.modelLeaf,regTrees.modelErr,(1,20)) #同意的数据创建一个模型树
yHat = regTrees.createForeCast(myTree,testMat[:,0],regTrees.modelTreeEval)
np.corrcoef(yHat,testMat[:,1],rowvar=0)[0,1]    # 好像稍微高那么一些

ws,X,Y = regTrees.linearSolve(trainMat)   # 再试一下普通的线性回归
for i in range(np.shape(testMat)[0]):
    yHat[i] = testMat[i,0] * ws[1,0] + ws[0,0]
np.corrcoef(yHat,testMat[:,1],rowvar=0)[0,1]    # 好像最低的

# 大致应该是：模型树>回归树>线性回归





                   
