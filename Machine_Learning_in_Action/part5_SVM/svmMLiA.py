# -*- coding: utf-8 -*-
"""
Created on Thu May  4 15:26:58 2017

@author: kaifeng
"""

import numpy as np
import scipy as sp

def loadData(fileName):
    # 读取数据的函数
    dataMat = []
    labelMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr = line.strip().split('\t')
        dataMat.append([float(lineArr[0]),float(lineArr[1])])
        labelMat.append(float(lineArr[2]))
    return dataMat,labelMat

def selectJrand(i,m):
    # 随机给出а的下标
    j = i
    while (j==i):
        j = int(np.random.uniform(0,m))     # m是а的数量
    return j

def clipAlpha(aj,H,L):
    '''
        函数是用于调整大于H或小于L的а值
                | H                 if a_new > H
        а_new = | a_new_边界        if L<= a_new <= H
                | L                 uf a_new < L    
    '''
    if aj > H:
        aj = H
    if L > aj:
        aj = L
    return aj


def smoSimple(dataMatIn,classLabels,C,toler,maxIter):
    dataMatrix = sp.mat(dataMatIn)                  # 矩阵化，方便计算
    labelMat = sp.mat(classLabels).transpose()     # 矩阵化、转置
    b = 0                                           # SVM中的一个参数，类似于截距
    m,n = np.shape(dataMatrix)                      # m是样本数，n是特征数
    alphas = sp.mat(np.zeros((m,1)))                # SVM中另一个参数，是一个矩阵
    iterm = 0                                       # 控制迭代的
    while(iterm < maxIter):
        alphaPairsChanged = 0                       # SMO算法是一次改变两个a的
        for i in range(m):
            # sp.multiply是矩阵元素之间的乘法，不是矩阵乘法
            fXi = sp.float64(sp.multiply(alphas,labelMat).T * (dataMatrix*dataMatrix[i,:].T)) + b # 计算预测值
            Ei = fXi - sp.float64(labelMat[i])         # 计算误差
            if ((labelMat[i]*Ei < -toler).all() and (alphas[i] < C)) or ((labelMat[i]*Ei > toler).all() and (alphas[i] > 0)):  # 如果参数а可以改进则进入流程
                j = selectJrand(i,m)    # 随机选取第二个参数а，其实应该用启发式的决策而不是随机
                fXj = sp.float64(sp.multiply(alphas,labelMat).T * (dataMatrix*dataMatrix[j,:].T)) + b # 计算预测值
                Ej = fXj - sp.float64(labelMat[j])     # 计算误差
                alphaIold = alphas[i].copy()        # 记录下来两个参数的这次修改前的值
                alphaJold = alphas[j].copy()
                if (labelMat[i] != labelMat[j]):
                    L = max(0,alphas[j]-alphas[i])  # 计算L和H，其实这两个应该用另外的方式计算，作用是保证а在[0,C]范围内
                    H = min(C,C+alphas[j]-alphas[i])
                else:
                    L = max(0,alphas[j]+alphas[i]-C)
                    H = min(C,alphas[j]+alphas[i])
                if L==H: print ('L==H') ;continue        # 直接进入下次for循环
                # 参数更新公式：a_new = a + y(Ei-Ej)/η    eta=η
                eta = 2.0 * dataMatrix[i,:]*dataMatrix[j,:].T - dataMatrix[i,:]*dataMatrix[i,:].T - dataMatrix[j,:]*dataMatrix[j,:].T
                if eta >= 0: print ('eta>=0') ;continue
                alphas[j] -= labelMat[j]*(Ei-Ej)/eta           # 更新一
                alphas[j] = clipAlpha(alphas[j],H,L)            # 更新二，是否超出边界看
                if (abs(alphas[j] - alphaJold) < 0.00001): print ('j not moving enough') ;continue
                alphas[i] += labelMat[j] * labelMat[i] * (alphaJold-alphas[j])    # i的更新公式 a_new  = a_old+y1*y2*(aj-a_更新二后)
                
                # 参数b的更新公式和满足条件
                b1 = b - Ei - labelMat[i]*(alphas[i] - alphaIold)*dataMatrix[i,:]*dataMatrix[i,:].T - labelMat[j]*(alphas[j]-alphaJold)*dataMatrix[i,:]*dataMatrix[j,:].T
                b2 = b - Ej - labelMat[i]*(alphas[i] - alphaIold)*dataMatrix[i,:]*dataMatrix[j,:].T - labelMat[j]*(alphas[j]-alphaJold)*dataMatrix[j,:]*dataMatrix[j,:].T
                if (0 < alphas[i]) and (C > alphas[i]):
                    b = b1
                elif(0 < alphas[j]) and (C > alphas[j]):
                    b = b2
                else:
                    b = (b1+b2)/2.0
                
                alphaPairsChanged += 1
                print ("iter: %d i:%d, pairs changed %d" % (iterm,i,alphaPairsChanged))
        if (alphaPairsChanged == 0):
            iterm += 1
        else:
            iterm = 0
        print ("iteration number: %d" % iterm)
    return b,alphas
    

# 以下这些是为了优化处理速度的辅助函数
class optStruct(object):
    def __init__(self,dataMatIn,classLabels,C,toler,kTup):
        self.X = dataMatIn
        self.labelMat = classLabels
        self.C = C
        self.tol = toler
        self.m = np.shape(dataMatIn)[0]
        self.alphas = sp.mat(sp.zeros((self.m,1)))
        self.b = 0
        self.eCache = sp.mat(sp.zeros((self.m,2)))      # 这就缓存了？第一列是标示为，记录是否有效，第二列是实际E
        self.K = sp.mat(np.zeros((self.m,self.m)))
        for i in range(self.m):
            self.K[:,i] = kernelTrans(self.X,self.X[i,:],kTup)  # 因为在计算中有很多要用到的地方，所以也存一下
        
        

def calcEk(oS,k):
    # 计算误差，对于a确定的
    fXk = sp.float64(sp.multiply(oS.alphas,oS.labelMat).T * oS.K[:,k] + oS.b)
    Ek = fXk - sp.float64(oS.labelMat[k])
    return Ek

def selectJ(i,oS,Ei):
    # 吴老师曾经提到过的启发式的算法
    maxK = -1
    maxDeltaE = 0
    Ej = 0
    oS.eCache[i] = [1,Ei]
    valiEcacheList = sp.nonzero(oS.eCache[:,0].A)[0]  # 构建一个非零列表，就是非零的a的列表
    if len(valiEcacheList) > 1:
        for k in valiEcacheList:
            if k == i:
                continue
            Ek = calcEk(oS,k)
            deltaE = abs(Ei - Ek)   
            if (deltaE > maxDeltaE):    # 选择具有最大的步长的j
                maxK = k
                maxDeltaE = deltaE
                Ej = Ek
        return maxK,Ej
    else:
        j = selectJrand(i,oS.m)         # 如果是第一个就用传统的随机
        Ej = calcEk(oS,j)
    return j,Ej

def updateEk(oS,k):
    # 把新的误差值存入缓存中
    Ek = calcEk(oS,k)
    oS.eCache[k] = [1,Ek]


def innerL(i,oS):
    # 和smoSimple基本上差不多的
    # 不同的地方是用了自己定义的数据结构通过oS传递，之后用selectJ不用随机选择
    Ei = calcEk(oS,i)
    if ((oS.labelMat[i]*Ei < -oS.tol).all() and (oS.alphas[i] < oS.C)) or ((oS.labelMat[i]*Ei > oS.tol).all() and (oS.alphas[i] > 0)):
        j,Ej = selectJ(i,oS,Ei)
        alphaIold = oS.alphas[i].copy()
        alphaJold = oS.alphas[j].copy()
        if (oS.labelMat[i] != oS.labelMat[j]):
            L = max(0,oS.alphas[j]-oS.alphas[i])  
            H = min(oS.C,oS.C+oS.alphas[j]-oS.alphas[i])
        else:
            L = max(0,oS.alphas[j]+oS.alphas[i]-oS.C)
            H = min(oS.C,oS.alphas[j]+oS.alphas[i])
        if L==H: print ('L==H') ;return 0
        eta = 2.0 * oS.K[i,j] - oS.K[i,j] - oS.K[j,j]
        if eta >= 0:print ('eta>=0') ; return 0
        oS.alphas[j] -= oS.labelMat[j]*(Ei-Ej)/eta
        oS.alphas[j] = clipAlpha(oS.alphas[j],H,L)
        updateEk(oS,j)        # 更新缓存
        if (abs(oS.alphas[j] - alphaJold) < 0.00001): print ('j not moving enough') ;return 0
        oS.alphas[i] += oS.labelMat[j] * oS.labelMat[i] * (alphaJold-oS.alphas[j])
        updateEk(oS,i)          # 更新缓存
        b1 = oS.b - Ei - oS.labelMat[i]*(oS.alphas[i] - alphaIold)*oS.K[i,i] - oS.labelMat[j]*(oS.alphas[j]-alphaJold)*oS.K[i,j]
        b2 = oS.b - Ej - oS.labelMat[i]*(oS.alphas[i] - alphaIold)*oS.K[i,j] - oS.labelMat[j]*(oS.alphas[j]-alphaJold)*oS.K[j,j]
        if (0 < oS.alphas[i]) and (oS.C > oS.alphas[i]):
            oS.b = b1
        elif(0 < oS.alphas[j]) and (oS.C > oS.alphas[j]):
            oS.b = b2
        else:
            oS.b = (b1+b2)/2.0
        return 1
    else:
        return 0


def smoP(dataMatIn,classLabels,C,toler,maxIter,kTup=('normal',0)):
    # 对应的外层循环，和smoSimple是类似的，不同的是退出循环的条件更多了，貌似迭代6次左右就停止了。
    oS = optStruct(sp.mat(dataMatIn),sp.mat(classLabels).transpose(),C,toler,kTup)
    iterm = 0
    entireSet = True
    alphaPairsChanged = 0
    while (iterm < maxIter) and ((alphaPairsChanged>0) or (entireSet)):
        alphaPairsChanged = 0
        if entireSet:
            for i in range(oS.m):       # 遍历所有的值，找第一个a
                alphaPairsChanged += innerL(i,oS)   # 找第二个a
                print("fullSet, iter: %d i:%d, pairs changed %d" % (iterm,i,alphaPairsChanged))
            iterm += 1
        else:       # 遍历非边界的值，找第一个a，就是0<a<c那个正方形中的
            nonBoundIs = sp.nonzero((oS.alphas.A > 0) * (oS.alphas.A < C))[0]
            for i in nonBoundIs:
                alphaPairsChanged += innerL(i,oS) # 找第二个
                print ("non-bound, iter: %d i:%d, pairs changed %d" % (iterm,i,alphaPairsChanged))
            iterm += 1
        if entireSet:   # 控制在边界和非边界循环切换
            entireSet = False
        elif (alphaPairsChanged ==0):
            entireSet = True
        print ("iteration number: %d" % iterm)
    return oS.b,oS.alphas

def calcWs(alphas,dataArr,classLabels):
    # 计算w的，就是a的集合和数据集结合处的结果
    X = sp.mat(dataArr)
    labelMat = sp.mat(classLabels).transpose()
    m,n = np.shape(X)
    w = np.zeros((n,1))
    for i in range (m):
        w += sp.multiply(alphas[i] * labelMat[i],X[i,:].T)
    return w


def kernelTrans(X,A,kTup):
    # 把之前的X和X.T的全部替换掉记得~
    m,n = np.shape(X)
    K = sp.mat(np.zeros((m,1)))
    if kTup[0] == 'normal':     # 正常的线性核?
        K = X * A.T
    elif kTup[0] == 'Gauss':    # 高斯核
        for j in range(m):
            deltaRow = X[j,:] - A
            K[j] = deltaRow*deltaRow.T
        K = sp.exp(K/(-1*kTup[1]**2)) # 元素间的除法
    else:           # 不理解的
        raise NameError('this kernel i dont understand')
    return K

def testGauss(k1=1.3):
    dataArr,labelArr = loadData('testSetRBF.txt')
    
    # 训练，得到参数
    b,alphas = smoP(dataArr,labelArr,200,0.0001,10000,('Gauss',k1))
    datMat = sp.mat(dataArr)
    labelMat = sp.mat(labelArr).transpose()
    svInd = sp.nonzero(alphas.A > 0)[0]     # 支持向量的矩阵
    sVs = datMat[svInd]
    labelSV = labelMat[svInd]
    print ("there are %d Support Vectors" % np.shape(sVs)[0])
    m,n = np.shape(datMat)
    errorCount = 0
    for i in range(m):
        kernelEval = kernelTrans(sVs,datMat[i,:],('Gauss',k1))
        predict = kernelEval.T * (sp.multiply(labelSV,alphas[svInd])) + b
        if np.sign(predict) != np.sign(labelArr[i]):
            errorCount += 1
    print("the training error rate is: %f" % (float(errorCount)/m))
    
    # 测试参数在新数据上如何
    dataArr,labelArr = loadData('testSetRBF2.txt')
    errorCount = 0
    datMat = sp.mat(dataArr)
    labelMat = sp.mat(labelArr).transpose()
    m,n = np.shape(datMat)
    for i in range(m):
        kernelEval = kernelTrans(sVs,datMat[i,:],('Gauss',k1))
        predict = kernelEval.T * (sp.multiply(labelSV,alphas[svInd])) + b
        if np.sign(predict) != np.sign(labelArr[i]):
            errorCount += 1
    print("the test error rate is: %f" % (float(errorCount)/m))

def img2vector(filename):
    returnVect = np.zeros((1,1024))         # 生成一个要返回的向量，因为32*32=1024
    fr = open(filename)
    for i in range(32):                 # i控制列向下
        lineStr = fr.readline()
        for j in range(32):             # j控制行向前
            returnVect[0,32*i+j] = int(lineStr[j])
    return returnVect

def loadImage(dirName):
    from os import listdir
    hwLabels = []
    trainingFileList = listdir(dirName)           #读取整个文件夹中的内容
    m = len(trainingFileList)
    trainingMat = np.zeros((m,1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]     #去掉.txt
        classNumStr = int(fileStr.split('_')[0])    #去掉_后面的
        if classNumStr == 9:
            hwLabels.append(-1)
        else:
            hwLabels.append(1)
        trainingMat[i,:] = img2vector('%s/%s' % (dirName,fileNameStr))
    return trainingMat,hwLabels
        
def testDigits(kTup = ('normal',10)):
    # 和testGauss基本上差不多也
    dataArr,labelArr = loadImage('trainingDigits')
    b,alphas = smoP(dataArr,labelArr,200,0.0001,10000,kTup)
    datMat = sp.mat(dataArr)
    labelMat = sp.mat(labelArr).transpose()
    svInd = sp.nonzero(alphas.A > 0)[0]     # 支持向量的矩阵
    sVs = datMat[svInd]
    labelSV = labelMat[svInd]
    print ("there are %d Support Vectors" % np.shape(sVs)[0])
    m,n = np.shape(datMat)
    errorCount = 0
    for i in range(m):
        kernelEval = kernelTrans(sVs,datMat[i,:],kTup)
        predict = kernelEval.T * (sp.multiply(labelSV,alphas[svInd])) + b
        if np.sign(predict) != np.sign(labelArr[i]):
            errorCount += 1
    print("the training error rate is: %f" % (float(errorCount)/m))
    
    # 测试参数在新数据上如何
    dataArr,labelArr = loadImage('testDigits')
    errorCount = 0
    datMat = sp.mat(dataArr)
    labelMat = sp.mat(labelArr).transpose()
    m,n = np.shape(datMat)
    for i in range(m):
        kernelEval = kernelTrans(sVs,datMat[i,:],kTup)
        predict = kernelEval.T * (sp.multiply(labelSV,alphas[svInd])) + b
        if np.sign(predict) != np.sign(labelArr[i]):
            errorCount += 1
    print("the test error rate is: %f" % (float(errorCount)/m))







