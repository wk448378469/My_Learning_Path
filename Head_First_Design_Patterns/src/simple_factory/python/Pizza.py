# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 20:38:24 2018

@author: 凯风
"""

from abc import ABCMeta

class Pizza(metaclass = ABCMeta):
    
    def __init__(self):
        self.name = ""
        self.dough = ""
        self.sauce = ""
        self.toppings = []
        
    def getName(self):
        return self.name
    
    def prepare(self):
        print("Preparing " + self.name)
    
    def bake(self):
        print("Baking " + self.name)
    
    def cut(self):
        print("Cutting " + self.name)
    
    def box(self):
        print("Boxing " + self.name)
    
    def __str__(self):
        display = ""
        display += "--- " + self.name + " ----\n"
        display += self.dough + "\n"
        display += self.sauce + "\n"
        for topping in self.toppings:
            display += topping + "\n"
        return display


class CheesePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "Cheese Pizza"
        self.dough = "Regular Crust"
        self.sauce = "Marinara Pizza sauce"
        self.toppings.append("Fresh Mozzarella")
        self.toppings.append("Parmesan")


class ClamPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "Clam Pizza"
        self.dough = "Thin Crust"
        self.sauce = "White garlic sauce"
        self.toppings.append("Clams")
        self.toppings.append("Grated parmesan cheese")


class PepperoniPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "Pepperoni Pizza"
        self.dough = "Crust"
        self.sauce = "Marinara sauce"
        self.toppings.append("Sliced Pepperoni")
        self.toppings.append("Sliced Onion")
        self.toppings.append("Grated parmesan cheese")


class VeggiePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "Veggie Pizza"
        self.dough = "Crust"
        self.sauce = "Marinara sauce"
        self.toppings.append("Sliced mushrooms")
        self.toppings.append("Sliced red pepper")
        self.toppings.append("Sliced black olives")






