# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 15:21:19 2017

@author: 凯风
"""

'''
    图：
        利用字典来保存图的相关信息
'''


class Vertex(object):
    # 结点的类
    
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
    
    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight          # 该结点连接其他结点，以及权重
    
    def __str__(self):
        # 也是一个内置函数
        # 利用print打印属性时，不至于把地址打出来
        return str(self.id) + 'connectedTo' + str([x.id for x in self.connectedTo])
    
    def getConnections(self):
        # 获取该结点的连接的其他结点
        return self.connectedTo.keys()
    
    def getId(self):
        # 获取该结点的ID
        return self.id

    def getWeight(self,nbr):
        # 获取该结点与nbr之间的权重
        return self.connectedTo[nbr]
    

class Graph(object):
    # 图的类
    
    def __init__(self):
        self.vertList = {}              # 保存结点对象的
        self.numVertices = 0            # 结点数量
    
    def addVertex(self,key):
        # 添加结点
        self.numVertices = self.numVertices + 1         # 增加结点数量
        newVertex = Vertex(key)                         # 创建结点对象
        self.vertList[key] = newVertex                  # 结点对象添加到图中
        return newVertex                                # 返回结点对象
    
    def getVertex(self,n):
        # 获取结点
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None
    
    def __contains__(self,n):
        # 内置函数
        # 可以用in这个方法
        return n in self.vertList
    
    def addEdge(self,f,t,cost=0):
        # 添加结点与结点之间的连接
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t],cost)
    
    def getVertices(self):
        # 添加图中所有结点的key
        return self.vertList.keys()
    
    def __iter__(self):
        # 内置函数
        # 可以利用for进行迭代~
        return iter(self.vertList.values())
    
if __name__ == '__main__':
    g = Graph()
    for i in range(6):
        g.addVertex(i)
    g.vertList
    g.addEdge(0,1,5)
    g.addEdge(0,5,2)
    g.addEdge(1,2,4)
    g.addEdge(2,3,9)
    g.addEdge(3,4,7)
    g.addEdge(3,5,3)
    g.addEdge(4,0,1)
    g.addEdge(5,4,8)
    g.addEdge(5,2,1)
    for v in g:
        for w in v.getConnections():
            print ("( %s , %s )" % (v.getId(), w.getId()))

