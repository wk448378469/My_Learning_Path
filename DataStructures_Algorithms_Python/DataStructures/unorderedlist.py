# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 10:42:06 2017

@author: 凯风
"""

'''
    无序链表，一种递归的数据结构，或者为空，或者指向一个结点的引用。该节点又包含一个元素和一个指向另一个链表的索引
        节点：
            包含方法：获取元素、获取下一个的索引、设置元素、设置下一个的索引
        无序链表：
            包括方法：是否为空、添加元素、搜索链表中是否有元素、移出元素、插入、索引、还有pop等
        
'''

class Node(object):
    # 单个节点的类
    def __init__(self,initdata):
        self.data = initdata
        self.next = None
    
    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def setData(self,newdata):
        self.data = newdata
    
    def setNext(self,newnext):
        self.next = newnext


class UnorderList(object):
    
    def __init__(self):
        # 表头是一个结点对象,叫做表头，其实一直处于链表的末端在认知中
        self.head = None
    
    def isEmpty(self):
        # 根据表头来确定是否为空
        return self.head == None
    
    def add(self,item):
        temp = Node(item)               # 创建新结点
        temp.setNext(self.head)         # 设置新结点的“上一项”为上一个结点对象
        self.head = temp                # 设置新结点为头

    def append(self,item):
        # 在链表的最前面添加结点
        temp = Node(item)
        if self.isEmpty():
            self.head = temp
        else:
            current = self.head
            while current.getNext() != None:
                current = current.getNext()
            current.setNext(temp)

    def size(self):
        current = self.head                 # 获取头结点，其实是链表的最后面的元素(认知中)
        count = 0                           # 计数
        while current != None:              
            count = count + 1
            current = current.getNext()
        return count
    
    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext() 	# 移动~
        return found
    
    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext() 	# 移动~
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
    
    def index(self,item):
        # 不够完美，因为是返回的链表中最后出现的，而不是像python自带的list的index方法，返回最先出现的~
        current = self.head
        currentIndex = self.size()
    
        for i in range(currentIndex):
            if current.getData() == item:
                return currentIndex - 1
            else:
                current = current.getNext()
                currentIndex = currentIndex - 1
                
        return item,'is not in list'
                
    
    def insert(self,pos,item):
        # 这里的问题就是要不要写的比较全面，支持正负pos的索引插入
        if pos <= 1:
            self.add(item)
        elif pos > self.size():
            self.append(item)
        else:
            temp = Node(item)                   # 插入位置后面的结点，初始化
            count = 0
            pre = None                          # 插入位置前面的结点，初始化
            current = self.head
            currentIndex = self.size()
            
            while currentIndex - count != pos:
                count = count + 1
                # 移动两个类似于固定器的结点
                pre = current
                current = current.getNext()
            pre.setNext(temp)
            temp.setNext(current)
        
    def pop(self):
        current = self.head
        self.head = current.getNext()               # 移动一下头指针
        

if __name__ == '__main__':
    # part 1 test Node
    temp = Node(93)
    print (temp.getData())
    # part 2 test UnorderList
    mylist = UnorderList()
    mylist.add(31)
    mylist.remove(31)
    mylist.add(77)
    mylist.append(33)
    mylist.add(17)
    mylist.add(93)
    mylist.insert(2,66)
    mylist.index(66)
    mylist.pop()
    print (mylist.size())
    print (mylist.search(93))
    mylist.add(100)
    print (mylist.search(100))