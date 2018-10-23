# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 22:06:42 2018

@author: 凯风
"""

from interface import Duck, Turkey
import random

class DuckAdapter(Turkey):
    def __init__(self, duck):
        self.duck = duck

    def gobble(self):
        self.duck.quack()
    
    def fly(self):
        if random.randint(1, 100) % 2 == 0:
            self.duck.fly()


class TurkeyAdapter(Duck):
    def __init__(self, turkey):
        self.turkey = turkey
    
    def quack(self):
        self.turkey.gobble()
    
    def fly(self):
        for i in range(3):
            self.turkey.fly()