# -*- coding: utf-8 -*-
"""
Created on Thu May  4 11:01:05 2017

@author: kaifeng
"""

import logRegression
from imp import reload 
import numpy as np

# 调用函数，来获取参数θ的矩阵
reload(logRegression)
dataArr , labelMat = logRegression.loadDataSet()
logRegression.gradAscent(dataArr,labelMat)


# 利用参数θ的矩阵绘制最优线性解
reload(logRegression)
weights = logRegression.gradAscent(dataArr,labelMat)
logRegression.plotBestFit(weights)

# 测试随机梯度下降的效果
reload(logRegression)
dataArr,labelMat = logRegression.loadDataSet()
weights = logRegression.stocGradAscent(np.array(dataArr),labelMat)
logRegression.plotBestFit(weights)   # 效果差了很多，但是计算速度快，如果多迭代几次就可能会有更好的效果，参数可以稳定

# 测试已修改后的随机梯度下降的效果
reload(logRegression)
weights = logRegression.stocGradAscentNew(np.array(dataArr),labelMat)
logRegression.plotBestFit(weights)  # 效果应该差不多了

# 测试看在病马死亡率问题上分类效果如何
reload(logRegression)
logRegression.multiTest()



