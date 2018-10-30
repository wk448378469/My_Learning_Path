# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 22:32:02 2018

@author: 凯风
"""

from gumballMachine import GumballMachine

if __name__ == "__main__":
    g = GumballMachine(10)
    
    print(str(g))
    
    g.insertQuarter()
    g.turnCrank()
    
    print(str(g))
    
    g.insertQuarter()
    g.turnCrank()
    g.insertQuarter()
    g.turnCrank()
    g.insertQuarter()
    g.turnCrank()
    g.insertQuarter()
    g.turnCrank()
    
    print(str(g))
    
    