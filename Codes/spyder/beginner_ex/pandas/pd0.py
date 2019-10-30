# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 08:46:16 2019

@author: Ahmed Ali
"""

import pandas as pd
#___________________________________
#فيكتور بس ليها انديكس شبه كى كدا
data =pd.Series([1.2,3.6,0.9,4.7])
print(data)  #هيطبع الفاليوا والانديكس
print(data.values)#طباعة الفاليوا
print(data.index)#طباعة الانديكس
print(data.keys)#طباعة الكى

#مهم بيجيب البيانات الاحصائيه 
print(data.describe()) #   <--
#تطبع اللى انت عايزه المهم تكتب اسم الفاليوا صح وهيطلع مع AGG
print(data.agg(['min','max','sum','mean','std']))
#ممكن انت تديله الكى والفاليوا 
data=pd.Series([1,2,9,6],index=['a','b','c','d'])
print(data)
#ممكن تديله ديكشنرى ب القيم وتخلص
data=pd.Series({'w':23,'rt':43,'i':9})
print(data)
#ممكن ننده عليها ب الكى 
print(data['i'])
#__________________________________

a=pd.Index([1,3,9,12])
b=pd.Index([3,1,6,7,9])
print(a)
print(b)
print(a & b)
print(a | b)
print(a ^ b)