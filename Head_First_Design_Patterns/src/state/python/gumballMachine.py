# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 22:21:15 2018

@author: 凯风
"""

from state import SoldOutState, SoldState, NoQuarterState, WinnerState, HasQuarterState

class GumballMachine(object):
    def __init__(self, count):
        self.soldOutState = SoldOutState(self)
        self.noQuarterState = NoQuarterState(self)
        self.hasQuarterState = HasQuarterState(self)
        self.soldState = SoldState(self)
        self.winnerState = WinnerState(self)
        
        self.count = count
        self.state = self.soldOutState
        
        if self.count > 0:
            self.state = self.noQuarterState
    
    def insertQuarter(self):
        self.state.insertQuarter()
    
    def ejectQuarter(self):
        self.state.ejectQuarter()
    
    def turnCrank(self):
        self.state.turnCrank()
        self.state.dispense()
    
    def releaseBall(self):
        print("A gumball comes rolling out the slot...")
        if self.count != 0:
            self.count = self.count - 1
    
    def getCount(self):
        return self.count

    def refill(self, count):
        self.count += count
        print("The gumball machine was just refilled, it's new count is: " + str(self.count))
        self.state.refill()
    
    def setState(self, state):
        self.state = state
    
    def getState(self):
        return self.state
    
    def getSoldOutState(self):
        return self.getSoldOutState

    def getNoQuarterState(self):
        return self.noQuarterState
    
    def getHasQuarterState(self):
        return self.hasQuarterState
    
    def getSoldState(self):
        return self.soldState
    
    def getWinnerState(self):
        return self.winnerState
    
    def __str__(self):
        result = ""
        result += "\nMighty Gumball, Inc."
        result += "\nJava-enabled Standing Gumball Model #2004\n"
        result += "{0}{1}{2}".format("Inventory: ", str(self.count), " gumball")
        if self.count != 1:
            result += "s"
        
        result += "\n"
        result += "{0}{1}{2}".format("Machine is ", str(self.state), "\n")
        return result

        
        
        
        
        