# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 18:36:23 2017

@author: 凯风
"""

'''
    队列的一个应用。
        类似于小时候玩的抢凳子吧
        好像还有一个历史故事...
'''

def hotPotato(namelist,num):
    # 初始化对象
    simqueue = queue.Queue()
    
    # 小孩全加入到队列中
    for name in namelist:
        simqueue.enqueue(name)
        
    while simqueue.size() > 1:
        
        # 开始数数，类似于围着圆跑起来
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
        
        # 删掉倒霉的那个
        simqueue.dequeue()
        
    return simqueue.dequeue()

if __name__ == '__main__':
    import queue
    namelist = ['ming','zhang','wang','huang','huo','zhao','qian']
    num = 10
    print (hotPotato(namelist,num))