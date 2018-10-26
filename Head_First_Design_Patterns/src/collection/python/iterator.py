# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 15:37:31 2018

@author: 凯风
"""

from interface import Iterator

class DinerMenuIterator(Iterator):
    def __init__(self, items):
        self.items = items
        self.position = 0
        
    def _next(self):
        menuItem = self.items[self.position]
        self.position = self.position + 1
        return menuItem
    
    def hasNext(self):
        if (self.position >= len(self.items)):
            return False
        else:
            return True

class PancakeHouseMenuIterator(Iterator):
    def __init__(self, items):
        self.items = items
        self.menuItems = list(self.items.values())
        self.position = 0
        
    def _next(self):
        menuItem = self.menuItems[self.position]
        self.position = self.position + 1
        return menuItem

    def hasNext(self):
        if (self.position >= len(self.items)):
            return False
        else:
            return True