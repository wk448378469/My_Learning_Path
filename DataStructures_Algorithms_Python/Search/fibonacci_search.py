# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

'''
    斐波那契查找：
        说明：恩，也是二分查找的优化版本，和插值类似，最重要的就是mid的更新上做了些创新，利用了黄金分割的相关知识
        思路：应该也可以利用递归完成的
        复杂度：期望，O(log2(n))
'''
import numpy as np

def fibonacci(length):
    # numpy 里面应该也有生成的方法
    F = [0,1]
    i = 2
    while i < length + 5:
        F.append(F[i-1] + F[i-2])
        i = i + 1
    return F

def fibonacciSearch(List, key):
    if key not in List:
        print ('Perhaps this key does not exist in this list')
        return False
    
    # 获取一个菲波那切数列
    F = fibonacci(len(List))
    
    low = 0
    high = len(List) - 1
    
    # 计算List的最大索引，位于菲波那切数列的神马位置
    k = 0
    while high > F[k]-1:
        k = k + 1
    
    # 将List扩充元素，扩充到 List最大索引在菲波那切数列位置的数量
    i = high
    while F[k]-1 > i:
        List.append(List[high])
        i = i + 1
    
    # 主要的逻辑了算是
    while low <= high:
        mid = low + F[k-1] - 1
        
        if key < List[mid]:
            high = mid - 1
            k = k - 1
        elif key > List[mid]:
            low = mid + 1
            k = k - 2
        else:
            if mid <= high:
                return mid
            else:
                return high
    
if __name__ == '__main__':
    List = list(sorted(np.random.randint(0,high=500,size=100)))
    result = fibonacciSearch(List, 120)
    if List[result] == 120:
        print ('\n')
        print ('congratulations ≖‿≖✧ ')