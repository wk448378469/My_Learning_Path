# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

'''
    顺序查找：
        说明：适合存储结构为顺序存储或链接存储的线性表。
        思路：从开头找，一直找到为止
        复杂度：O(n)
'''

def sequentialSearch(List,key):
    length = len(List)
    
    if length == 0:
        return 'This list is empty'
    
    for i in range(length):
        if List[i] == key:
            return i
    return 'This value is not in the list'

if __name__ == '__main__':
    List = [3, 25, 18, 123, 202, 524, 7, 9, 11, 232]
    result = sequentialSearch(List,222)
    print (result)