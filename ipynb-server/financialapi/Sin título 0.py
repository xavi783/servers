# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 10:04:48 2014

@author: jserrano
"""

class Struct(object):
    
    _fields = []    
    
    def __init__(self, *args, **kwargs): 
        # kwargs has preference
        if len(self._fields) and len(args):            
            for name, value in zip(self._fields, args):                
                setattr(self, name, value) if not name in kwargs.keys() else None
        # even if it is setted after
        if len(kwargs):  
            [setattr(self, name, value) for name, value in kwargs.items()]

class Program(Struct):
    _fields = ["id","type"];

p = Program(0, type=1)        