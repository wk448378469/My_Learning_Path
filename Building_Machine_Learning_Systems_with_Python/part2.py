# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 12:57:49 2017

@author: kaifeng
"""

import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import numpy as np

# 读取数据
data = load_iris()
features = data['data']
feature_names = data['feature_names']
target = data['target']
species = data['target_names'][data['target']]

for t,marker,c in zip(range(3),'>ox','rgb'):
    plt.scatter(feature[target==t,0],
                feature[target==t,1],
                marker = marker,
                c = c)

plength = feature[:,2]
is_setosa = (target == 0)
max_setosa = plength[is_setosa].max()       # 等于3.0
min_non_setosa = plength[~is_setosa].min()     #等于1.9

'''
    def model1 ():
        if features[:,2] < 2:
            print 'this is iris setosa'
        else:
            print 'maybe iris virginica or iris versicolour'
'''

features = features[~is_setosa]
species = species[~is_setosa]
virginica = (species == 'virginica')

best_acc = -1.0
for fi in range(features.shape[1]):
    thresh = features[:,fi].copy()
    thresh.sort()
    for t in thresh:
        pred = (features[:,fi] > t)
        acc = (pred == virginica).mean()
        if acc > best_acc:
            best_acc = acc
            beat_fi = fi
            beat_t = t


'''
    def model2 ():
        if example[beat_fi] > t :
            print 'this is virginica'
        else:
            print 'this is versicolour'
'''



