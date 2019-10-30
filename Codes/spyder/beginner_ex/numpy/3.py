# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 21:39:06 2019

@author: Ahmed Ali
"""

import numpy as np

vect1=np.arange(15)

print(type(vect1))

#ـــــــــــــــــــــــــــــــــــ
# مهم جدااا تحويل الفيكتور ل متركس 
mtx1=np.reshape(vect1,(4,4))
#ـــــــــــــــــــــــــــــــــــ
#خلى بالك المتركس الجديدة لازم تكون بنفس الايليمنت اللى ف 
# الفيكتور يعنى لو الفيكتور طوله 30 يبقى المتركس 6*5 مثلا
#او 3*10 اى حاجه المهم نفس عدد الايليمنت
print(mtx1)

mxx=np.arange(18).reshape((3,6))# make matrex (3,6)


larg=np.max(vect1)
small=np.min(vect1)


print(larg)
print(small)

print(vect1.max())
print(vect1.min())


print(mtx1.max())
print(mtx1.min())
# موقع اكبر واصغر ارقام 
Location_max=np.argmax(mtx1)
Location_min=np.argmin(mtx1)
print(Location_max)
print(Location_min)


# مهم جدا بيقلك الاراى فيكتور ولا متركس وبيديلك الابعاد

print(np.shape(vect1))
print(np.shape(mtx1))

sx=np.shape(vect1)
print(sx)
type(sx)


