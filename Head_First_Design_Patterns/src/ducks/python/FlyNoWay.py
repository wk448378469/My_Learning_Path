# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 16:06:23 2018

@author: 凯风
"""

from FlyBehavior import FlyBehavior

class FlyNoWay(FlyBehavior):
    def __init__(self):
        pass
    
    def fly(self):
        print("I can't fly")