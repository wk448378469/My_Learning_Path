# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 22:11:17 2018

@author: 凯风
"""

from sub import MallardDuck, WildTurkey
from adapter import TurkeyAdapter
from interface import Duck

def requirer(duck):
    if isinstance(duck, Duck):
        duck.quack()
        duck.fly()
    else:
        raise Exception("bad duck!!!")

if __name__ == "__main__":
    duck = MallardDuck()
    turkey = WildTurkey()
    
    turkeyAdapter = TurkeyAdapter(turkey)
    
    print("The Turkey says...")
    turkey.gobble()
    turkey.fly()
    
    print("\nThe Duck says...")
    requirer(duck)
    
    print("\nThe TurkeyAdapter says...")
    requirer(turkeyAdapter)
    
    