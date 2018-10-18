# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 21:06:55 2018

@author: 凯风
"""

from factory import SimplePizzaFactory, PizzaStore

if __name__ == "__main__":
    factory = SimplePizzaFactory()
    store = PizzaStore(factory)
    
    pizza = store.orderPizza("cheese")
    print("We ordered a " + pizza.getName() + "\n")
    print(pizza)
    
    pizza = store.orderPizza("veggie")
    print("We ordered a " + pizza.getName() + "\n")
    print(pizza)    