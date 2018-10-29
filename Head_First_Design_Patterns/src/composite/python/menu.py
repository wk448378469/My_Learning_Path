# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 10:04:53 2018

@author: 凯风
"""

from abc import ABCMeta, abstractmethod
from iterator import CompositeIterator, NullIterator

class MenuComponent(metaclass = ABCMeta):
    def add(self, menuComponent):
        raise NotImplementedError()
    
    def remove(self, menuComponent):
        raise NotImplementedError()
    
    def getChild(self, i):
        raise NotImplementedError()
    
    def getDescription(self):
        raise NotImplementedError()
    
    def getPrice(self):
        raise NotImplementedError()
    
    def isVegetarian(self):
        raise NotImplementedError()
    
    @abstractmethod
    def createIterator(self):
        pass

    def prints(self):
        raise NotImplementedError()
        


class Menu(MenuComponent):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.iterator = None
        self.menuComponents = []
    
    def add(self, menuComponent):
        self.menuComponents.append(menuComponent)
    
    def remove(self, menuComponent):
        self.menuComponents.remove(menuComponent)
    
    def getChild(self, i):
        return self.menuComponents[i]

    def getName(self):
        return self.name
    
    def getDescription(self):
        return self.description
    
    def createIterator(self):
        if (self.iterator == None):
            self.iterator = CompositeIterator(self.menuComponents)
        return self.iterator
    
    def prints(self):
        print("\n" + self.getName())
        print(", " + self.getDescription())
        print("--------------------------")
        
                

class MenuItem(MenuComponent):
    def __init__(self, name, description, vegetarian, price):
        self.name = name
        self.description = description
        self.vegetarian = vegetarian
        self.price = price
    
    def getName(self):
        return self.name
    
    def getDescription(self):
        return self.description
    
    def getPrice(self):
        return self.getPrice
    
    def isVegetarian(self):
        return self.vegetarian
    
    def createIterator(self):
        return NullIterator()
    
    def prints(self):
        print("  " + self.getName())
        if(self.isVegetarian()):    
            print("(v)")
        
        print(", " + self.getPrice())
        print("     -- " + self.getDescription())
        





