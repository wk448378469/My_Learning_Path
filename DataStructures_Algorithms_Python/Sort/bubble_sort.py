# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 10:35:56 2017

@author: 凯风
"""

'''
    冒泡排序：
        说明：
            从列表的第一个位置和第二个位置开始，比较两个值，如果1>2，则调换位置
            以此类推到倒数第二个元素和最后一个元素，此时列表的最大值就位于了列表的最末端
            然后继续从头来，一直到倒数第三个元素和倒数第二个元素为止~
        复杂度：O(n^2)，n是列表的长度~
        
'''

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
                

def shortBubbleSort(alist):
    # 算作是优化吧~
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
       exchanges = False
       for i in range(passnum):
           if alist[i]>alist[i+1]:
               exchanges = True
               temp = alist[i]
               alist[i] = alist[i+1]
               alist[i+1] = temp
       passnum = passnum-1

alist=[20,30,40,90,50,60,70,80,100,110]
shortBubbleSort(alist)
print(alist)

alist = [39,23,42,54,75,83,56,32,22,1,5]
bubbleSort(alist)
print(alist)