# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 11:16:52 2018

@author: 凯风
"""

class Waitress(object):
    
    def __init__(self, allMenus):
        self.allMenus = allMenus
    
    def printMenu(self):
        self.allMenus.prints()
    
    def printVegetarianMenu(self):
        iterator = self.allMenus.createIterator()
        
        print("\nVEGETARIAN MENU\n----")
        while(iterator.hasNext()):
            menuComponent = iterator._next()
            try:
                if(menuComponent.isVegetarian()):
                    menuComponent.prints()
            except NotImplementedError:
                pass

