# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 15:10:20 2017

@author: 凯风
"""

'''
    栈
        最主要的特性就是，先进后出~
        其他的应该也没什么吧
'''


class Stack(object):
    
    def __init__(self):
        self.items = []
    
    # 判断是否为空
    def isEmpty(self):
        return self.items == []
    
    # 进栈
    def push(self,item):
        self.items.append(item)
    
    # 出栈
    def pop(self):
        return self.items.pop()
    
    # 查看最后进入的元素
    def peek(self):
        return self.items[len(self.items) - 1]
    
    # 获取栈的大小
    def size(self):
        return len(self.items)


if __name__ == '__main__':
    s = Stack()
    print(s.isEmpty())
    s.push(4)
    s.push('cat')
    print(s.peek())
    s.push(True)
    print(s.size())
    s.push([8.4])
    print (s.pop())
    print (s.pop())
    print (s.isEmpty())
    print (s.pop())
    print (s.pop())
