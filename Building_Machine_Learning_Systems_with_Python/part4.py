# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 14:19:41 2017

@author: kaifeng
"""

from gensim import corpora,models,similarities
import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import distance

corpus = corpora.BleiCorpus('C:/Users/carne/Desktop/ap/ap.dat','C:/Users/carne/Desktop/ap/vocab.txt')
# 数据下载url：http://www.cs.princeton.edu/~blei/lda-c/ap.tgz

model = models.ldamodel.LdaModel(corpus,num_topics=100,id2word = corpus.id2word)

topics = [model[c] for c in corpus]
print (topics[0])

plt.hist([len(t) for t in topics])
plt.ylabel('Nr of documents')
plt.xlabel('Nr of topics')

model1 = models.ldamodel.LdaModel(corpus,num_topics=100,id2word = corpus.id2word,alpha=1)
topics1 = [model1[c] for c in corpus]

plt.clf()
plt.hist([[len(t) for t in topics],[len(t) for t in topics1]],np.arange(42))
plt.ylabel('Nr of documents')
plt.xlabel('Nr of topics')
plt.text(9,193,r'default alpha')
plt.text(26,156,r'alpha = 1')

dense = np.zeros((len(topics),100),float)
for ti,t in enumerate(topics):
    for tj,v in t:
        dense[ti,tj] = v

pairwise = distance.squareform(distance.pdist(dense)) # 计算主题距离
largest = pairwise.max()

for ti in range(len(topics)):
    pairwise[ti,ti] = largest + 1 #把对角线上的元素设为较大值

def closest_to(doc_id):
    return pairwise[doc_id].argmin()



model.save('C:/Users/carne/Desktop/ap.pkl')
# 模型的保存

model = models.ldamodel.LdaModel.load('C:/Users/carne/Desktop/ap.pkl')
# 模型的读取














