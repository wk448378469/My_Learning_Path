# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 16:09:13 2018

@author: 凯风
"""

from ModelDuck import ModelDuck
from MallardDuck import MallardDuck
from FlyRockectPowered import FlyRockectPowered

class MiniDuckSimulater(object):
    
    def __init__(self):
        mallard = MallardDuck()
        mallard.performFly()
        mallard.performQuack()
        mallard.display()
        mallard.swim()
        
        print("\n")
        
        model = ModelDuck()
        model.performFly()
        model.setFlyBehavior(FlyRockectPowered())
        model.performFly()


if __name__ == "__main__":
    MiniDuckSimulater()
    
    
        