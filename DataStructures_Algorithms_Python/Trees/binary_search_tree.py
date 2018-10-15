# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 18:37:48 2017

@author: 凯风
"""

'''
    二叉查找树(又称二叉排序树~)：
        性质：
            1、若左子树不空，则左子树上所有结点的值均小于它的根结点的值
            2、若右子树不空，则右子树上所有结点的值均大于或等于它的根结点的值
            3、左、右子树也分别为二叉排序树
            4、没有键值相等的节点
            PS.对二叉查找树进行中序遍历，即可得到有序的数列
        复杂度：插入、查找O(log2(n)),最坏情况O(n)
        插入流程：
            1、若当前的二叉查找树为空，则插入的元素为根节点
            2、若插入的元素值小于根节点值，则将元素插入到左子树中
            3、若插入的元素值不小于根节点值，则将元素插入到右子树中
        删除流程：
            1、若为叶子节点，直接删除该节点，再修改其父节点的指针（记得区分根节点和不是根节点）
            2、若为单支节点（即只有左子树或右子树），让该结点的子树与该结点的父亲节点相连，删除结点（记得区分是根节点和不是根节点）
            3、若结点的左子树和右子树均不空。找到结点的后继y，因为y一定没有左子树，所以可以删除y，并让y的父亲节点成为y的右子树的父亲节点，
               并用y的值代替结点的值；或者方法二是找到p的前驱x，x一定没有右子树，所以可以删除x，并让x的父亲节点成为y的左子树的父亲节点。
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


class BinarySearchTree(object):
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
        else:                                   # 传入的key大于根节点的key
            if currentNode.hasRightChild():
                   self._put(key,val,currentNode.rightChild)
            else:
                   currentNode.rightChild = TreeNode(key,val,parent=currentNode)

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
    mytree = BinarySearchTree()
    mytree[3] = 'red'
    mytree[4] = 'blue'
    mytree[6] = 'yellow'
    mytree[2] = 'at'
    mytree[1] = 'all'
    mytree[9] = 'new'
    print (mytree[6])   # 调用顺序：__getitem__ , get , _get
    print (mytree[2])
    













