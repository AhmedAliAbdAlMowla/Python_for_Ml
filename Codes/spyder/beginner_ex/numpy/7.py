# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 14:35:59 2019

@author: Ahmed Ali
"""

import numpy as np

vect1=np.array(range(10))

vect2=vect1.copy()

np.random.shuffle(vect2) # resort randomly

mtx1=np.diag(vect2) # convert to matrex digonal in is vector 

print(mtx1)

vect3=np.arange(5)

mtx2=np.diag(vect3,2)    # 2 is add 2 row and 2 colum to matrex after digon

print(mtx2)    


mtx8=np.random.uniform(1,60,16)
print(mtx8)

mtx8=np.reshape(mtx8,(4,4))

#   counting ____________________________________________

count1=np.count_nonzero(mtx2>0)
print(count1)

count2=np.count_nonzero(mtx2==0)
print(count2)

count3=np.count_nonzero(mtx8>16)
print(count3)

print(np.count_nonzero(mtx8>15,axis=1)) # return vector count in any axis x
print(np.count_nonzero(mtx8>15,axis=0)) # return vector count in any axis y

x=np.count_nonzero(mtx8>15,axis=1)
y=np.count_nonzero(mtx8>15,axis=0)
print(type(x),type(y))#  array 

# boolean result 

reult=np.any(mtx1==3) # if he found 3 in mtrex return true else fuls

print(np.any(mtx1==8))
print(np.any(mtx1<0))

bomtx=np.any(mtx1>4,axis=1) # boolean matrex
print(bomtx)

print(np.all(mtx1>5))  # لازم الكل يفى ب الشرط 

print(np.all(mtx1>-1))

#__________________________________________________________
# المقارنه بين مصفوفتين ووجود نسب للتفاوت  مهم جدااا
A=np.random.randint(1,100,16)
B=np.random.randint(1,100,16)
A=np.reshape(A,(4,4))
B=np.reshape(B,(4,4))

Res=np.isclose(A,B,rtol=2) # نسبة السماح او التفاوت 

print(Res)

Res2=np.isclose(A,B,rtol=1)
print(Res2)

A=np.random.uniform(1,20,16)
B=np.random.uniform(1,20,16)
A=np.reshape(A,(4,4))
B=np.reshape(B,(4,4))
print(A)

rs=np.isclose(A,B,rtol=0.2) # 0.2
print(rs)
