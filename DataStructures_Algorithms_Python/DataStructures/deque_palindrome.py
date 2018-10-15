# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 10:15:09 2017

@author: 凯风
"""

'''
    利用双端队列来检测字符串是否镜像对称，例如madam、wow等
'''

def palchecker(aString):
    # 创建对象
    chardeque = deque.Deque()
    
    # 把每个对象添加到双端队列中，从左向右添加
    for ch in aString:
        chardeque.addRear(ch)
    
    # 初始化
    stillEqual = True
    
    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()     # 从右向左获取字符
        last = chardeque.removeRear()       # 从左向右获取字符
        # 是否相同
        if first != last:
            stillEqual = False
    
    return stillEqual

if __name__ == '__main__':
    import deque
    str1 = 'lsdkjfskf'
    str2 = 'radar'
    print (palchecker(str1),palchecker(str2))