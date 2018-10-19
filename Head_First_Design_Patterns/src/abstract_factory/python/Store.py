# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 21:30:18 2018

@author: 凯风
"""

from abc import ABCMeta, abstractmethod
from factory import NYPizzaIngredientFactory, ChicagoPizzaIngredientFactory
from Pizza import CheesePizza, ClamPizza, PepperoniPizza, VeggiePizza

class PizzaStore(metaclass = ABCMeta):
    
    @abstractmethod
    def createPizza(self, item):
        pass
    
    def orderPizza(self, item):
        pizza = self.createPizza(item)
        print("---Making a " + pizza.getName() + " ---")
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza


class ChicagoPizzaStore(PizzaStore):
    def createPizza(self, item):
        ingredientFactory = ChicagoPizzaIngredientFactory()
        
        if (item == "cheese"):
            pizza = CheesePizza(ingredientFactory)
            pizza.setName("Chicago Style Cheese Pizza")
        elif (item == "veggie"):
            pizza = VeggiePizza(ingredientFactory)
            pizza.setName("Chicago Style Veggie Pizza")
        elif (item == "clam"):
            pizza = ClamPizza(ingredientFactory)
            pizza.setName("Chicago Style Clam Pizza")
        elif (item == "pepperoni"):
            pizza = PepperoniPizza(ingredientFactory)
            pizza.setName("Chicago Style Pepperoni Pizza")
        
        return pizza
        
class NYPizzaStore(PizzaStore):
    def createPizza(self, item):
        ingredientFactory = NYPizzaIngredientFactory()
        
        if (item == "cheese"):
            pizza = CheesePizza(ingredientFactory)
            pizza.setName("New York Style Cheese Pizza")
        elif (item == "veggie"):
            pizza = VeggiePizza(ingredientFactory)
            pizza.setName("New York Style Veggie Pizza")
        elif (item == "clam"):
            pizza = ClamPizza(ingredientFactory)
            pizza.setName("New York Style Clam Pizza")
        elif (item == "pepperoni"):
            pizza = PepperoniPizza(ingredientFactory)
            pizza.setName("New York Style Pepperoni Pizza")
        
        return pizza














