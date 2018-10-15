# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 17:07:40 2017

@author: 凯风
"""

'''
    利用栈，将中缀表达式转化为后缀表达式
        大致形式：
                中缀表达式              前缀表达式                  后缀表达式
              A + B * C + D         	+ + A * B C D              A B C * + D +
            (A + B) * (C + D)       	* + A B + C D              A B + C D + *
    
        主要流程：
        1、opstack空栈保存运算符，postfixlist输出清单
        2、切分中缀表达式
        3、遍历中缀表达式的列表tokenlist
            \如果是运算值(字符或数字)，添加到输出清单postfixlist
            \如果是左括号，入栈
            \如果是右括号，出栈，直到遇到完成第一个左括号出栈
            \如果是运算符号
                \判断栈中是否有同级或高一级的运算的运算符，有则添加到postfixlist
                \否则入栈
        4、全部出栈         
'''

def infixToPostfix(infixexpr):
    # 优先级对照表
    prec = {'*':3,'/':3,'+':2,'-':2,'(':1}
    opStack = stack.Stack()
    postfixList = []
    tokenList = infixexpr.split()           # 切分中缀表达式
    
    for token in tokenList:

        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or token in '1234567890' or token in 'abcdefghigklmnopqrstuvwxyz':
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while(not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)
            
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    
    return ' '.join(postfixList)

if __name__ == '__main__':
    import stack
    expr1 = 'a * b + c * d'
    expr2 = '( a + b ) * c - ( d - e ) * ( f + g )'
    print (infixToPostfix(expr1),'\n',infixToPostfix(expr2))
        