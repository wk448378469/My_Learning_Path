# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 13:42:12 2017

@author: kaifeng
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression          #导入模型包
from sklearn.cross_validation import train_test_split          #划分训练集和测试集的包
from sklearn.preprocessing import StandardScaler              # 数据标准化的包
from sklearn.metrics import precision_recall_curve,classification_report,roc_auc_score      #评估模型的包
import matplotlib.pyplot as plt                             # 画图包
import seaborn as sns
from sklearn.grid_search import GridSearchCV         # 导入交叉验证的包

df = pd.read_csv('C:/Users/carne/Desktop/adultTest.csv')

df.head()

#将字符串型数据转化为数值型数据 —— one hot code 独热码，就是对应的feature转变为0和1的数据框
df_new = pd.get_dummies( data = df , columns = ['workclass','education','marital-status', 'occupation', 'relationship', 'race', 'sex','native-country'])

#对class做些处理，把空格什么的去掉
df_new['class'] = df['class'].map(lambda s : s.strip(" "))


#创建一个新的列，用来对class做区分
df_new.loc[df_new['class'] == '<=50K','label'] = 0
df_new.loc[df_new['class'] != '<=50K','label'] = 1

#划分数据集
X = df_new.drop(['class','label'],axis = 1)
y = df_new['label']

#把X的缺失值补上
X.fillna( 0 , inplace = 0)

# 划分训练集和测试集
trainX,testX,trainY,testY = train_test_split(X,y,train_size = 0.7)

# 数据的标准化（线性模型中，有很多大的值会影响到模型，而那些one hot code 的feature则影响的很小）
std = StandardScaler() 
std.fit(trainX)
trainX_std = std.transform(trainX)
testX_std = std.transform(testX)

'''
标准化的计算公式:
    当前的feature的值-feature的平均值)/feature的标准差
注意事项：
    一定要在训练集上做标准化，在测试集上做应用
    
'''
#model A 未标准化
lr = LogisticRegression()      #创建一个对象
lr.fit(trainX,trainY)              #训练模型
lr.score(testX,testY)                 # 准确度
proba = lr.predict_proba(testX)[:,1]         # 获取模型0和1的概率，并且取出来true的

#model B 标准化
lr = LogisticRegression()
lr.fit(trainX_std,trainY) 
lr.score(testX_std,testY)         
proba1 = lr.predict_proba(testX_std)[:,1]


# 评估模型
precision,recall,thresholds = precision_recall_curve(testY,proba)
precision1,recall1,thresholds1 = precision_recall_curve(testY,proba1)


plt.plot(recall,precision,label = 'no std')       # 看recall和precision的走势图
plt.plot(recall1,precision1,label ='with std')
plt.xlabel("recall")
plt.ylabel("precision")
plt.legend()
 
print(classification_report(testY,lr.predict(testX)))         # 看一下F1值
print(classification_report(testY,lr.predict(testX_std)))         # 看一下F1值

print (roc_auc_score(testY,proba))                                # 看一下auc的面积
print (roc_auc_score(testY,proba1))                               # 看一下auc的面积




# model的交叉验证~
param = {'C':[0.001,0.01,0.1,1,10],'max_iter':[100,250]}
clf =GridSearchCV(lr,param,cv = 5,n_jobs = -1,verbose = 1,scoring='roc_auc')
clf.fit(trainX_std,trainY)

clf.grid_scores_       #查看每一组结果
clf.best_params_      #最佳参数组合

#{'C': 0.1, 'max_iter': 100} 这个组合最好，然后去测试集上试一下看有没有提升
lr2 = LogisticRegression(C = 0.1 ,max_iter = 100 )
lr2.fit(trainX_std,trainY) 
lr2.score(testX_std,testY)          # 好像高了那么一点点~
