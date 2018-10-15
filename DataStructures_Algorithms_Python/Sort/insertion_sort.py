# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 11:26:00 2017

@author: 凯风
"""

'''
    插值排序：
        说明：
            假定第一个元素被排序了~反正只有一个
            加入第二个元素与第一个元素比较，插入到相应的位置
            加入第三个元素，与前两个比较，插入相应的位置
            ……
        复杂度:O(n^2)
'''

def insertionSort(alist):
    for index in range(1,len(alist)):
        
        currentvalue = alist[index]
        position = index
        while position > 0 and alist[position-1] > currentvalue:
            alist[position] = alist[position-1]
            position = position - 1
        
        alist[position] = currentvalue

alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print(alist)  