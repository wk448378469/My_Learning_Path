# -*- coding: utf-8 -*-
"""
Created on Thu May  4 15:39:02 2017

@author: kaifeng
"""

import svmMLiA
from imp import reload 
import numpy as np
import scipy as sp

# 读取下数据，SVM中label一般是-1和1如果二分的话
dataArr,labelArr = svmMLiA.loadData('testSet.txt')
labelArr   


# 查看下SMO的输出结果
reload(svmMLiA)
b,alphas = svmMLiA.smoSimple(dataArr, labelArr, 0.6, 0.001, 40)
b
alphas
# 输出支持向量
for i in range (100):
    if alphas[i] >0.0:
        print (dataArr[i],labelArr[i])
        

# 看下优化之后的
reload(svmMLiA)
b,alphas = svmMLiA.smoP(dataArr, labelArr, 0.6, 0.001, 40)

# 给出W
reload(svmMLiA)
ws = svmMLiA.calcWs(alphas,dataArr,labelArr)
ws

# 查看分类结果
datMat = sp.mat(dataArr)
datMat[0] * sp.mat(ws) + b   # 看预测的
labelArr[0]                  # 看实际的

# 试试看高斯核的
reload(svmMLiA)
svmMLiA.testGauss()     # 默认是1.3
svmMLiA.testGauss(k1 = 0.5)
svmMLiA.testGauss(k1 = 0.7)
svmMLiA.testGauss(k1 = 0.9)
svmMLiA.testGauss(k1 = 1.1)
svmMLiA.testGauss(k1 = 1.4)
svmMLiA.testGauss(k1 = 1.6)     # 别搞太大

#看看在数字识别上效果如何
reload(svmMLiA)
svmMLiA.testDigits(('Gauss',10))    # 这个应该是最好的参数了已经
