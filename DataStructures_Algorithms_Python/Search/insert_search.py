# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 19:06:58 2017

@author: 凯风
"""

'''
    插值查找：
        说明：其实主要是二分查找的一个优化改良，比如我们在查找amazing这个词的时候，
             肯定不会从中间开始，而是靠前的位置。如果是zoo这个词，则是靠后的位置开始
        思路：让查找点的方法从二分，改为：low+(key-List[low])/(List[high]-List[low])*(high-low)
        复杂度：O(log2(log2(n)))
'''


def insertSearch(List,key,low,high):
    if key not in List:
        return 'This value is not in the list'
    # 和二分的唯一区别就是mid的公式而已
    mid = int(low+(key-List[low])/(List[high]-List[low])*(high-low))
    if key == List[mid]:
        return mid
    if key < List[mid]:
        return insertSearch(List , key , low , mid -1)
    if key > List[mid]:
        return insertSearch(List , key , mid + 1 , high)
    
if __name__ == '__main__':
    import numpy as np
    List = list(sorted(np.random.randint(0,high=1000,size=500)))
    # 看你运气喽~~~
    result = insertSearch(List,99,0,499)
    print (result)