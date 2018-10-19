# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 21:36:47 2018

@author: 凯风
"""

from abc import ABCMeta, abstractmethod

class Pizza(metaclass = ABCMeta):
    name = ""
    dough = None
    sauce = None
    veggies = []
    cheese = None
    pepperoni = None
    clam = None
    
    @abstractmethod
    def prepare(self):
        pass
    
    def bake(self):
        print("Bake for 25 minutes at 350")
        
    def cut(self):
        print("Cutting")
    
    def box(self):
        print("boxing")
    
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name

    def __str__(self):
        result = "---- " + self.name + " ----\n"
        if (self.dough != None):
            result += str(self.dough) + "\n"
        if (self.sauce != None):
            result += str(self.sauce) + "\n"
        if (self.cheese != None):
            result += str(self.cheese) + "\n"
        if (self.veggies.count != 0):
            for i in range(len(self.veggies)):
                result += str(self.veggies[i])
                if (i < len(self.veggies) -1):
                    result += ", "
        if (self.clam != None):
            result += str(self.clam) + "\n"
        
        if (self.pepperoni != None):
            result += str(self.pepperoni) + "\n"
        
        return result
        
        

class CheesePizza(Pizza):
    def __init__(self, ingredientFactory):
        self.ingredientFactory = ingredientFactory
    
    def prepare(self):
        print("Prepareing " + self.name)
        self.dough = self.ingredientFactory.createDough()
        self.sauce = self.ingredientFactory.createSauce()
        self.cheese = self.ingredientFactory.createCheese()
        

class VeggiePizza(Pizza):
    def __init__(self, ingredientFactory):
        self.ingredientFactory = ingredientFactory
    
    def prepare(self):
        print("Prepareing " + self.name)
        self.dough = self.ingredientFactory.createDough()
        self.sauce = self.ingredientFactory.createSauce()
        self.cheese = self.ingredientFactory.createCheese()
        self.veggies = self.ingredientFactory.createVeggies()


class ClamPizza(Pizza):
    def __init__(self, ingredientFactory):
        self.ingredientFactory = ingredientFactory
    
    def prepare(self):
        print("Prepareing " + self.name)
        self.dough = self.ingredientFactory.createDough()
        self.sauce = self.ingredientFactory.createSauce()
        self.cheese = self.ingredientFactory.createCheese()
        self.clam = self.ingredientFactory.createClam()


class PepperoniPizza(Pizza):
    def __init__(self, ingredientFactory):
        self.ingredientFactory = ingredientFactory
    
    def prepare(self):
        print("Prepareing " + self.name)
        self.dough = self.ingredientFactory.createDough()
        self.sauce = self.ingredientFactory.createSauce()
        self.cheese = self.ingredientFactory.createCheese()
        self.veggies = self.ingredientFactory.createVeggies()
        self.pepperoni = self.ingredientFactory.createPepperoni()