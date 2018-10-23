# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 16:12:17 2018

@author: 凯风
"""

from Duck import Duck
from FlyNoWay import FlyNoWay
from Quack import Quack

class ModelDuck(Duck):
    def __init__(self):
        self.flyBehavior = FlyNoWay()
        self.quackBehavior = Quack()
    
    def display(self):
        print("I'm a model duck")