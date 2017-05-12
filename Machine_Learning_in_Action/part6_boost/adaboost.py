 # -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt



def loadSimpData():
    # 用于检测boost的简单函数
    datMat = np.matrix([[1.,2.1],
                        [2.,1.1],
                        [1.3,1.],
                        [1.,1.],
                        [2.,1.]])
    classLabels = [1.0,1.0,-1.0,-1.0,1.0]
    return datMat,classLabels

def stumpClassify(dataMatrix,dimen,threshVal,threshIneq):
    # 通过阈值比较数据进行分类，可以理解为只有一个决策的决策树？,反正就是个弱分类器应该
    retArray = np.ones((np.shape(dataMatrix)[0],1))     # 生成一个和样本数一样的数组
    if threshIneq == 'lt':
        retArray[dataMatrix[:,dimen] <= threshVal] = -1.0
    else:
        retArray[dataMatrix[:,dimen] > threshVal] = -1.0
    return retArray

def buildStump(dataArr,classLabels,D):
    # 基于加权输入值进行决策的分类器
    dataMatrix = np.mat(dataArr)
    labelMat = np.mat(classLabels).T
    m,n = np.shape(dataMatrix)
    numSteps = 10.0     # 特征所有可能值得分母
    bestStump = {}      # 存储给定权重向量D后，最佳单层决策树的相关信息
    bestClassEst = np.mat(np.zeros((m,1)))      # 生成和样本数一样的矩阵
    minError = np.inf   # 正无穷
    for i in range(n):      # 循环所有的数据维度
        rangeMin = dataMatrix[:,i].min()
        rangeMax = dataMatrix[:,i].max()
        stepSize = (rangeMax-rangeMin)/numSteps     # 步长
        for j in range(-1,int(numSteps)+1):         # 遍历当前特征下所有可能的值
            for inequal in ['lt','gt']:             # what is this...
                threshVal = (rangeMin+float(j)*stepSize)    # 初始化阈值？
                predictedVals = stumpClassify(dataMatrix,i,threshVal,inequal)
                errArr = np.mat(np.ones((m,1)))
                errArr[predictedVals == labelMat] = 0       # 预测对的等于0
                weightedError = D.T*errArr          # 计算加权错误率
                print ('split:dim %d , thresh %.2f , thresh inequal:%s , the weighted error is %.3f'% (i,threshVal,inequal,weightedError))
                if weightedError < minError:        # 误差低于正无穷(这个正无穷会被替换掉)
                    minError = weightedError
                    bestClassEst = predictedVals.copy()
                    bestStump['dim'] = i            # 最佳的用于分类的特征
                    bestStump['thresh'] = threshVal     # 分类特征的值应该取多少
                    bestStump['ineq'] = inequal     # ['lt','gt']应该是特征名称？
    return bestStump,minError,bestClassEst
    
def adaBoostTrainDS(dataArr,classLabels,numIt=40):
    # 完整的adaboost算法
	weakClassArr = []
	m = np.shape(dataArr)[0]       # 样本数
	D = np.mat(np.ones((m,1))/m)   # 初始化加权矩阵
	aggClassEst = np.mat(np.zeros((m,1)))
	for i in range(numIt):     # 进入迭代
		bestStump,error,ClassEst = buildStump(dataArr,classLabels,D)  # 建立树桩
		print ('D:',D.T)
		alpha = float(0.5*np.log((1.0-error)/max(error, 1e-16)))      # 初始化a--分类器的权重
		bestStump['alpha'] = alpha
		weakClassArr.append(bestStump)        # 把树桩的相关信息保存进一个数组
		print ('classEst:',ClassEst.T)        # 打印当前树桩的分类结果 
        # 为下一次迭代计算D，D应该是一个分布才对呀~~~上一次分类正确的，下一次权重会为0
		expon = np.multiply(-1*alpha*np.mat(classLabels).T,ClassEst)      
		D = np.multiply(D,np.exp(expon))
		D = D/D.sum()
		aggClassEst += alpha*ClassEst         # 记录每个数据点的估计类别，等下和真实的类别的符号比较用
		print ('aggClassEst:',aggClassEst.T)
		aggErrors = np.multiply(np.sign(aggClassEst) != np.mat(classLabels).T,np.ones((m,1))) #计算权重
		errorRate = aggErrors.sum()/m
		print ('total error:',errorRate)
		if errorRate==0.0:    # 退出条件
		    break
	return weakClassArr,aggClassEst        # aggClassEst为了画图用的


def adaClassify(datToClass,classifierArr):
    # 基于上面的boosting来分类测试数据
	dataMatrix = np.mat(datToClass)
	m = np.shape(dataMatrix)[0]
	aggClassEst = np.mat(np.zeros((m,1)))  # 和boosting最后一步的作用一直，存放叫做符号的东西吧算是
	for i in range(len(classifierArr)):    # 遍历基分类器的数量
		classEst = stumpClassify(dataMatrix,
                           classifierArr[i]['dim'],
                           classifierArr[i]['thresh'],
                           classifierArr[i]['ineq'])    # 对每个分类器调用，得到一个估计值
		aggClassEst += classifierArr[i]['alpha']*classEst
		print (aggClassEst)   # 打印变化情况
	return np.sign(aggClassEst)    # 返回符号，大于0则是1，小于0则是-1
    
    
def loadDataSet(filename):
	numFeat = len(open(filename).readline().split('\t'))   # 读取文件，获取特征数
	dataMat = []
	labelMat = []
	fr = open(filename)
	for line in fr.readlines():
		lineArr = []
		curLine = line.strip().split('\t')        # 去掉空格和换行
		for i in range(numFeat -1):       
			lineArr.append(float(curLine[i]))            # 生成每个样本
		dataMat.append(lineArr)                           # 生成训练集
		labelMat.append(float(curLine[-1]))               # 生成标签
	return dataMat,labelMat


def plotROC(predStrengths,classLabels):
    # ROC曲线绘制及AUC计算
    cur = (1.0,1.0)
    ySum = 0.0      # 计算AUC的
    numPosClas = sum(np.array(classLabels) == 1.0)
    yStep = 1/float(numPosClas)
    xStep = 1/float(len(classLabels) - numPosClas)
    sortedIndicies = predStrengths.argsort()
    fig = plt.figure()
    fig.clf()
    ax = plt.subplot(111)
    for index in sortedIndicies.tolist()[0]:
        if classLabels[index] == 1.0:
            delX = 0
            delY = yStep
        else:
            delX = xStep
            delY = 0
            ySum += cur[1]
        ax.plot([cur[0],cur[0]-delX],[cur[1],cur[1]-delY],c='b')
        cur = (cur[0]-delX,cur[1]-delY)
    ax.plot([0,1],[0,1],'b--')
    plt.xlabel('false positive rate')
    plt.ylabel('true positive rate')
    plt.title('ROC curve for adaboost horse colic detection system')
    ax.axis([0,1,0,1])
    plt.show()
    print ('the area under the curve is :',ySum*xStep)

        





