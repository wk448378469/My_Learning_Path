# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 18:14:52 2017

@author: 凯风
"""

'''
    队列：
        先进先出~
        
        isEmpty —— 队列是否为空
        enqueue —— 添加元素
        dequeue —— 删除元素
        size    —— 队列的长度
'''

class Queue(object):
    
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def enqueue(self,item):
        self.items.insert(0,item)
    
    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
    
if __name__ == '__main__':
    q = Queue()
    q.enqueue(4)
    q.enqueue('dog')
    q.enqueue(True)
    q.size()
    for i in range(q.size()):
        print ('delete ',q.dequeue())
    print (q.isEmpty())