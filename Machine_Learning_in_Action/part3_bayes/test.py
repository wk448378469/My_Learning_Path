# -*- coding: utf-8 -*-
"""
Created on Wed May  3 12:19:55 2017

@author: kaifeng
"""

import bayes
from imp import reload

reload(bayes)

# 调用生产测试数据的函数
listOposts,listClasses = bayes.loadDataSet()

# 获取无重复、全部词的函数
myVocaBList = bayes.creatVocabList(listOposts)
myVocaBList

# 获得每个文本的词向量
bayes.setOfWords2Vec(myVocaBList,listOposts[0])
bayes.setOfWords2Vec(myVocaBList,listOposts[3])
bayes.setOfWords2Vec(myVocaBList,listOposts[4])

# 调用计算函数，计算各类先验概率等
import numpy as np
trainMat = []
for postinDoc in listOposts:
    trainMat.append(bayes.setOfWords2Vec(myVocaBList,postinDoc))
    
p0v,p1v,pAb = bayes.trainNB0(trainMat,listClasses)
pAb
p0v
p1v
p2v = 1 - p1v


# 测试模型
reload(bayes)
bayes.testingNB()


# 测试模型，看垃圾邮件分类器表现如何
reload(bayes)
bayes.spamTest()


# 测试模型，看详情的如何....
reload(bayes)
import feedparser
ny = feedparser.parse('http://newyork.craigslist.org/stp/index.rss')
sf = feedparser.parse('http://sfbay.craigslist.org/stp/index.rss')
# 这里获取的数据因为每次都不太一致，需要调整
#   1、随机生成训练集的数量
#   2、频率最高词的数量
vocabList,pSF,pNY = bayes.localWords(ny,sf)
vocabList,pSF,pNY = bayes.localWords(sf,ny)


# 看看刚刚的那些词对分类影响比较大
reload(bayes)
bayes.getTopWords(ny,sf)

