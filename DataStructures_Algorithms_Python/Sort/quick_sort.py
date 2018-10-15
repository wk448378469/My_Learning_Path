# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 12:57:10 2017

@author: 凯风
"""

'''
    快速排序:
        说明：
            先从数列中取出一个数作为基准数
            根据基准数将数列进行分区，小于基准数的放左边，大于基准数的放右边
            重复分区操作，知道各区间只有一个数为止
        复杂度：O(n*log(n))
        其他：若初始数列基本有序时，快排序反而退化为冒泡排序
'''

def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
    if first < last:
        # 获取分割点
        splitpoint = partition(alist,first,last) 
        # 递归
        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
    pivotvalue = alist[first]
    leftmark = first + 1
    rightmark = last
    done = False
    
    while not done:    
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1    
        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1    
        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp
            
    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp
    return rightmark
    
alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print (alist)
