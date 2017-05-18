# -*- coding: utf-8 -*-
"""
Created on Wed May 17 17:31:05 2017

@author: 凯风
"""


import numpy as np
from imp import reload
import svdRec

# SVD的矩阵分解，Data(m*n) = U(m*m) * Σ(m*n) * V^T(n*n)
U,Sigma,VT = np.linalg.svd([[1,1],[7,7]])   
U
Sigma   # 为啥不是2*2呢？因为Σ除了对角线外都是0，这样子可以节省空间吧
VT
data = svdRec.loadExData()
U,Sigma,VT = np.linalg.svd(data)    # 在一个稍微大点的数据集上看看效果
Sigma   
# 前三个数值明显大于后两个，数量及上差太多了~
# 所以呢？原数据集可以用Data(m*n) = U(m*3) * Σ(3*3) * V^T(3*n) 来近似？
Sig3 = np.mat([[Sigma[0],0,0],[0,Sigma[1],0],[0,0,Sigma[2]]])
U[:,:3]*Sig3*VT[:3,:]   # 之后就用这个了？


reload(svdRec)
myMat = np.mat(svdRec.loadExData())
# 以下都是查看列向量的相似度
svdRec.eculidSim(myMat[:,0],myMat[:,4])     # 欧氏距离 
svdRec.eculidSim(myMat[:,0],myMat[:,0]) 
svdRec.cosSim(myMat[:,0],myMat[:,4])        # 余弦相似度
svdRec.cosSim(myMat[:,0],myMat[:,0])
svdRec.pearsSim(myMat[:,0],myMat[:,4])      # 皮尔逊相关系数
svdRec.pearsSim(myMat[:,0],myMat[:,0])
'''
    *关于是用列向量还是行向量的问题*
    如果m>>n，也就是样本数大于特征数，则用列向量进行计算相似度，因为减少计算量
    如果m<<n，也就是样本数小于特征数，则用行向量进行计算相似度，也是节省
'''


reload(svdRec)
myMat = np.mat(svdRec.loadExData())
myMat[0,1] = myMat[0,0] = myMat[1,0] = myMat[2,0] = 4
myMat[3,3] = 2
myMat
svdRec.recommend(myMat,2)       # 用户2，未评分的商品的评分情况，元组中第一个是商品ID，第二个是评分
svdRec.recommend(myMat,2,simMeas=svdRec.eculidSim)      # 换一下相关度计算方法
svdRec.recommend(myMat,2,simMeas=svdRec.pearsSim)

# 利用SVD
reload(svdRec)
U,Sigma,VT = np.linalg.svd(np.mat(svdRec.loadExData2()))
Sigma
Sig2 = Sigma ** 2   # 查看多少个奇异值能达到总“能量”的90%
sum(Sig2)
sum(Sig2) * 0.9
sum(Sig2[:2])
sum(Sig2[:3])   # 前三个元素即可了，所以可以把11维的数据压缩成3维


reload(svdRec)
myMat = np.mat(svdRec.loadExData2())
svdRec.recommend(myMat,1,estMethod=svdRec.svdEst)        # 利用SVD来进行评分评估
svdRec.recommend(myMat,1,estMethod=svdRec.svdEst,simMeas=svdRec.pearsSim)   # 换一种相似度计算方法


reload(svdRec)
svdRec.imgCompress(2)   # 压缩图片














