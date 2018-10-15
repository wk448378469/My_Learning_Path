# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 15:20:00 2017

@author: 凯风
"""

'''
    树结构和栈结构的应用：
        buildParseTree
            说明：构建解析树，将传入的表达式，存到树结构中
            思路：
                如果字符是(    则添加一个新的树结点作为当前结点的左侧child，并下降到左侧的child
                如果字符是+-*/ 则将当前结点的值设置为运算符，并且添加一个右侧child作为当前结点的右child，下降到右侧的child
                如果字符是num  则将当前结点的值设置为num，并返回父结点
                如果字符是)    则转到当前结点的父结点
                PS.利用栈来追踪父子结点
        evaluate
            说明：利用递归遍历解析树，计算表达式的结构，然后返回数值
        postorder
            说明：后序遍历
        preorder
            说明：前序遍历
        inorder
            说明：中序遍历
        printexp
            说明：打印表达式
'''

def buildParseTree(fpexp):
    
    fplist = fpexp.split()                              # 分割字符串
    pStack = stack.Stack()                              # 初始化栈
    eTree = binary_tree.BinaryTree('')                  # 初始化树
    pStack.push(eTree)                                  # 将树这个对象，入栈
    currentTree = eTree                         
    
    for i in fplist:                                    # 迭代字符串
        
        if i == '(':
            currentTree.insertLeft('')                  # 添加左侧子节点
            pStack.push(currentTree)                    # 入栈
            currentTree = currentTree.getLeftChild()    # 下降
            
        elif i not in ['+','-','*','/',')']:
            currentTree.setRootVal(int(i))              # 设置结点值
            parent = pStack.pop()                       # 出栈
            currentTree = parent                        # 上升
            
        elif i in ['+','-','*','/']:
            currentTree.setRootVal(i)                   # 设置结点值
            currentTree.insertRight('')                 # 添加右侧子节点
            pStack.push(currentTree)                    # 入栈
            currentTree = currentTree.getRightChild()   # 下降
            
        elif i == ')':
            currentTree = pStack.pop()                  # 出栈
            
        else:
            raise ValueError
            
    return eTree

def evaluate(parseTree):
    # 计算树结构中的表达式，并返回结果
    opers = {'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv}
    
    leftC = parseTree.getLeftChild()                # 左侧子节点
    rightC = parseTree.getRightChild()              # 右侧子节点
    
    if leftC and rightC:                            # 均不为空，执行
        fn = opers[parseTree.getRootVal()]          # 获取值
        return fn(evaluate(leftC),evaluate(rightC)) # 计算
    else:
        return parseTree.getRootVal()               # 报错

def postorder(tree):
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())

def preorder(tree):
    if tree != None:
        print (tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

def inorder(tree):
    if tree != None:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())

def printexp(tree):
    sVal = ''
    if tree != None:
        sVal = '(' + printexp(tree.getLeftChild())
        sVal = sVal + str(tree.getRootVal())
        sVal = sVal + printexp(tree.getRightChild()) + ')'
    return sVal

if __name__ == '__main__':
    import binary_tree
    from DataStructures import stack
    import operator
    # 解析树
    pt = buildParseTree("( ( 10 + 5 ) * 3 )")
    # 遍历树
    postorder(pt)
    print ('\n') 
    preorder(pt)
    print ('\n')                
    inorder(pt)
    print ('\n')
    # 计算表达式
    print (evaluate(pt))
    # 打印表达式
    print (printexp(pt))