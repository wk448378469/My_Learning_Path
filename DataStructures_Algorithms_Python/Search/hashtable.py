# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 18:08:47 2017

@author: 凯风
"""

'''
    hash表~~！
        说明：
            槽                一个hash表可以存放多个槽，槽既是用来盛放数据的载体，槽包括槽的索引、槽中的数据
            hash函数          把item映射成为hash值的函数，并且把得到的hash值存放到对应的槽中
                数值型             取余数
                电话码             两两相加后取余数
                数值型             平方后取中间的两位数，再取余数
                字符串型            可以转化数值型后再计算~
                ……                  ……
            解决冲突           有时候两个或两个以上的item计算后，得到同一个索引，如何解决他们的存放记为解决冲突
                方案一             遇到冲突，找到hash表中槽没有被占用的，用来存放item，比如从hash表头开始依次找空槽。缺点：容易聚集在一起
                方案二             rehash，就是在映射一次，对item第一次的oldhash值~
                方案三             每个槽允许插入多个item~~
                ……                  ……
            负载因子λ           当前已经被用掉的槽的数量除以总的槽的数量~
        复杂度：
            好的情况 0.5(1 + 1/(1-λ))
            坏的情况 0.5(1 + (1/(1-λ))^2)
'''

class HashTable(object):
    
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size         # 槽
        self.data = [None] * self.size          # 槽中的数据
    
    def hashfunction(self,key,size):
        ''' hash 函数
            这里使用的方法是取余数，对于整数数值型的数据来说是最基础的
            对于其他的例如字符串型、浮点数等有更多其他好玩的方法~
            总之，目的就是把key映射到一个另一空间去~'''
        return key % size
    
    def rehash(self,oldhash,size):
        '''
            解决冲突时用到的方案一，方案也有很多的其实~
            这里面用到的是再次映射一次~
        '''
        return(oldhash + 1) % size
    
    def __getitem__(self,key):
        # 快速获得key的数据
        return self.get(key)
    
    def __setitem__(self,key,data):
        # 快速设定key和data
        self.put(key,data)
    
    def put(self,key,data):
        hashvalue = self.hashfunction(key,len(self.slots))              # 计算hash值
        if self.slots[hashvalue] == None:                               # hash表中，如果对应的槽没有备用掉
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:                        # 如果备用掉的槽中的key和新加入的是一样的~
                self.data[hashvalue] = data                         # 覆盖原来的数据...so bad
            else:
                nextslot = self.rehash(hashvalue,len(self.slots))               # 解决冲突，重新计算一次hash值
                while self.slots[nextslot] != None and self.slots[nextslot] != key:     # 判断槽有没有被用掉，对应的key是否相等
                    nextslot = self.rehash(nextslot,len(self.slots))
                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data
    
    def get(self,key):
        startslot = self.hashfunction(key,len(self.slots))          # 获取槽的位置
        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position,len(self.slots))
                if position == startslot:
                    stop = True
        return data


        
if __name__ == '__main__':
    H = HashTable()
    H[54] = 'cat'   #这里应该调用的是__setitem__ ,等价于  H.put(54,'cat') 
    H[26] = 'dog'
    H[93] = 'lion'
    H[17] = 'tiger'
    H[77] = 'bird'
    H[31] = 'cow'
    H[44] = 'goat'
    H[55] = 'pig'
    H[20] = 'chicken'
    print (H.slots)
    print (H.data)
    print (H[20])   # 这里应该调用的是 __getitem__ , 等价于 H.get(20)
    print (H[17])
    H[20] = 'duck'
    print (H[20])
    print (H[99])