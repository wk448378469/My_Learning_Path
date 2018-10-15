# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 11:42:04 2017

@author: 凯风
"""

'''
    希尔排序(缩小增量排序)：
        说明：先将整个待排序的记录序列分割成为若干子序列分别进行直接插入排序，待整个序列中的记录“基本有序”时，再对全体记录进行依次直接插入排序。
        复杂度：O(n^(1+e)),其中e在[0,1]
'''

def shellSort(alist):
    sublistcount = len(alist) // 2
    
    while sublistcount > 0:
        
        for startposition in range(sublistcount):
            # 对每个分组进行，小组内插值排序
            gapInsertionSort(alist,startposition,sublistcount)
        print ('after increments of size',sublistcount,'this list is',alist)
        
        sublistcount  = sublistcount // 2 # 更新分组策略
        
def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):
        currentvalue = alist[i]
        position = i
        while position >= gap and alist[position-gap] > currentvalue:
            alist[position] = alist[position-gap]
            position = position - gap
            
        alist[position] = currentvalue
    
alist = [54,26,93,17,77,31,44,55,20]
shellSort(alist)
print(alist)