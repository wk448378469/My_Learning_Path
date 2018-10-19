# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 22:04:33 2018

@author: 凯风
"""

from Store import NYPizzaStore, ChicagoPizzaStore

if __name__ == "__main__":
    
    nyStore = NYPizzaStore()
    chicagoStore = ChicagoPizzaStore()
    
    pizza = nyStore.orderPizza("cheese")
    print("Order a " + str(pizza) + "\n\n")

    pizza = chicagoStore.orderPizza("veggie")
    print("Order a " + str(pizza) + "\n\n")        