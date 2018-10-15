# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 15:33:36 2017

@author: 凯风
"""

'''
    利用stack检测检测字符串中，花括号、尖括号、括号的完整性
'''

def parChecker(symbolString):
    # 创建对象
    s = stack.Stack()
    
    # 初始化
    balanced = True
    index = 0
    
    # 当索引位小于总长度并且平衡为真时，进入循环
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        
        if symbol in "([{":                      # 区别一，增加了两类括号
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,symbol):     # 区别二，利用一个函数进行抵消括号对时，是否一致性的问题
                    balanced = False
            index = index + 1
            
    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(Open,Close):
    opens = '([{'
    closes = ')]}'
    return opens.index(Open) == closes.index(Close)
    
if __name__ == '__main__':
    import stack
    str1 = parChecker('{{([][])}()}')
    str2 = parChecker('[{()]')
    print (str1,str2)