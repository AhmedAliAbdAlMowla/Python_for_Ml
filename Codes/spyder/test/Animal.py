# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 11:14:24 2019

@author: Ahmed Ali
"""

class Dog:
    numofdog=0
    
    def __init__(self,col,eyeco,l=10):
        Dog.numofdog+=1
        self.color=col
        self.eyecol=eyeco
        self.lenth=l
    def calc(self,a):
        return self.numofdog*a


# فنكشن عاديه بس عايز اجرب استدعيها من ملف الانيملز   
def su(a,b):
    return a+b