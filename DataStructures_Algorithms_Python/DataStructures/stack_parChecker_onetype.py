# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 15:33:36 2017

@author: 凯风
"""

'''
    利用stack检测字符串中，括号的完整性
'''

def parChecker(symbolString):
    # 创建对象
    s = stack.Stack()
    
    # 初始化
    balanced = True
    index = 0
    
    # 当索引位小于总长度并且平衡为真时，进入循环
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]                # 获取索引位的字符
        if symbol == '(':                           # 是否是左括号
            s.push(symbol)                          # 是，入栈
        else:
            if s.isEmpty():                         # 判断当前是否为空栈
                balanced = False                    # 置为不完整
            else:
                s.pop()
        index = index + 1
        
    if balanced and s.isEmpty():
        return True
    else:
        return False
    
if __name__ == '__main__':
    import stack
    str1 = parChecker('((()))')
    str2 = parChecker('(()(((')
    print (str1,str2)