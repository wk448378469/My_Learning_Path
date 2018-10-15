# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 14:45:58 2017

@author: 凯风
"""

'''
    到底是结点，还是节点啊！！！！！！@#！@￥#@￥##￥%￥￥%
'''

class BinaryTree(object):
    
    def __init__(self,rootObj):
        self.key = rootObj                  # 根节点的值
        self.leftChild = None               # 左child的初始化
        self.rightChild = None              # 右child的初始化
        
    def insertLeft(self,newNode):
        # 左测child插入对象
        if self.leftChild == None:                  # 判断左child是否为空
            self.leftChild = BinaryTree(newNode)    # 创建一棵子树，并复制给左child
        else:                   
            t = BinaryTree(newNode)                 # 创建一棵树
            t.leftChild = self.leftChild            # 新的树的的左child为原树的左child
            self.leftChild = t                      # 原树的child复制给新的树，完成插入
    
    def insertRight(self,newNode):
        # 同insertLeft
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t
    
    def getRightChild(self):
        # 获取结点右侧的child
        return self.rightChild
    
    def getLeftChild(self):
        # 获取结点左测的child
        return self.leftChild
    
    def setRootVal(self,obj):
        # 设置结点的值
        self.key = obj
    
    def getRootVal(self):
        # 获取结点的值~
        return self.key
    

if __name__ == '__main__':
    r = BinaryTree('a')
    print(r.getRootVal())
    print(r.getLeftChild())
    r.insertLeft('b')
    print(r.getLeftChild())
    print(r.getLeftChild().getRootVal())
    r.insertRight('c')
    print(r.getRightChild())
    print(r.getRightChild().getRootVal())
    r.getRightChild().setRootVal('hello')
    print(r.getRightChild().getRootVal())
    