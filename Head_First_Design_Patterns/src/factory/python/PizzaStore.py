# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 09:46:02 2018

@author: 凯风
"""

from Pizza import ChicagoStyleCheesePizza,ChicagoStyleClamPizza,NYStyleClamPizza,NYStyleVeggiePizza
from abc import ABCMeta, abstractmethod

class PizzaStore(metaclass = ABCMeta):
    @abstractmethod
    def createPizza(self, item):
        pass
    
    def orderPizza(self, _type):
        pizza = self.createPizza(_type)
        print("--- Making a " + pizza.getName() + " ---")
        
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        
        return pizza

class ChicagoPizzaStore(PizzaStore):
    def createPizza(self, item):
        if(item == "cheese"):
            return ChicagoStyleCheesePizza()
        elif(item == "clam"):
            return ChicagoStyleClamPizza()
        else:
            return None
        

class NYPizzaStore(PizzaStore):
    def createPizza(self, item):
        if(item == "clam"):
            return NYStyleClamPizza()
        elif(item == "veggie"):
            return NYStyleVeggiePizza()
        else:
            return None













