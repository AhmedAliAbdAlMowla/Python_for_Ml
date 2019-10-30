# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 12:38:43 2019

@author: Ahmed Ali
"""

import numpy as np

ar=[[1,2,3],[6,5,4]]
arr=np.array(ar)

print (type(arr))

print(len(arr))
print(arr.size)

arr2=arr[0:2,:2].copy()

print(arr2)

lst=np.array(range(0,50,7))

mx1=np.linspace(0,60,78)


mx2=np.random.randint(1,15,20)

mx3=np.reshape(mx2,(4,5))

print(mx3)
#np.shape بتديلك المصفوفه كام ف كام 
print(np.shape(mx3))
print(np.shape(arr))

print(np.ndim(mx3)) #  بيديلك هيا كام بعد 2 ولا 3 ولا 1 ولا ايه

print(mx3.dtype)# بيديلك نوع البيانات اللى ف المصفوفة 

mx4=np.array([range(i,i+3) for i in [2,6,9]])

print(mx4)
#فارغة والقيم الموجوده بها تساوى صفر لانها ب ال سالب
mx5=np.empty((4,4))

print(mx5)

aa= np.random.uniform(1,10)
lst2=np.random.uniform(1,20,9)   #9 number number
lst2=np.reshape(lst2,(3,3)) #convert from 1d to 2d 


#________________________________________
#   verry import 

ll=[1,2,3,4,5,6,7,8,9,10,11,12]
ll=np.array(ll)
print(ll)

np.random.shuffle(ll)   #   الخــلط العشوائى او الترتيب العشوائى 
print( ll)

#___________________________________________





