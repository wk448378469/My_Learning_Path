# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 20:24:38 2018

@author: 凯风
"""

import threading

class Singleton(object):
    _instanceLock = threading.Lock()
    
    @classmethod
    def getInstance(cls):
        if not hasattr(Singleton, "_uniqueInstance"):
            with Singleton._instanceLock:
                if not hasattr(Singleton, "_uniqueInstance"):
                    Singleton._uniqueInstance = Singleton()
        return Singleton._uniqueInstance
    
    def getDescription(self):
        return "I'm a classic Singleton!\n"

if __name__ == "__main__":
    obj1 = Singleton.getInstance()
    print(obj1.getDescription())
    
    obj2 = Singleton.getInstance()
    
    if(obj1 == obj2):
        print("two obj points to one memory address")