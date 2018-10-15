# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 18:59:36 2017

@author: 凯风
"""

'''
    利用队列来模拟打印任务
        流程：
            1、创建一个队列代表打印任务，每个任务将被赋予一个时间戳，当开始时队列是空的
            2、迭代每一秒
                \是否有新的打印任务呗创建，如果是，将它添加到currentsecond钟作为时间戳的队列
                \如果当前打印机不是繁忙状态并且任务在等待
                    \从打印队列中删除下一个任务，并将任务分配给其他打印机
                    \从currentsecond中减去时间戳，以计算该任务的等待时机
                    \将该任务的等待时机附加到一个列表中，以便后续操作
                    \根据打印任务中的页数，确定需要多少时间
                \如果需要的话，打印机现在可以打印下一秒中的内容，并且在任务所需要的时间中减去一秒
                \如果任务已经完成，则重置打印机为不忙碌状态
            3、在任务完成后，计算出总等待时间/平均等待时间
'''


class Printer(object):
    # 打印机类，主要的任务是确定当前是否有任务，是否繁忙，计算所需时间，重置打印机状态等
    
    def __init__(self,ppm):
        self.pagerate = ppm                 # 打印速度
        self.currentTask = None             # 当前任务
        self.timeRemaining = 0              # 等待时机
    
    def tick(self):
        # 模拟时间流逝~~
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:             # 如果时间小于等于，重置当前任务为空
                self.currentTask = None
    
    def busy(self):
        # 返回当前是否繁忙
        if self.currentTask != None:
            return True
        else:
            return False
    
    def startNext(self,newtask):
        # 开始下一个任务，收另外一个对象~
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60/self.pagerate      # 根据还有任务的打印数量计算任务所需时间

class Task(object):
    # 打印任务类，利用随机数函数提供一个1-20页的打印长度
    # 此外每个任务还有一个时间戳的属性，用来表示任务创建并放置在打印队列中的时间
    
    def __init__(self,time):
        self.timestamp = time                       # 时间
        self.pages = random.randrange(1,21)         # 随机打印数量
        
    def getStamp(self):
        # 获取时间
        return self.timestamp
    
    def getPages(self):
        # 获取数量
        return self.pages
    
    def waitTime(self,currenttime):
        # 计算等待时间
        return currenttime - self.timestamp
    
def simulation(numSeconds,pagesPerMinute):
    
    # 初始化
    labprinter = Printer(pagesPerMinute)        # 创建打印对象，传入一页打印所需时间
    printQueue = queue.Queue()                  # 创建打印队列
    waitingtimes = []                           # 等待时机
    
    for currentSecond in range(numSeconds):
        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)
        
        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)
            
        labprinter.tick()
    averageWait = sum(waitingtimes)/len(waitingtimes)
    print ("Average Wait %6.2f secs %3d tasks remaining."%(averageWait,printQueue.size()))

def newPrintTask():
    # 是否创建一个新的打印任务的函数
    num = random.randrange(1,181)
    if num == 180:
        return True
    else:
        return False

if __name__ == '__main__':
    import random,queue
    for i in range(10):
        simulation(3600,5)