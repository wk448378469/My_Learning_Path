# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 10:11:14 2018

@author: 凯风
"""


class CompositeIterator(object):
    def __init__(self, iterator):
        self.stack = []
        self.stack.append(iterator)
    
    def _next(self):
        if (self.hasNext()):
            iterator = self.stack[0]
            component = iterator._next()
            self.stack.append(component.createIterator())
            return component
        else:
            return None
    
    def hasNext(self):
        if (len(self.stack) == 0):
            return False
        else:
            iterator = self.stack[0]
            if (not iterator.hasNext()):
                self.stack.pop()
                return self.hasNext()
            else:
                return True
    
    def remove(self):
        raise NotImplementedError()

class NullIterator(object):
    def _next(self):
        return None
    def hasNext(self):
        return False
        