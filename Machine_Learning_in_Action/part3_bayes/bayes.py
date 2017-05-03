# -*- coding: utf-8 -*-
"""
Created on Wed May  3 11:35:32 2017

@author: kaifeng
"""

import numpy as np

def loadDataSet():
    postingList = [
                   ['my','dog','has','flea','problem','help','please'],
                   ['maybe','not','take','him','to','dog','park','stupid'],
                   ['my','dalmation','is','so','cute','I','love','him'],
                   ['stop','posting','stupid','worthless','garbage'],
                   ['mr','licks','ate','my','steak','how','to','stop','him'],
                   ['quit','buying','worthless','dog','food','stupid'] 
                  ]
    classVec = [0,1,0,1,0,1]   # 1代表有侮辱性词汇 0代表没有
    return postingList,classVec


def creatVocabList(dataSet):
    vocabSet = set([])
    for document in dataSet:
        vocabSet = vocabSet | set(document)       # 计算并集
    return list(vocabSet)       # 返回一个包含所有词，但是没有重复的列表


def setOfWords2Vec(vocabList,inputSet):
    # 词集模式，即不考虑词在样本中的出现频次，只考虑是否出现
    returnVec = [0]*len(vocabList)          # 创建一个和词库一样长度的列表
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else:
            print ('the word :%s is not in my Vocabulary!' %word)
    return returnVec


def bagOfWords2Vec(vocabList,inputSet):
    # 词袋模式，即考虑词在样本中出现的频次
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] += 1   # 唯一的区别在这里
    return returnVec
    

def trainNB0(trainMatrix,trainCategory):
    numTrainDocs = len(trainMatrix)         # 获取训练集样本数  6 
    numWords = len(trainMatrix[0])          # 总词汇量的长度   32
    pAbusive = sum(trainCategory)/float(numTrainDocs)   # 计算侮辱样本的概率
    
    # 初始化概率，拉普拉斯平滑
    p0Num = np.ones(numWords)
    p1Num = np.ones(numWords)
    p0Denom = 2.0
    p1Denom = 2.0
    
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:           # 如果样本是侮辱性的
            # 向量相加
            p1Num += trainMatrix[i]             # p1的数量为样本为侮辱性的向量和
            p1Denom += sum(trainMatrix[i])      # 计算样本为侮辱性的样本的词汇总数
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    
    # 对每个元素做处理
    p1Vect = np.log(p1Num/p1Denom)                # 计算侮辱性的词向量，每个词出现的概率
    p0Vect = np.log(p0Num/p0Denom)                # 取对数是为了防止值过小
    return p0Vect,p1Vect,pAbusive


def classifyNB(vec2Classify,p0Vec,p1Vec,pClass1):
    p1 = sum(vec2Classify*p1Vec) + np.log(pClass1)      # 测试样本的向量与侮辱性词向量相乘求和，再加上侮辱性样本的概率
    p0 = sum(vec2Classify*p0Vec) + np.log(1-pClass1)
    if p1>p0:
        return 1        # 垃圾
    else:
        return 0        # 正常


def testingNB():
    listOPosts,listClasses = loadDataSet()
    myVocabList = creatVocabList(listOPosts)
    trainMat = []
    for postingDoc in listOPosts:
        trainMat.append(setOfWords2Vec(myVocabList,postingDoc))
    p0V,p1V,pAb = trainNB0(np.array(trainMat),np.array(listClasses))
    
    # test1
    testEntry = ['love','my','dalamation']
    thisDoc = np.array(setOfWords2Vec(myVocabList,testEntry))
    print (testEntry,'classified as:',classifyNB(thisDoc,p0V,p1V,pAb))
    
    # test2
    testEntry = ['stupid','garbage']
    thisDoc = np.array(setOfWords2Vec(myVocabList,testEntry))
    print (testEntry,'classified as:',classifyNB(thisDoc,p0V,p1V,pAb))


def textParse(bigString):
    # 文本解析函数
    import re
    listOfTokens = re.split('r\W*',bigString)       # 去掉标点符号
    return [tok.lower() for tok in listOfTokens if len(tok) > 2]  # 去掉字符串中长度小于2的，首字母小写

def spamTest():
    docList = []    # 装词的
    classList = []  # 装标签的
    fullText = []   # 装全文本的
    for i in range(1,26):
        wordList = textParse(open('email/spam/%d.txt' % i,'rb').read().decode('GBK','ignore'))
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(1)
        wordList = textParse(open('email/ham/%d.txt' % i,'rb').read().decode('GBK','ignore'))
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(0)
        # 分别读取垃圾邮件和正常邮件，因为两个文件的数量25个是一样的，所以可以这样做
        
    vocabList = creatVocabList(docList)     # 生成词向量
    trainingSet = list(range(50))
    testSet = []
    for i in range(10):
        randIndex = int(np.random.uniform(0,len(trainingSet)))
        testSet.append(trainingSet[randIndex])
        del(trainingSet[randIndex])
        # 随机生成训练集
    
    trainMax = []
    trainClasses = []
    
    for docIndex in trainingSet:
        trainMax.append(setOfWords2Vec(vocabList,docList[docIndex]))
        trainClasses.append(classList[docIndex])
    p0V,p1V,pSpam = trainNB0(np.array(trainMax),np.array(trainClasses))
    # 训练模型
    
    errorCount = 0
    for docIndex in testSet:
        wordVector = setOfWords2Vec(vocabList,docList[docIndex])
        if classifyNB(np.array(wordVector),p0V,p1V,pSpam) != classList[docIndex]:
            errorCount += 1
    # 预测测试集
    
    print ('the error rate is :',float(errorCount)/len(testSet))


def calcMostFreq(vocabList,fullText):
    # 计算词的出现频率
    import operator
    freqDict = {}
    for token in vocabList:
        freqDict[token] = fullText.count(token)
    sortedFreq = sorted(freqDict.items(),key=operator.itemgetter(1),reverse = True)
    return sortedFreq[:10]

def localWords(feed1,feed0):
    '''
        和spamTest那个函数不同的地方：
            1、需要通过url来获取数据，不能用文件
            2、去掉高频词的辅助函数
            3、返回的值多些
    '''
    import feedparser
    docList = []
    classList = []
    fullText = []
    minLen = min(len(feed1['entries']),len(feed0['entries']))
    for i in range(minLen):
        wordList = textParse(feed1['entries'][i]['summary'])
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(1)
        wordList = textParse(feed0['entries'][i]['summary'])
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(0)
    vocabList = creatVocabList(docList)
    top10words = calcMostFreq(vocabList,fullText)
    for pairW in top10words:
        if pairW[0] in vocabList:
            vocabList.remove(pairW[0])
    trainingSet = list(range(2*minLen))
    testSet = []
    for i in range(20):
        randIndex = int(np.random.uniform(0,len(trainingSet)))
        testSet.append(trainingSet[randIndex])
        del(trainingSet[randIndex])
    trainMat = []
    trainClasses = []
    for docIndex in trainingSet:
        trainMat.append(bagOfWords2Vec(vocabList,docList[docIndex]))
        trainClasses.append(classList[docIndex])
    p0V,p1V,pSpam = trainNB0(np.array(trainMat),np.array(trainClasses))
    errorCount = 0
    for docIndex in testSet:
        wordVector = bagOfWords2Vec(vocabList,docList[docIndex])
        if classifyNB(np.array(wordVector),p0V,p1V,pSpam) != classList[docIndex]:
            errorCount += 1
    print ('the error rate is:' ,float(errorCount)/len(testSet))
    return vocabList,p0V,p1V


def getTopWords(ny,sf):
    import operator
    vocabList,p0V,p1V = localWords(ny,sf)
    topNY = []
    topSF = []
    for i in range(len(p0V)):
        if p0V[i] > -5.0:
            topSF.append((vocabList[i],p0V[i]))
        if p1V[i] > -5.0:
            topNY.append((vocabList[i],p1V[i]))
    sortedSF = sorted(topSF,key=lambda pair:pair[1],reverse = True)
    print ('-----------SF-------------')
    for item in sortedSF:
        print (item[0])
    sortedNY = sorted(topNY,key=lambda pair:pair[1],reverse = True)
    print ('-----------NY-------------')
    for item in sortedNY:
        print (item[0])
        








