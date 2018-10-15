# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 18:37:48 2017

@author: 凯风
"""

'''
    平衡二叉树，又称为AVL树(两个创造者的名字缩写)
        是属于在二叉搜索树的一个优化
        主要解决二叉搜索树在极端情况下复杂度退化为线性的即O(n)
        主要性质：
            是一棵空树或它的左右两个子树的高度差的绝对值不超过1，
            并且左右两个子树都是一棵平衡二叉树
        复杂度：稳定在O(log2(n))
        结点公式：
            F(n) = F(n-1) + F(n-2) + 1 其中
                1       —— 根结点
                F(n-1)  —— 左子树的结数量
                F(n-2)  —— 右子树的结数量
        PS...下面的代码只是在binary serch tree 文件的基础上做了简单修改，并未真实完成AVL tree
'''


class TreeNode(object):
    # 结点对象
    def __init__(self,key,val,left=None,right=None,parent=None):
        self.key = key                          # 结点键
        self.payload = val                      # 结点值
        self.leftChild = left                   # 左子结点
        self.rightChild = right                 # 右子节点
        self.parent = parent                    # 父结点

    def hasLeftChild(self):
        # 是否有左子结点
        return self.leftChild

    def hasRightChild(self):
        # 是否有右子结点
        return self.rightChild

    def isLeftChild(self):
        # 判断结点是否为左结点(是否有父结点并且父结点的右子节点是该结点)
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        # 同上
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        # 结点是否为根结点
        return not self.parent

    def isLeaf(self):
        # 结点是否为叶结点
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        # 是否有子结点
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        # 节点是否有全子结点(同时有左子结点和右子结点)
        return self.rightChild and self.leftChild

    def replaceNodeData(self,key,value,lc,rc):
        # 更新结点的信息
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self


class BalanceBinaryTree(object):
    # 二叉搜索树
    def __init__(self):
        self.root = None            # 根结点
        self.size = 0               # 树包含的结点数

    def length(self):
        # 获取结点数
        return self.size

    def __len__(self):
        # 内置函数，返回对象的长度，具体说明参考官网~
        return self.size

    def put(self,key,val):
        # 添加结点
        if self.root:                           # 如果根结点不为空
            self._put(key,val,self.root)        # 调用方法
        else:                                   # 根结点为空
            self.root = TreeNode(key,val)       # 设置根结点，属性传入的key和value
        self.size = self.size + 1

    def _put(self,key,val,currentNode):
        if key < currentNode.key:               # 传入的key小于根结点的key
            if currentNode.hasLeftChild():      # 根节点有左结点
                   self._put(key,val,currentNode.leftChild)     # 递归
            else:                               # 根节点无左结点
                   currentNode.leftChild = TreeNode(key,val,parent=currentNode)     # 将传入的参数，设置为根结点的左子结点
                   self.updateBalance(currentNode.leftChild)
        else:                                   # 传入的key大于根节点的key
            if currentNode.hasRightChild():
                   self._put(key,val,currentNode.rightChild)
            else:
                   currentNode.rightChild = TreeNode(key,val,parent=currentNode)
                   self.updateBalance(currentNode.leftChild)
    
    def updateBalance(self,node):
        if node.balanceFactor > 1 or node.balanceFactor < -1:
            self.rebalance(node)
            return
        if node.parent != None:
            if node.isLeftChild():
                node.parent.balanceFactor += 1
            elif node.isRightChild():
                node.parent.balanceFactor -= 1
            if node.parent.balanceFactor != 0:
                self.updateBalance(node.parent)
    
    def rotateLeft(self,rotRoot):
        newRoot = rotRoot.rightChild
        rotRoot.rightChild = newRoot.leftChild
        if newRoot.leftChild != None:
            newRoot.leftChild.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.leftChild = newRoot
            else:
                rotRoot.parent.rightChild = newRoot
        newRoot.leftChild = rotRoot
        rotRoot.parent = newRoot
        rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(newRoot.balanceFactor,0)
        newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(rotRoot.balanceFactor,0)

    def rotateRight(self,rotRoot):
        newRoot = rotRoot.leftChild
        rotRoot.leftChild = newRoot.rightChild
        if newRoot.rightChild != None:
            newRoot.rightChild.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isRightChild():
                rotRoot.parent.rightChild = newRoot
            else:
                rotRoot.parent.leftChild = newRoot
        newRoot.rightChild = rotRoot
        rotRoot.parent = newRoot
        rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(newRoot.balanceFactor,0)
        newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(rotRoot.balanceFactor,0)
        
    def rebalance(self,node):
        if node.balanceFactor < 0:
            if node.rightChild.balanceFactor > 0:
                self.rotateRight(node.rightChild)
                self.rotateLeft(node)
            else:
                self.rotateLeft(node)
        elif node.balanceFactor > 0:
            if node.leftChild.balanceFactor < 0 :
                self.rotateLeft(node.leftChild)
                self.rotateRight(node)
            else:
                self.rotateRight(node)
        
                
    def __setitem__(self,k,v):
        # 和__getitem__差不多，可以使用[key] = value 进行快速定义
       self.put(k,v)

    def get(self,key):
        # 获取key对应的value
       if self.root:
           res = self._get(key,self.root)
           if res:
                  return res.payload
           else:
                  return None
       else:
           return None

    def _get(self,key,currentNode):
        # 递归的查找key对应结点
        # 返回结点对象，在get方法中获取value，也就是payload~
       if not currentNode:
           return None
       elif currentNode.key == key:
           return currentNode
       elif key < currentNode.key:
           return self._get(key,currentNode.leftChild)
       else:
           return self._get(key,currentNode.rightChild)

    def __getitem__(self,key):
        # 定制类的一种，可以使用[key],进行快速选取
       return self.get(key)

    def __contains__(self,key):
        # 官网给出的翻译是：implement membership test operators
        # 理解起来应该就是是否包含这个key吧~
        # 有了这个以后可以使用 key in 对象:     主要就是in这个快捷方法
       if self._get(key,self.root):
           return True
       else:
           return False

    def delete(self,key):
        
      if self.size > 1:
         nodeToRemove = self._get(key,self.root)        # 调用_get找到要删除的结点对象
         if nodeToRemove:                               # 找到了
             self.remove(nodeToRemove)                  # 调用remove方法删除
             self.size = self.size-1                    # 更新size
         else:
             raise KeyError('Error, key not in tree')
             
      elif self.size == 1 and self.root.key == key:     # key等于根结点的key，并且树的结点数=1
         self.root = None                               # 重置根结点为None
         self.size = self.size - 1                      # 更新size
         
      else:
         raise KeyError('Error, key not in tree')

    def __delitem__(self,key):
        # 官网给出的解释：deletion of self[key]
        # 和__getitem__的注释是一样的~
        # 就是删除，但是快捷方式如何调用呢？ 好像是del 对象[key]
       self.delete(key)
     
    def __iter__(self):
        # 可以用for……in……进行迭代
        # 应该是把对象变成可迭代的，迭代器？
        # yield，把一个函数变成generator，生成器
        # 应该缺少一个__next__
        if self:
            if self.hasLeftChild():
                for elem in self.leftChild:
                    yield elem
            yield self.key
            if self.hasRightChild():
                for elem in self.rightChild:
                    yield elem

    def spliceOut(self):
        # 为删除结点操作的准备~
       if self.isLeaf():
           if self.isLeftChild():
                  self.parent.leftChild = None
           else:
                  self.parent.rightChild = None
       elif self.hasAnyChildren():
           if self.hasLeftChild():
                  if self.isLeftChild():
                     self.parent.leftChild = self.leftChild
                  else:
                     self.parent.rightChild = self.leftChild
                  self.leftChild.parent = self.parent
           else:
                  if self.isLeftChild():
                     self.parent.leftChild = self.rightChild
                  else:
                     self.parent.rightChild = self.rightChild
                  self.rightChild.parent = self.parent

    def findSuccessor(self):
        # 为删除结点操作的准备~
      succ = None
      if self.hasRightChild():
          succ = self.rightChild.findMin()
      else:
          if self.parent:
                 if self.isLeftChild():
                     succ = self.parent
                 else:
                     self.parent.rightChild = None
                     succ = self.parent.findSuccessor()
                     self.parent.rightChild = self
      return succ

    def findMin(self):
        # 查找二叉查找树中key最小的结点
        # 因为性质决定了肯定在左边，所以……
      current = self
      while current.hasLeftChild():
          current = current.leftChild
      return current

    def remove(self,currentNode):
        # 最痛苦的要开始了~~~~~~~~~~
        # 删除结点
        # 就...看文档最开始的上面的流程吧
         if currentNode.isLeaf(): 
           if currentNode == currentNode.parent.leftChild:
               currentNode.parent.leftChild = None
           else:
               currentNode.parent.rightChild = None
         elif currentNode.hasBothChildren(): 
           succ = currentNode.findSuccessor()
           succ.spliceOut()
           currentNode.key = succ.key
           currentNode.payload = succ.payload

         else: 
           if currentNode.hasLeftChild():
             if currentNode.isLeftChild():
                 currentNode.leftChild.parent = currentNode.parent
                 currentNode.parent.leftChild = currentNode.leftChild
             elif currentNode.isRightChild():
                 currentNode.leftChild.parent = currentNode.parent
                 currentNode.parent.rightChild = currentNode.leftChild
             else:
                 currentNode.replaceNodeData(currentNode.leftChild.key,
                                    currentNode.leftChild.payload,
                                    currentNode.leftChild.leftChild,
                                    currentNode.leftChild.rightChild)
           else:
             if currentNode.isLeftChild():
                 currentNode.rightChild.parent = currentNode.parent
                 currentNode.parent.leftChild = currentNode.rightChild
             elif currentNode.isRightChild():
                 currentNode.rightChild.parent = currentNode.parent
                 currentNode.parent.rightChild = currentNode.rightChild
             else:
                 currentNode.replaceNodeData(currentNode.rightChild.key,
                                    currentNode.rightChild.payload,
                                    currentNode.rightChild.leftChild,
                                    currentNode.rightChild.rightChild)




if __name__ == '__main__':
    mytree = BalanceBinaryTree()
    mytree[3] = 'red'
    mytree[4] = 'blue'
    mytree[6] = 'yellow'
    mytree[2] = 'at'
    mytree[1] = 'all'
    mytree[9] = 'new'
    print (mytree[6])   # 调用顺序：__getitem__ , get , _get
    print (mytree[2])
    













