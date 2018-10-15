# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 16:22:09 2017

@author: 凯风
"""

'''
    有序链表，就是有排序的，与无序相比，剩下的就没太多不同了应该
    最大的不同点就是add的这个方法上，因为添加结点时需要考虑大小了~
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

class OrderedList(object):
    
    def __init__(self):
        self.head = None
    
    def add(self,item):
        current = self.head
        previous = None
        stop = False
        
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()
                
        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def isEmpty(self):
        # 和无序一样
        return self.head == None

    def search(self,item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()
        return found
    
    def size(self):
        # 和无序一样的
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

if __name__ == '__main__':
    mylist = OrderedList()
    mylist.add(31)
    mylist.add(77)
    mylist.add(17)
    mylist.add(93)
    mylist.add(26)
    mylist.add(54)
    print (mylist.size())
    print (mylist.search(93))
    print (mylist.search(100))
    
        