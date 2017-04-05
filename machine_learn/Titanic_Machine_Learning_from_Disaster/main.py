# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 15:25:53 2017

@author: kaifeng
"""

# 导入库
import pandas as pd
import numpy as np
import random as rnd

import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC,LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import Perceptron  #感知器
from sklearn.linear_model import  SGDClassifier
from sklearn.tree import DecisionTreeClassifier


#导入数据
train_df = pd.read_csv('C:/Users/carne/Desktop/train.csv')
test_df = pd.read_csv('C:/Users/carne/Desktop/test.csv')

#查看训练集的features
print (train_df.columns.values)
train_df.head() #前五行
train_df.tail() #后五行

#查看数据类型
train_df.info()
test_df.info()

#查看统计数据
train_df.describe()
train_df.describe(include = ['O'])
'''
1、可能会删除掉Ticket 这个特征，因为票号对预测没有什么作用，而且票号的样本数量应该和总数一样，但是重复性居然有210个
2、Cabin因为有太多的缺失值也可能去掉
3、PassengerId也可能没什么用丢掉
4、名字对是否生存来说也没什么卵用
'''

'''
根据kaggle的说明可能有一下几个feature对生存影响较大
    1、性别=female的生存下去的几率更高？
    2、年龄小于<N的生存下去的几率更高？
    3、Pclass低的，买的票好，所以几率更高？
    验证一下猜想
'''

train_df[['Pclass','Survived']].groupby(['Pclass'],as_index=False).mean().sort_values(by='Survived',ascending=False)
# 1的概率0.629630     2的概率0.472826      3的概率0.242363   

train_df[['Sex','Survived']].groupby(['Sex'],as_index=False).mean().sort_values(by='Survived')
# male生存的概率0.188908     female的概率0.742038

train_df[['SibSp','Survived']].groupby(['SibSp'],as_index=False).mean().sort_values(by='Survived',ascending=False)
# 是否有兄弟姐妹好像没有什么帮助  字段里面还包含配偶，所以也不好说

train_df[["Parch", "Survived"]].groupby(['Parch'], as_index=False).mean().sort_values(by='Survived', ascending=False)
#　是否有父母小孩的好像也没有什么帮助



#可视化的方法查看数据的相关信息
g = sns.FacetGrid(train_df,col = 'Survived')
g.map(plt.hist,'Age',bins = 20)
'''
观察图像好像可能看出：
    1、年级比较小于4岁的存活的概率挺高的（一根柱子是4岁的区间）
    2、80左右的都活了下来
    3、大多数的年级在15-35左右
'''

grid = sns.FacetGrid(train_df, col ='Survived', row ='Pclass' ,size=2.2, aspect=1.6)
grid.map(plt.hist,'Age',alpha = 0.5,bins = 20)
grid.add_legend()
'''
观察图像好像可能看出：
    1、Pclass=3的存活几率非常低
    2、Pclass=2和3中，年龄小的也活下来挺多
    3、Pclass=1的存活几率挺高的
'''

grid2 = sns.FacetGrid(train_df,row = 'Embarked' , size = 2.2 ,aspect = 1.6)
grid2.map(sns.pointplot,'Pclass','Survived','Sex',palette = 'deep')
grid2.add_legend()
'''
观察图像好像可能看出：
    1、除了第二个登录点外，女的生存几率挺高
    2、不同的登录点可能有不同的关联性，所以把这个feature也考虑进去吧
'''


grid3 = sns.FacetGrid(train_df,row = 'Embarked',col = 'Survived' , size=2.2 , aspect = 1.6)
grid3.map(sns.barplot,'Sex','Fare',alpha = 0.5 , ci = None)
grid3.add_legend()
'''
观察图像好像可能看出：
    1、票价高的存活几率大点
    2、好像确实登录点与生存有点关系
'''


# 基于以上的这些观察，对数据集做一些处理，删除一些没用的，创造一些更好的feature
# 注意点就是要保证测试集和训练集同步
train_df = train_df.drop(['Ticket','Cabin'],axis = 1)
test_df =test_df.drop(['Ticket','Cabin'],axis = 1)


# 确定一下names和passengerID是否可以删除
combine = [train_df,test_df]
for dataset in combine:
    #把名字中的Mr等内容根据正则选出来
    dataset['Title'] = dataset.Name.str.extract('([A-Za-z]+)\.',expand=False)
pd.crosstab(train_df['Title'],train_df['Sex'])

# 替换title的字段，把稀有度较低的结合成一类
for dataset in combine:
    dataset['Title'] = dataset['Title'].replace(['Lady', 'Countess','Capt', 'Col',\
 	'Don', 'Dr', 'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona'],'Rare')
    dataset['Title'] = dataset['Title'].replace('Mlle','Miss')
    dataset['Title'] = dataset['Title'].replace('Ms','Miss')
    dataset['Title'] = dataset['Title'].replace('Mme','Mrs')

train_df[['Title','Survived']].groupby(['Title'],as_index=False).mean()

# 把字符串转化成标称数据
title_mapping = {'Mr':1,'Miss':2,'Mrs':3,'Master':4,'Rare':5}
for dataset in combine:
    dataset['Title'] = dataset['Title'].map(title_mapping)
    dataset['Title'] = dataset['Title'].fillna(0)     #处理缺失值

train_df = train_df.drop(['Name','PassengerId'],axis=1)
test_df = test_df.drop(['Name'], axis=1)
combine = [train_df,test_df]

# 把sex也转化成标称数据把
set_mapping = {'female':1,'male':0}
for dataset in combine:
    dataset['Sex'] = dataset['Sex'].map(set_mapping).astype(int)
        
# 还要处理一下Age中的缺失数据0_0
grid4 = sns.FacetGrid(train_df,row = 'Pclass',col = 'Sex',size = 2.2 , aspect = 1.6)
grid4.map(plt.hist,'Age',alpha = 0.5 , bins = 20)
grid4.add_legend()

# 用Pclass和Sex来随机给出比较好
guess_ages = np.zeros((2,3))
for dataset in combine:
    for i in range(0,2):     # 性别只有两个
        for j in range (0,3): #仓位有三个值
            guess_df =dataset[(dataset['Sex'] == i) & (dataset['Pclass'] == j+1)]['Age'].dropna()
            age_guess = guess_df.median()
            guess_ages[i,j] = int(age_guess/0.5+0.5)*0.5 # 数据集中有.5
    for i in range(0,2):
        for j in range (0,3):
            dataset.loc[(dataset.Age.isnull()) & (dataset.Sex == i) & (dataset.Pclass == j+1),'Age'] = guess_ages[i,j]
    dataset['Age'] = dataset['Age'].astype(int)

# 把处理好的Age feature 转化成区间属性类型~
train_df['AgeBand'] = pd.cut(train_df['Age'],5)

#看下效果如何
train_df[['AgeBand','Survived']].groupby(['AgeBand'],as_index=False).mean().sort_values(by='AgeBand',ascending = True)

# 再把区间类型的转化成标称类型的....
for dataset in combine:
    dataset.loc[dataset['Age'] <= 16,'Age'] = 0
    dataset.loc[(dataset['Age']>16) & (dataset['Age']<=32) ,'Age'] = 1
    dataset.loc[(dataset['Age']>32) & (dataset['Age']<=48) ,'Age'] = 2
    dataset.loc[(dataset['Age']>48) & (dataset['Age']<=64) ,'Age'] = 3
    dataset.loc[dataset['Age']>64,'Age'] = 4
    
# 删除掉ageband
train_df = train_df.drop(['AgeBand'],axis=1)
combine = [train_df,test_df]

# 把兄弟姐妹数量和父母子女数量结合在一起组成新的变量
for dataset in combine:
    dataset['FamilySize'] = dataset['SibSp'] + dataset['Parch'] + 1
    
# 看看数据如何
train_df[['FamilySize','Survived']].groupby(['FamilySize'],as_index=False).mean().sort_values(by='Survived',ascending = True)

# 这个数据再变一下变成是否单身，根据FamilySize ？= 1
for dataset in combine:
    dataset['IsAlone'] = 0
    dataset.loc[dataset['FamilySize'] == 1 , 'IsAlone'] = 1
    
# 看看数据如何
train_df[['IsAlone','Survived']].groupby(['IsAlone'],as_index=False).mean()

# 删掉没用的feature
train_df = train_df.drop(['SibSp','Parch','FamilySize'],axis=1)
test_df = test_df.drop(['SibSp','Parch','FamilySize'],axis=1)
combine = [train_df,test_df]

# 把登录口的字符串数据缺失值填上，并且变成数值型
freq_port = train_df.Embarked.dropna()[0]
for dataset in combine:
    dataset['Embarked'] = dataset['Embarked'].fillna(freq_port)
for dataset in combine:
    dataset['Embarked'] = dataset['Embarked'].map({'S':0,'C':1,'Q':2}).astype(int)
    
# 处理一下船票价格的缺失值
test_df['Fare'].fillna(test_df['Fare'].dropna().median(),inplace = True)

# 把船票价格的类型转化为标称型
train_df['FareBand'] = pd.qcut(train_df['Fare'],4)
train_df[['FareBand','Survived']].groupby(['FareBand'],as_index=False).mean().sort_values(by='FareBand',ascending=True)
for dataset in combine:
    dataset.loc[ dataset['Fare'] <= 7.91, 'Fare'] = 0
    dataset.loc[(dataset['Fare'] > 7.91) & (dataset['Fare'] <= 14.454), 'Fare'] = 1
    dataset.loc[(dataset['Fare'] > 14.454) & (dataset['Fare'] <= 31), 'Fare']   = 2
    dataset.loc[ dataset['Fare'] > 31, 'Fare'] = 3
    dataset['Fare'] = dataset['Fare'].astype(int)
train_df = train_df.drop(['FareBand'],axis=1)
combine = [train_df,test_df]


# 模型环节啦~
X_train = train_df.drop('Survived',axis = 1)
Y_train = train_df['Survived']
X_test = test_df.drop('PassengerId',axis = 1).copy()

# logistic regression














