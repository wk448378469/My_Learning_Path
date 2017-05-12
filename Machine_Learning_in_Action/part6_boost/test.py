# -*- coding: utf-8 -*-
"""
Created on Thu May 11 16:32:22 2017

@author: 凯风
"""
from imp import reload
import adaboost
import numpy as np


datMat,classLabels = adaboost.loadSimpData()

reload(adaboost)
D = np.mat(np.ones((5,1))/5) # 初始化向量，用来标记每个样本的权重，如果分类错误则增加其权重
adaboost.buildStump(datMat,classLabels,D) # 单个基分类器


reload(adaboost)    
classifierArray = adaboost.adaBoostTrainDS(datMat,classLabels,9)    # 完整的基于基分类器的boosting
# 最后的参数9是迭代次数


reload(adaboost)
datArr,labelArr = adaboost.loadSimpData()
classifierArr = adaboost.adaBoostTrainDS(datArr,labelArr,30)
# 预测数据
adaboost.adaClassify([0,0],classifierArr)
adaboost.adaClassify([[5,5],[0,0]],classifierArr)


# 在实例上看看效果
reload(adaboost)
datArr,labelArr = adaboost.loadDataSet('horseColicTraining2.txt')
classifierArray = adaboost.adaBoostTrainDS(datArr,labelArr,50)      # 训练，迭代50次
testArr,testLabelArr = adaboost.loadDataSet('horseColicTest2.txt')  
prediction10 = adaboost.adaClassify(testArr,classifierArray)        # 测试
errArr = np.mat(np.ones((67,1)))
errArr[prediction10 != np.mat(testLabelArr).T].sum()        # 打印错误数量，总数为67

# ROC曲线绘制及AUC计算
reload(adaboost)
datArr,labelArr = adaboost.loadDataSet('horseColicTraining2.txt')
classifierArray,aggClassEst = adaboost.adaBoostTrainDS(datArr,labelArr,50)
adaboost.plotROC(aggClassEst.T,labelArr)

