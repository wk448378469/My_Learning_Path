# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 18:09:55 2017

@author: 凯风
"""

'''
    二分查找：
        说明：必须作用于已经排序的数据结构，如果未排序应该先排序，至于排序本身有很多方法，后面也会学到
        思路：拿key和中间点比较，如果相等就直接返回，若不等根据key和中间点大小的比较决定下一步查找哪一个子表
        复杂度：O(log2(n))
        PS.突然想起来哈佛的那门编程课程，老师上来讲二分查找，上来就撕书
'''


def binarySearchNorm(List,key):
    # 正常的，用循环
    length = len(List)
    if length == 0:
        return 'This list is empty'    
    # 二分查找
    low = 0
    high = len(List) - 1
    while low < high:
        mid = int((low + high) / 2)
        if key < List[mid]:
            high = mid - 1
        elif key > List[mid]:
            low = mid + 1
        else:
            return mid
    return 'This value is not in the list'

def binarySearchRecu(List,key,low,high):
    # 学习用递归
    if key not in List:
        return 'This value is not in the list'
    
    mid = int((low+high) / 2)
    if key == List[mid]:
        return mid
    if key < List[mid]:
        return binarySearchRecu(List , key , low , mid -1)
    if key > List[mid]:
        return binarySearchRecu(List , key , mid + 1 , high)
    
if __name__ == '__main__':
    List = [1, 5, 7, 8, 22, 54, 99, 123, 200, 222, 444]
    result = binarySearchNorm(List,99)
    result = binarySearchRecu(List,99,0,len(List)-1)
    print (result)