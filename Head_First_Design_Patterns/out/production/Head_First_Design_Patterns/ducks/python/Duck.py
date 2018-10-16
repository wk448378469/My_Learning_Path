# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 15:44:07 2018

@author: 凯风
"""

from abc import ABCMeta, abstractmethod
from FlyBehavior import FlyBehavior
from QuackBehavior import QuackBehavior

class Duck(object):
    __metaclass__ = ABCMeta
    
    def _init_(self):
        self.flyBehavior = None
        self.quackBehavior = None
        
    @abstractmethod
    def display():
        pass
    
    def performFly(self):
        self.flyBehavior.fly()

    def performQuack(self):
        self.quackBehavior.quack()
    
    def swim(self):
        print("All ducks float, even decoys")
    
    def setFlyBehavior(self, fb):
        if (isinstance(fb, FlyBehavior)):
            self.flyBehavior = fb
        else:
            raise TypeError("bad value")

    def setQuackBehavior(self, qb):
        if (isinstance(qb, QuackBehavior)):
            self.quackBehavior = qb
        else:
            raise TypeError("bad value")
    
    
    
    
    