# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 16:07:53 2018

@author: 凯风
"""

from QuackBehavior import QuackBehavior

class MuteQuack(QuackBehavior):
    def __init__(self):
        pass
    
    def quack(self):
        print("<<Silince>>")