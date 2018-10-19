# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 09:56:58 2018

@author: 凯风
"""

from PizzaStore import NYPizzaStore, ChicagoPizzaStore

if __name__ == "__main__":
    nyStore = NYPizzaStore()
    chicagoStore = ChicagoPizzaStore()
    
    pizza = nyStore.orderPizza("clam")
    print("Order a " + pizza.getName() + "\n\n")
    
    pizza = nyStore.orderPizza("veggie")
    print("Order a " + pizza.getName() + "\n\n")

    pizza = chicagoStore.orderPizza("cheese")
    print("Order a " + pizza.getName() + "\n\n")

    pizza = chicagoStore.orderPizza("clam")
    print("Order a " + pizza.getName() + "\n\n")