# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 16:38:42 2018

@author: 凯风
"""

from Duck import Duck
from FlyWithWings import FlyWithWings
from Quack import Quack

class MallardDuck(Duck):
    def __init__(self):
        self.flyBehavior = FlyWithWings()
        self.quackBehavior = Quack()
    
    def display(self):
        print("I'm a real Mallard duck")