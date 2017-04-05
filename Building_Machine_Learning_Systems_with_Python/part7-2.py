# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 15:48:46 2017

@author: kaifeng
"""
import numpy as np
from sklearn.datasets import load_svmlight_file
from sklearn.cross_validation import KFold
from sklearn.linear_model import ElasticNetCV

data, target = load_svmlight_file('C:/Users/carne/Desktop/E2006.train')

met = ElasticNetCV(fit_intercept=True)

kf = KFold(len(target),n_folds=2)

for train , test in kf:
    met.fit(data[train],target[train])
    p = map(met.predict,data[test])
    p = np.array(p).ravel()
    e = p - target[test]
    err += np.dot(e,e)

rmse_10cv = np.sqrt(err/len(target))

# 别用个人笔记本跑。。。有点浪费时间了~



