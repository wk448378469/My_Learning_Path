# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 20:47:51 2018

@author: 凯风
"""

from Pizza import CheesePizza, ClamPizza, PepperoniPizza, VeggiePizza

class SimplePizzaFactory(object):
    
    def createPizza(self, _type):
        if (_type == "cheese"):
            pizza = CheesePizza()
        elif (_type == "pepperoni"):
            pizza = PepperoniPizza()
        elif (_type == "clam"):
            pizza = ClamPizza()
        elif (_type == "veggie"):
            pizza = VeggiePizza()
        else:
            pizza = None
    
        return pizza


class PizzaStore(object):
    def __init__(self, factory):
        self.factory = factory
        
    def orderPizza(self, _type):
        pizza = self.factory.createPizza(_type)
        
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        
        return pizza
