# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 18:04:41 2017

@author: 凯风
"""

'''
    这段代码只是为了后面的binary search tree 的简单版本
    主要作用就是给定一个数值型的列表，删除的元素永远都是列表中最小的~
'''

class BinHeap(object):
    
    def __init__(self):
        self.heapList = [0]                 # 堆表
        self.currentSize = 0                # 包含元素
        
    def percUp(self,i):
        while i // 2 > 0:                   # 在列表中获取父结点...真tm抽象啊
            if self.heapList[i] < self.heapList[i // 2]:            # 添加的元素比父结点小吗？
                tmp = self.heapList[i//2]                           # 下面是更新
                self.heapList[i//2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2
    
    def insert(self,k):
        # 尾部添加,但是会破坏树结构，所以需要调用percup来确保树结构不被破坏~~~
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)
        
    def percDown(self,i):
        # 和percup正好是反着的，主要用于删除结点用的
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc
            
    def minChild(self,i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1
    
    def delMin(self):
        # 删除表中最小值，不能乱删，需要用到percDwon
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval
    
    def buildHeap(self,alist):
        # 将列表转化为我们的数据结构
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while i > 0:
            self.percDown(i)
            i = i - 1

if __name__ == '__main__':
    bh = BinHeap()
    bh.buildHeap([9,5,6,2,3])
    print (bh.delMin())
    print (bh.delMin())
    print (bh.delMin())
    print (bh.delMin())
    print (bh.delMin())