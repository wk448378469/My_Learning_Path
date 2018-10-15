# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 11:07:01 2017

@author: 凯风
"""

'''
    搜索排序：
        说明：
            每次选取列表中的最大值，置于最后
            选择子表的最大值，置于倒数第二个
            ……
        复杂度：O(n^2)
'''

def selectionSort(alist):
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           # 查找最大值的索引位
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp

alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)