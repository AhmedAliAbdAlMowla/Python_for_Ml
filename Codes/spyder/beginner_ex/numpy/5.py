# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 00:37:52 2019

@author: Ahmed Ali
"""

import numpy as np

arr=np.random.rand(5,5)

print(arr)
#ex1
print(arr[0])
#ex2
print(arr[0][0])
#ex3
print(arr[1][2])
#ex4
print(arr[1,2])

#  notes: ex3 ==ex4  defrant way same resolt


# sup 2d
new_arr2d=np.array(arr[1:3,2:4])
print(new_arr2d)
# الاقتصاص  انك تقص من مصفوفه اجزاء وتخزنها ك مصفوفه جديدة 
ne=np.arange(0,10)
nee=ne[2:6] #   اقتصاص عادى 
neee=ne[1:9:2]# اقتصاص ولاكن ال step =2


new_arr2d2=arr[2:4,1:3]
print(new_arr2d2)

print(type(new_arr2d),type(new_arr2d2))

new_arr2d2[:]=1.6   # you can see arr is chang py 1.6 becouse refranse


new_arr2d3=arr[3:5,2:4].copy() # . copy( )  solve this and new array not refrance from arr
print(new_arr2d3)
new_arr2d3[:]=1.7  

# condetion selection 
result = (arr>0.6)
print(result) # boolean array hold true or false for any elemint in mtrex (mask)
print(type(result))

#الاراى اللى اسمها ريسولت اللى فاتت الناس بتسميها مسك 
#وبتستخدمها علشان تجيب فيكتور بكل انتايج اللى جابت ترو فالمقارنه

cond_selec=arr[result] # this is mask operation
print(cond_selec)
type(cond_selec)

cond_selec2=arr[arr>0.3]
