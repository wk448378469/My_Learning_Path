# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 12:06:24 2017

@author: 凯风
"""

'''
    合并排序：
        说明：
            将两个（或两个以上）有序表合并成一个新的有序表，即把待排序序列分为若干个子序列，
            每个子序列是有序的。然后再把有序子序列合并为整体有序序列。
        复杂度：O(n*log(n))
        其他：
            1、需要递归实现
            2、如果列表过大的情况下，需要考虑列表切片后的存储空间
'''

def mergeSort(alist):
    
    print("Splitting ",alist)
    
    if len(alist)>1:
        mid = len(alist)//2
        # 切分列表
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        # 递归
        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        # 对子表排序
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)
    
alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print (alist)