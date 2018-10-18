# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 17:40:56 2018

@author: 凯风
"""

from Coffee import DarkRoast,Decaf,Espresso,HouseBlend
from Condiment import Mocha,Soy,Whip

class StartbuzzCoffee(object):
    def __init__(self):

        coffee2 = Decaf()
        print("{0} ${1}\n".format(coffee2.getDescription(),coffee2.cost()))
        
        coffee3 = Espresso()
        coffee3 = Soy(coffee3)
        print("{0} ${1}\n".format(coffee3.getDescription(),coffee3.cost()))

        coffee1 = DarkRoast()
        coffee1 = Mocha(coffee1)
        coffee1 = Whip(coffee1)
        print("{0} ${1}\n".format(coffee1.getDescription(),coffee1.cost()))
        
        coffee4 = HouseBlend()
        coffee4 = Whip(coffee4)
        coffee4 = Soy(coffee4)
        coffee4 = Mocha(coffee4)
        print("{0} ${1}\n".format(coffee4.getDescription(),coffee4.cost()))

if __name__ == "__main__":
    StartbuzzCoffee()