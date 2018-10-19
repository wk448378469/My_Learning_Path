# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 21:18:54 2018

@author: 凯风
"""

from abc import ABCMeta, abstractmethod
from Dough import ThickCrustDough, ThinCrustDough
from Sauce import MarinaraSauce, PlumTomatoSauce
from Cheese import MozzarellaCheese, ReggianoCheese
from Veggies import BlackOlives, Eggplant, Garlic, Mushroom, Onion, RedPepper, Spinach
from Pepperoni import SlicedPepperoni
from Clam import FreshClams, FrozenClams

class PizzaIngredientFactory(metaclass = ABCMeta):
    @abstractmethod
    def createDough(self):
        pass

    @abstractmethod
    def createSauce(self):
        pass

    @abstractmethod
    def createCheese(self):
        pass

    @abstractmethod
    def createVeggies(self):
        pass

    @abstractmethod
    def createPepperoni(self):
        pass

    @abstractmethod
    def createClam(self):
        pass


class NYPizzaIngredientFactory(PizzaIngredientFactory):
    def createDough(self):
        return ThinCrustDough()
    
    def createSauce(self):
        return MarinaraSauce()
    
    def createCheese(self):
        return ReggianoCheese()
    
    def createVeggies(self):
        return [Garlic(), Onion(), Mushroom(), RedPepper()]
    
    def createPepperoni(self):
        return SlicedPepperoni()
    
    def createClam(self):
        return FreshClams()


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    def createDough(self):
        return ThickCrustDough()
    
    def createSauce(self):
        return PlumTomatoSauce()
    
    def createCheese(self):
        return MozzarellaCheese()
    
    def createVeggies(self):
        veggies = [BlackOlives(), Spinach(), Eggplant()]
        return veggies
    
    def createPepperoni(self):
        return SlicedPepperoni()
    
    def createClam(self):
        return FrozenClams()
    