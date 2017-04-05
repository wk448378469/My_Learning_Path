# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 11:46:49 2017

@author: kaifeng
"""

# 这一章节里面涉及到太多的XML的解析了，下载数据又有很多G，战略性放弃先。
from sklearn import neighbors
knn = neighbors.KNeighborsClassifier(n_neighbors = 2)
print (knn)

X = [[1],[2],[3],[4],[5],[6]]
y = [0,0,0,1,1,1]

knn.fit(X,y)
knn.predict(1.5)
knn.predict(37)
knn.predict(3)

knn.predict_proba(1.5)
knn.predict_proba(37)
knn.predict_proba(-1)

from sklearn.linear_model import LogisticRegression
clf = LogisticRegression()
print (clf)
clf.fit(X,y)
