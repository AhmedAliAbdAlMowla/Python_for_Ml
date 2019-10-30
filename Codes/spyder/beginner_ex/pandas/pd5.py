# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 22:14:06 2019

@author: Ahmed Ali
"""

import numpy as np
import pandas as pd


# دمج ال داتا فريم 

df1=pd.DataFrame({'employe':['ahmed','ali','sheref','nada'],'salary':[
        32100,2222,3548,87875]})

df2=pd.DataFrame({'employe':['nada','ali','ahmed','sheref'],
                  'GPA':[3.8,2.7,3.3,3.9]})

df3=pd.merge(df1,df2)   # عملية الدمج 
print(df1)
print('__________________________')
print(df2)
print('__________________________')
print(df3)


#خلى بالك لازم يكون فيه عمود مشترك بين ال2 داتا فريم علشان تعرف تدمجهم
#موش شرط يكون اسم العمود نفس الاسم المهم يكون فيه نفس الداتا 

df4=pd.DataFrame({'name':['nada','ali','ahmed','sheref'],'grad':['goog'
                  ,'verygood','good','verygood']})
#هنا بيقله مين يكون ف الشمال ومين ف اليمين 
df5=pd.merge(df4,df3,left_on='name',right_on='employe') 
print(df3)
print(df5)

df5=df5.drop('name',axis=1) # حزف عمود 

df5=df5.set_index('employe')#غير المفتاح من الترتيب العادى 0و1 ل الامبلوى
print(df5)


df6=pd.DataFrame({'employe':['wty','ali','ahmed','sheref'],
                  'tr':[3.8,2.7,3.3,3.9]})



#________________________________________________________________
#________________________________________________________________
df7=pd.merge(df3,df6)#موش هيظهرلك غير الاسماء المشتركه بس
print(df7) 
df8=pd.merge(df3,df6, how='outer') #جاب الكل واستخدم non
print(df8)
#________________________________________________________________
#________________________________________________________________

df9=pd.merge(df3,df6,how='left')# هنا لازم يجيب الشمال كامل اين كان

df10=pd.merge(df3,df6,how='right')#هنا لازم يجيب اليمين كامل اين كان
#_________________________________________________________________________
# عض العمليات الاحصائيه 

print(df8.max())
print('__________________________')
print(df8.min())
print('__________________________')
print(df8.mean())   # المتوسط الحسايى عل الاعمده
print('__________________________')
print(df8.count())
print('__________________________')
print(df8.std())
print('__________________________')
print(df8.mean(axis=1))#المتوسط الحسابى عل الصفوف 
print('__________________________')
print(df8.sum())
print('__________________________')
print(df8['employe'].sum())
print('__________________________')
print(df8['salary'].sum())
#_________________________________________________________________________
#ملخص العمليات الاحصائيه 
#  نستخدك  describe
print(df8.describe())



