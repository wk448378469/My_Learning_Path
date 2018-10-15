# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 14:07:44 2017

@author: 凯风
"""

'''
    利用python自带的list实现二叉树，不适用自己定义的数据结构~
'''

def BinaryTree(r):
    # 初始化根节点
    return [r,[],[]]

def insertLeft(root,newBranch):
    # 给左侧的child赋新值或分支
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch,[],[]])
    return root

def insertRight(root,newBranch):
    # 给右侧的child赋新值或分支
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])

def setRootVal(root,newVal):
    # 设置根节点的值
    root[0] = newVal

def getRootVal(root):
    # 获取根节点的值
    return root[0]

def getLeftChild(root):
    # 获取左测的child
    return root[1]

def getRightChild(root):
    # 获取右侧的child
    return root[2]


if __name__ == '__main__':
    r = BinaryTree(3)
    insertLeft(r,4)
    insertRight(r,5)
    insertLeft(r,6)
    insertRight(r,7)
    l = getRightChild(r)
    print (l)
    
    setRootVal(l,9)
    print (r)
    insertLeft(l,11)
    print (r)
    print (getRightChild(getRightChild(r)))