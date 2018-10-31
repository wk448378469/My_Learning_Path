# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 00:49:56 2018

@author: 凯风

请先启动一个命令行输入 python -m Pyro4.naming
"""

import Pyro4

@Pyro4.expose
class GumballMachine(object):
    
    def __init__(self, location, count):
        self.location = location
        self.count = count
    
    def getLocation(self):
        return self.location
    
    def getCount(self):
        return self.count


if __name__ == "__main__":
    machine1 = GumballMachine("beijing", 10)
    machine2 = GumballMachine("shanghai", 20)
    machine3 = GumballMachine("guangdong", 30)
    
    daemon = Pyro4.Daemon()
    ns = Pyro4.locateNS()
    uri1 = daemon.register(machine1)
    uri2 = daemon.register(machine2)
    uri3 = daemon.register(machine3)
    
    ns.register("machine1", uri1) 
    ns.register("machine2", uri2) 
    ns.register("machine3", uri3)
    
    daemon.requestLoop()
    
