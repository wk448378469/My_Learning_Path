# -*- coding: utf-8 -*-
"""
Created on Tue May 16 10:26:18 2017

@author: 凯风
"""

from imp import reload
import apriori


reload(apriori)
dataSet = apriori.loadDataSet()     # 获取数据
dataSet
C1 = apriori.creadteC1(dataSet)     # 获取数据集的C1-候选项集合
C1
D = list(map(set,dataSet))          # 把数据转换成集合的形式存放在列表中
D
L1,supportData0 = apriori.scanD(D,C1,0.5)   # 以0.5支持度为要求，计算候选集的每一个项的支持度，并返回大于支持度的集合L1
L1
supportData0

# 根据支持度生成频繁集
reload(apriori)
L,supportData = apriori.apriori(dataSet)
L       # 获得支持度大于0.5的频繁集合
L[0]    # 包含一个元素的
L[1]    # 包含两个元素的
L[2]    # 包含三个元素的
L[3]
apriori.aprioriGen(L[0],2)  # 看一下如何生成的未和支持度比较的‘L[1]’
L,supportData = apriori.apriori(dataSet,minSupport=0.7) # 更大的支持度，获得少的结果了

# 根据可信度生成关联规则
reload(apriori)
L,supportData = apriori.apriori(dataSet,minSupport=0.5)
rules = apriori.generateRules(L,supportData,minConf=0.7)  # 0.7的可信度生成的规则
rules = apriori.generateRules(L,supportData,minConf=0.5)  # 0.5的可信度生成的规则



# 在毒蘑菇的数据集上测试下效果如何
mushDataSet = [line.split() for line in open('mushroom.dat').readlines()]
# 这个数据集第一列是标签是否有毒
L,supportData = apriori.apriori(mushDataSet,minSupport=0.3)
for item in L[3]:   
    if item.intersection('2'):      # 看下包含特征有毒为2的频繁项集
        print (item)
