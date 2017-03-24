# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 15:26:59 2017

@author: kaifeng
"""
import os
import sys
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer # Tf...是干什么的没弄懂
vectorizer = CountVectorizer(min_df = 1,stop_words = 'english')      # min_df是最小文档频率，可以是百分数也可以是整数

content = ['how to format my hard disk','hard disk format problem']
X = vectorizer.fit_transform(content)
vectorizer.get_feature_names()
a = X.toarray().transpose()         # toarray()可以访问全部内容

DIR = r"C:/Users/carne/Desktop/toy"
posts = [open(os.path.join(DIR, f)).read() for f in os.listdir(DIR)]

X_train = vectorizer.fit_transform(posts) #创建向量
num_samples , num_features = X_train.shape

new_post = 'imaging databases'
new_post_vec = vectorizer.transform([new_post])

print (new_post_vec.toarray())

import scipy as sp
def dist_raw(v1,v2):
    v1_normalized = v1/sp.linalg.norm(v1.toarray()) # 归一化
    v2_normalized = v2/sp.linalg.norm(v2.toarray())
    delta = v1_normalized - v2_normalized
    return sp.linalg.norm(delta.toarray()) # norm 用来计算最小距离

best_doc = None
best_dist = sys.maxsize
best_i = None

for i in range(0,num_samples):
    post = posts[i]
    if post == new_post:
        continue
    post_vec = X_train.getrow(i)
    d = dist_raw(post_vec,new_post_vec)
    print ("=== Post %i with dist=%.2f: %s" % (i, d, post))
    if d < best_dist:
        best_dist = d
        best_i = i
print("Best post is %i with dist=%.2f" % (best_i, best_dist))


vectorizer = CountVectorizer(min_df=1,stop_words='english') #stopwords是停用词，如果定义了就会有很多类似于most啊、a啊、about啊不被统计
sorted(vectorizer.get_stop_words())[:50] # 大约有多少呢？  318个
len(vectorizer.get_stop_words())     

# 同语义的词的去重，需要下载一个包....好像不用》。。。！！！
# 正统的叫法是词干处理~

from nltk import stem

english_stemmer = stem.SnowballStemmer('english') # 有很多，英语的用Snowball吧
english_stemmer.stem('imaging')
english_stemmer.stem('image')
english_stemmer.stem('imagine')
english_stemmer.stem('buys')
english_stemmer.stem('buying')
english_stemmer.stem('bought')

class StemmedCountVectorizer(CountVectorizer):
    # 创建一个类
    def build_analyzer(self):
        analyzer = super(StemmedCountVectorizer,self).build_analyzer()
        return lambda doc:(english_stemmer.stem(w) for w in analyzer(doc))
        # 这个方法确实挺高级的感觉....    
    
vectorizer = StemmedCountVectorizer(min_df=1,stop_words='english')
X_train = vectorizer.fit_transform(posts) #创建向量
num_samples , num_features = X_train.shape

for i in range(0,num_samples):
    post = posts[i]
    if post == new_post:
        continue
    post_vec = X_train.getrow(i)
    d = dist_raw(post_vec,new_post_vec)
    print ("=== Post %i with dist=%.2f: %s" % (i, d, post))
    if d < best_dist:
        best_dist = d
        best_i = i
print("Best post is %i with dist=%.2f" % (best_i, best_dist))
# post 2 的 就成了最接近的了~


# 停用词兴奋剂》？什么鬼东西翻译的，服了这个书的汉译了...
def tfidf(term,doc,docset):
    tf = float(doc.count(term))/sum(doc.count(term) for doc in docset)
    idf = sp.log(float(len(docset))/(len([doc for doc in docset if term in doc])))
    return tf * idf

a , abb , abc = ['a'],['a','b','b'],['a','b','c']
D = [a,abb,abc]
print(tfidf("a", a, D))
print(tfidf("b", abb, D))
print(tfidf("a", abc, D))
print(tfidf("b", abc, D))
print(tfidf("c", abc, D))
'''
    理解下来大致的意思是：
    如果一个词经常出现在某个post里面，而在其他post不怎么出现，则会给该词语一定的权重
    eg:'a'在a、abb、abc里面都有，所以权重会低，烂大街了。而c只在abc里面，所以权重会最高
'''

# 所以应用到上面的模型中....

class StemmedCountVectorizer(CountVectorizer):
    def build_analyzer(self):
        analyzer = super(StemmedCountVectorizer,self).build_analyzer()
        return lambda doc:(english_stemmer.stem(w) for w in analyzer(doc))
vectorizer = StemmedCountVectorizer(min_df=1, stop_words='english')

class StemmedTfidfVectorizer(TfidfVectorizer):
    def build_analyzer(self):
        analyzer = super(StemmedTfidfVectorizer, self).build_analyzer()
        return lambda doc: (english_stemmer.stem(w) for w in analyzer(doc))

vectorizer = StemmedTfidfVectorizer(min_df=1, stop_words='english')
X_train = vectorizer.fit_transform(posts)
num_samples , num_features = X_train.shape

for i in range(0,num_samples):
    post = posts[i]
    if post == new_post:
        continue
    post_vec = X_train.getrow(i)
    d = dist_raw(post_vec,new_post_vec)
    print ("=== Post %i with dist=%.2f: %s" % (i, d, post))
    if d < best_dist:
        best_dist = d
        best_i = i
print("Best post is %i with dist=%.2f" % (best_i, best_dist))
# 好像又都有了些变化，不过还是post = 2最好貌似

'''
    文本预处理过程：
    1、分词
    2、丢掉频率过高的，没有帮助的词
    3、丢掉频率低，很小可能出现在要预测的文本中的
    4、统计剩余词
    5、计算TF-IDF值
'''
