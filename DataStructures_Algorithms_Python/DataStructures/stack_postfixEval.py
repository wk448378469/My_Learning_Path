# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 17:54:12 2017

@author: 凯风
"""

'''
    后缀表达式的计算：
        流程：
            1、创建一个空栈
            2、切分表达式
            3、从左到右扫描
                \如果是数字，转化成整数型，入栈
                \如果是运算符，需要两个数字弹出，运算他们，然后入栈
            4、遍历完，弹出栈里面的结果
'''

def postfixEval(postfixExpr):
    operandStack = stack.Stack()
    tokenList = postfixExpr.split()
    
    for token in tokenList:
        if token in '0123456789':
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token,operand1,operand2)
            operandStack.push(result)
    return operandStack.pop()

def doMath(op,op1,op2):
    if op == '*':
        return op1 * op2
    elif op == '/':
        return op1 / op2
    elif op == '+':
        return op1 + op2
    else:
        return op1 - op2

if __name__ =='__main__':
    import stack
    expr = '7 8 + 3 2 + /'
    print (postfixEval(expr))