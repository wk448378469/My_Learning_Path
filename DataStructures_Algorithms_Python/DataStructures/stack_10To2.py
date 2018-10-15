# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 16:24:46 2017

@author: 凯风
"""

'''
    利用栈，将十进制转化为二进制
    当然也可以转化成为其他的例如八进制或十六进制，主要的思路是一样的
    当然更好的做法是divideBy2这个方法中，再新增加一个参数作为可选参数，以适应不同的转化目标~
'''

def divideBy2(decNumber):
    # 创建对象
    remstack = stack.Stack()
    
    while decNumber > 0 :
        rem = decNumber % 2             # 取余数
        remstack.push(rem)              # 入栈
        decNumber = decNumber // 2      # 更新被除数为原除法后的商
    
    binStr = ''                         # 初始化一个字符串，作为二进制的保存对象
    while not remstack.isEmpty():       
        binStr = binStr + str(remstack.pop())       # 出栈
    
    return binStr

if __name__ == '__main__':
    import stack
    num1 = 45
    num2 = 1024
    print (divideBy2(num1),divideBy2(num2))