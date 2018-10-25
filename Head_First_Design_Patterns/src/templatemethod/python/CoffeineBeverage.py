# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 09:59:57 2018

@author: 凯风
"""

from abc import ABCMeta, abstractmethod

class CoffeineBeverage(metaclass = ABCMeta):
    
    def prepareRecipe(self):
        self.boilWater()
        self.brew()
        self.pourInCup()
        
        if self.customerWantsCondiments():
            self.addCondiments()
    
    @abstractmethod
    def brew(self):
        pass

    @abstractmethod
    def addCondiments(self):
        pass
    
    def boilWater(self):
        print("Boiling water")
    
    def pourInCup(self):
        print("Pouring into cup")
    
    def customerWantsCondiments(self):
        return True


class Coffee(CoffeineBeverage):
    def brew(self):
        print("Dripping Coffee through filter")
    
    def addCondiments(self):
        print("Adding Sugar and Milk")
    
    def customerWantsCondiments(self):
        answer = self.__getUserInput()
        if answer.lower().startswith("y"):
            return True
        else:
            return False
    
    def __getUserInput(self):
        answer = input("Would you like milk and sugar with your coffee (y/n)?")
        
        if len(answer) == 0:
            return "no"
        
        return answer


class Tea(CoffeineBeverage):
    def brew(self):
        print("Steeping the tea")
    
    def addCondiments(self):
        print("Adding Lemon")
    
    def customerWantsCondiments(self):
        answer = self.__getUserInput()
        if answer.lower().startswith("y"):
            return True
        else:
            return False
    
    def __getUserInput(self):
        answer = input("Would you like lemon with your tea (y/n)?")
        
        if len(answer) == 0:
            return "no"
        
        return answer
        
        
if __name__ == "__main__":
    tea = Tea()
    coffee = Coffee()
    
    print("\nMaking tea...")
    tea.prepareRecipe()
    
    print("\nMaking coffee...")
    coffee.prepareRecipe()