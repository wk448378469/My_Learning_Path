# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 22:03:51 2018

@author: 凯风
"""

from interface import Duck, Turkey

class MallardDuck(Duck):
    def quack(self):
        print("Quack~")
    
    def fly(self):
        print("I'm flying~")


class WildTurkey(Turkey):
    def gobble(self):
        print("Gobble gobble~")
    
    def fly(self):
        print("I'm flying a short distance")