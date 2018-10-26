# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 15:27:26 2018

@author: 凯风
"""

from interface import Menu, MenuItem
from iterator import DinerMenuIterator, PancakeHouseMenuIterator


class DinerMenu(Menu):
    
    def __init__(self):
        self.menuItems = []
        self.addItem("Vegetarian BLT","",True, 2.99)
        self.addItem("BLT","", False, 2.99)
        self.addItem("Soup of the day", "", False, 3.29)
        self.addItem("Hotdog","", True, 3.05)
    
    def addItem(self, name, desc, vegetarian, price):
        menuItem = MenuItem(name, desc, vegetarian, price)
        self.menuItems.append(menuItem)
    
    def createIterator(self):
        return DinerMenuIterator(self.menuItems)

class PancakeHouseMenu(Menu):
    
    def __init__(self):
        self.menuItems = {}
        self.addItem("K&B's Pancake Breakfast", "", True,2.99)
        self.addItem("Regular Pancake Breakfast", "", False, 2.99)
        self.addItem("Blueberry Pancakes", "", True, 3.49)
        self.addItem("Waffles", "", True, 3.59)
    
    def addItem(self, name, desc, vegetarian, price):
        menuItem = MenuItem(name, desc, vegetarian, price)
        self.menuItems[name] = menuItem
    
    def createIterator(self):
        return PancakeHouseMenuIterator(self.menuItems)
    