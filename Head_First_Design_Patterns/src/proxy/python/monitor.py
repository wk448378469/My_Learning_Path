# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 01:42:46 2018

@author: 凯风
"""

import Pyro4

class GumballMonitor(object):
    def __init__(self, machine):
        self.machine = machine
    
    def report(self):
        print("Gumball Machine: " + self.machine.getLocation())
        print("Current inventory: " + str(self.machine.getCount()))
    
    
if __name__ == "__main__":
    location = ["PYRONAME:machine1",
                "PYRONAME:machine2",
                "PYRONAME:machine3"]
    
    monitors = []
    
    for l in location:
        monitors.append(GumballMonitor(Pyro4.Proxy(l)))
    
    for m in monitors:
        m.report()