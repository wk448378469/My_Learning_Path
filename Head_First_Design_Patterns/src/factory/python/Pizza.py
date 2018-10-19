# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 09:25:10 2018

@author: 凯风
"""

from abc import ABCMeta

class Pizza(metaclass = ABCMeta):
    def __init__(self):
        self.name = ""
        self.dough = ""
        self.sauce = ""
        self.toppings = []
    
    def prepare(self):
        print("Prepare" + self.name)
        print("Tossing dough...")
        print("Adding sauce...")
        print("Adding toppings:")
        for topping in self.toppings:
            print("    " + topping)
    
    def bake(self):
        print("Bake for 25 minutes at 350")
    
    def cut(self):
        print("Cut the pizza into diagonal slices")
    
    def box(self):
        print("Place pizza in official PizzaStore box")
    
    def getName(self):
        return self.name

    def __str__(self):
        display = "---- " + self.name + " ----\n"
        display += self.dough + "\n"
        display += self.sauce + "\n"
        for topping in self.toppings:
            display += topping + "\n"
        
        return display

class ChicagoStyleCheesePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "Chicago Style Deep Dish Cheese Pizza"
        self.dough = "Extra Tick Crust Dough"
        self.sauce = "Plum Tomato Sauce"
        self.toppings.append("Shredded Mozzarella Cheese")
    
    def cut(self):
        print("Cutting the pizza into square slices")


class ChicagoStyleClamPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "Chicago Style Clam Pizza"
        self.dough = "Extra Thick Crust Dough"
        self.sauce = "Plum Tomato Sauce"
        self.toppings.append("Shredded Mozzarella Cheese")
        self.toppings.append("Frozen Clams from Chespeake Bay")
    
    def cut(self):
        print("Cutting the pizza into square slices")

class NYStyleClamPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "NY Style Clam Pizza"
        self.dough = "Thin Crust Dough"
        self.sauce = "Marinara Sauce"
        
        self.toppings.append("Grated Reggiano Cheese")
        self.toppings.append("Fresh Clams from Long Island Sound")

class NYStyleVeggiePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "NY Style Veggie Pizza"
        self.dough = "Thin Crust Dough"
        self.sauce = "Marinara Sauce"
        self.toppings.append("Grated Reggiano Cheese")
        self.toppings.append("Garlic")
        self.toppings.append("Onion")
        self.toppings.append("Mushrooms")
        self.toppings.append("Red Pepper")








