# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 16:12:57 2018

@author: 凯风
"""

from menu import PancakeHouseMenu, DinerMenu

class Waitress(object):
    def __init__(self, pancakeHouseMenu, dinerMenu):
        self.pancakeHouseMenu = pancakeHouseMenu
        self.dinerMenu = dinerMenu
    
    def printMenu(self):
        pancakeIterator = self.pancakeHouseMenu.createIterator()
        dinerIterator = self.dinerMenu.createIterator()
        print("MENU\n----\nBREAKFASE")
        self.__printMenu(pancakeIterator)
        print("\nLUNCH")
        self.__printMenu(dinerIterator)
        
    
    def __printMenu(self, iterator):
        while(iterator.hasNext()):
            menuItem = iterator._next()
            print(menuItem.name + ",")
            print(str(menuItem.price) + " -- ")


if __name__ == "__main__":
    pancakeHouseMenu = PancakeHouseMenu()
    dinerMenu = DinerMenu()
    
    waitress = Waitress(pancakeHouseMenu, dinerMenu)
    
    waitress.printMenu()
    
    