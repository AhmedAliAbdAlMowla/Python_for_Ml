# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 17:06:06 2019

@author: Ahmed Ali
"""

import numpy as np
mx=np.arange(0,16)
mx=np.reshape(mx,(4,4)) 
mx2=mx.copy()
mx1=mx*3    #       1
mx2=np.full((4,4),0)
np.multiply(mx,3,out=mx2) #         2
#بترفع جميع عناصر المصفوفه ل اوس معين وبتخزن الناتج ف الout=
np.power(mx,2,out=mx1) #power
#             1            ==     2   نفس العمل 

#ينفع انفذ جميع العمليات الحسابيه عل المصفوفات
#مثل الجمع 
#بجمع جميع العناصر ولاكن صف صف او عمود عمود
su=np.add.reduce(mx1,axis=1) #بغير ال axisعلشان العمود والصف
 su=np.multiply.reduce(mx1,axis=1) #نفس الموضوع بس دى ضرب 
 #__________________________________________
 #الضرب التبادلى اللى يخليك تعمل متركس من فيكتور مثلا بناء عن القيم
 aa=np.arange(2,8)
 #بيضرب قسمه اول عنصر ف الفيكتور ويكون وحده جديدة وهذا ودايما بتكون مربعه 
 bb=np.multiply.outer(aa,aa)
zz=np.arange(2,6)
qw=np.multiply.outer(zz,aa) # يمكنها ضرب اى 2 فيكتور ف بعض
#________________________________________________________
# بيجمع القيم اللى ف كل سل وما قبلها ويخزن النتيجه فيه وفيه axis
su=np.add.accumulate(zz)
sf=np.multiply.accumulate(zz) # نفس الحوار يتاع الجمع بس ب الضرب بقا 

print(aa.dtype) #نوع البيانت اللى ف المصفوفة 
