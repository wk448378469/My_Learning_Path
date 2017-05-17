# -*- coding: utf-8 -*-
"""
Created on Tue May 16 15:50:35 2017

@author: 凯风
"""

from imp import reload
import fpGrowth

reload(fpGrowth)
rootNode = fpGrowth.treeNode('pyramid' , 9 , None)           # 创建一个单节点
rootNode.children['eye'] = fpGrowth.treeNode('eye',13,None)  # 增加一个子节点
rootNode.disp()                 # 显示
rootNode.children['phoenix'] = fpGrowth.treeNode('phoenix',3,None)  # 增加一个子节点
rootNode.disp()                 # 显示


reload(fpGrowth)
simpDat = fpGrowth.loadSimpDat()    # 获取数据集
simpDat
initSet = fpGrowth.createInitSet(simpDat)   # 格式化处理数据集
initSet
myFPtree,myHeaderTab = fpGrowth.createTree(initSet,3)   # 生成树
myFPtree.disp()         # 显示


reload(fpGrowth)
fpGrowth.findPrefixPath('x',myHeaderTab['x'][1])    # 给定元素，生成条件基
fpGrowth.findPrefixPath('z',myHeaderTab['z'][1])
fpGrowth.findPrefixPath('r',myHeaderTab['r'][1])


reload(fpGrowth)
freqItems = []      # 空列表存储频繁项集
fpGrowth.mineTree(myFPtree,myHeaderTab,3,set([]),freqItems)
freqItems


# 在大数据集上看看效果，该数据集有100W条记录
parseDat = [line.split() for line in open('kosarak.dat').readlines()]   # 读取数据
initSet = fpGrowth.createInitSet(parseDat)  # 集合格式化
myFPtree,myHeaderTab = fpGrowth.createTree(initSet,100000)  # 训练处一颗FP树，找到被10W人浏览的新闻
myFreqList = []     # 用来保存频繁项集的
fpGrowth.mineTree(myFPtree,myHeaderTab,100000,set([]),myFreqList)
len(myFreqList)     # 获取频繁集长度
myFreqList      # 看看频繁项集的元素都有哪些
