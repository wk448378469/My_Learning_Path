# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 11:06:14 2017

@author: kaifeng
"""
import sklearn.datasets
import scipy as sp

test_data = sklearn.datasets.load_files('C:/Users/carne/Desktop/20news-bydate-test')
train_data = sklearn.datasets.load_files('C:/Users/carne/Desktop/20news-bydate-train')
# 这两个数据集可以通过sklearn.datasets.fetch_20newsgroups的方法获得

print (len(train_data.filenames))
print (len(test_data.filenames))

group = [ 'comp.graphics', 'comp.os.ms-windows.misc','comp.sys.ibm.pc.hardware','comp.sys.mac.hardware','comp.windows.x','sci.space']
# 缩小一点数据的范围，能跑的快些

test_data = sklearn.datasets.load_files('C:/Users/carne/Desktop/20news-bydate-test',categories = group)
train_data = sklearn.datasets.load_files('C:/Users/carne/Desktop/20news-bydate-train',categories = group)

print (len(train_data.filenames))
print (len(test_data.filenames))

from sklearn.feature_extraction.text import TfidfVectorizer
from nltk import stem

english_stemmer = stem.SnowballStemmer('english')

class StemmedTfidfVectorizer(TfidfVectorizer):
    # 上一节课学到的降噪的方法，主要是处理一些不合法的字符啊什么的
    def build_analyzer(self):
        analyzer = super(TfidfVectorizer,self).build_analyzer()
        return lambda doc:(english_stemmer.stem(w) for w in analyzer(doc))

vectorizer = StemmedTfidfVectorizer(min_df = 10 , max_df = 0.5 , stop_words = 'english' , decode_error = 'ignore')
vectorized = vectorizer.fit_transform(train_data.data)
num_samples , num_features = vectorized.shape

num_clusters = 50
from sklearn.cluster import KMeans

km = KMeans(n_clusters=num_clusters,init = 'random',n_init = 1,verbose = 1)
km.fit(vectorized)

km.labels_
# 生成了一个3529个元素的数组，数组的范围是[0,49]，因为我们聚类是聚了50个

# 簇的中心
km.cluster_centers_

new_post = 'Disk drive problems. Hi, I have a problem with my hard disk.After 1 year it is working only sporadically now.I tried to format it, but now it doesn\'t boot any more.Any ideas? Thanks.'
# 看一下这个新的文本会被划分到哪里~

new_post_vec = vectorizer.transform([new_post])
new_post_label = km.predict(new_post_vec)[0]

similar_indices = (km.labels_ == new_post_label).nonzero()[0]
# 找一下在测试数据集里面的，那些帖子的向量比较近
# nonzero() 是将布尔型数组转化为一个更小的数组，他包含True元素的索引位

similar = []

for i in similar_indices:
    dist = sp.linalg.norm((new_post_vec - vectorized[i]).toarray())
    similar.append((dist,train_data.data[i]))
    
similar = sorted(similar)

# 看看哪个最接近、差不多相似和几乎不相似的打出来看看
similar_at_1 = similar[0]
similar_at_2 = similar[int(len(similar)/2)]
similar_at_3 = similar[len(similar)-1] # or similar[-1]

print(similar_at_1)
print(similar_at_2)
print(similar_at_3)

# 看一看聚类的效果如何
from sklearn import metrics
labels = train_data.target
print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels, km.labels_))
print("Completeness: %0.3f" % metrics.completeness_score(labels, km.labels_))
print("V-measure: %0.3f" % metrics.v_measure_score(labels, km.labels_))
print("Adjusted Rand Index: %0.3f" % metrics.adjusted_rand_score(labels, km.labels_))
print("Adjusted Mutual Information: %0.3f" % metrics.adjusted_mutual_info_score(labels, km.labels_))
print(("Silhouette Coefficient: %0.3f" % metrics.silhouette_score(vectorized, labels, sample_size=1000)))
 
# 反正就是一些指标指标指标，然后具体表示啥的以后再慢慢研究吧






