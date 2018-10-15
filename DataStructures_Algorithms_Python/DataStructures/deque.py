# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 10:03:44 2017

@author: 凯风
"""

'''
    Deque，双端队列，可以在两端进行添加元素和删除元素的数据类型。
        
'''

class Deque(object):
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        # 判断是否为空
        return self.items == []
    
    def addFront(self,item):
        # 在右侧添加一个元素
        self.items.append(item)
    
    def addRear(self,item):
        # 在左侧添加一个元素
        self.items.insert(0,item)
    
    def removeFront(self):
        # 删除右侧的元素并返回删除的元素
        return self.items.pop()

    def removeRear(self):
        # 删除左侧的元素并返回删除的元素
        return self.items.pop(0)
    
    def size(self):
        # 获取双端队列的尺寸
        return len(self.items)
    
if __name__ == '__main__':
    d = Deque()
    print (d.isEmpty())
    d.addFront(4)
    d.addRear('dog')
    d.addRear('cat')
    print (d.size())
    print (d.removeFront())
    print (d.removeRear())
    print (d.removeRear())