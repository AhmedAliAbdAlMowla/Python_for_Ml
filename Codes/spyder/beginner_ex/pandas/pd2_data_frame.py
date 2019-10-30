# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 10:21:13 2019

@author: Ahmed Ali
"""
import numpy as np
import pandas as pd
import matplotlib as mp
import sklearn as sl
import seaborn as sb
import keras as ks
import tensorflow as ts
import theano as to
# data frame      مهم جدااااااااا
#                     الطريقة الاولى للأنشاء   
array1=np.array([
                 [1,20,30,5],
                 [61,9,80,7],
                 [3,6,47,90],
                 [9,65,7,10],
                 [6,32,4,70]
                  ])
       

col=['w','e','r','t']
row=['a','b','c','d','e']
 #لاحظ توافق عدد الصفوف والاعمدة ف الاسماء والمتركس نفسه 
df=pd.DataFrame(array1,index=row,columns=col)     #data frame creat
print(df)




#   ملاحظه مهم 
#  لو مديتش للفنكشن بتاعت الداتا فريم ال ليست بتاعت الانديكس 
# هتعملهم ديفولت من ال 0 ل فوق 
#
df3=pd.DataFrame(array1,columns=col) 
print(df3)


#____________________________________________________________________
#                             الطريقة الثانية للأنشاء

w=pd.Series({'a':1,'b':2,'c':3,'d':4})
x=pd.Series({'a':2,'b':3,'c':4,'d':5})
y=pd.Series({'a':3,'b':4,'c':5,'d':6})
z=pd.Series({'a':4,'b':5,'c':6,'d':7})

df2=pd.DataFrame({'play':w,'work':x,'drink':y,'eat':z})
print(df2)
#_________________________________________________________
#الطريقة الثالثة للأنشاء 
data1=[{'square':i**2} for i in range(10)]
df4=pd.DataFrame(data1)
print(df4)

data2=[{'square':i**2,'root':i**0.5,'cube':i**3}
             for i in range(10)]

df5=pd.DataFrame(data2)
print(df5)

ss=54
roww=[]
for i in range(10):
    ss+=1
    roww.append(ss)

print(roww)    
df6=pd.DataFrame(data2,index=roww)
print(df6)
df7=pd.DataFrame([{'a':1,'b':2},{'a':2,'b':3},{'a':3,'b':4}])
print(df7)
df8=pd.DataFrame([{'a':1,'b':2},{'c':2,'d':3},{'e':3,'f':4}])
print(df8)
#لاحظ حط ف الاماكن اللى مدتلهاش قيم non

 #____________________________________________________________________
print(df['w'])#لو عايز اطبع عامود معين من الداتا فريم بنده ب الاسم
# والعكس مينفعش لان الكى هوا الكولوم الرو لا 

print(df2['play'])

#_____________________________________________________________________
# الترانزبوس  transpose T
# المعكوس   المدور 
print(df2)
print(df2.T)    # المدور المعكوس الاثنين واحد
#_________________________________________________________________
print(df2.values) # طباعة القيم
print(df2.keys())    #طباعة المفاتيح 
#__________________________________________________________
print('play' in df2.keys())   # هل الكلمه موجوده ف المفاتيح او لا 
print('ahmed' in df2.keys())   # ترو او فولس
#_________________________________________________________
print(5 in df2.values)  #هل القم موجود ف القيم ام لا ترو او فلس
print(1223 in df2.values)
#____________________________________________________________
print(df2.stack())# بيطبع الداتا فريم بس ق شكل عودى 
#____________________________________________________________
#  طباعة اجزاء معينه من الداتا فريم عن طريق الانديكس 
print(df2.iloc[:3,1:2])
print(df2.iloc[:3,:3])
print(df2.iloc[1:2,2:3])
#_________________________________________________________________
#طباعة اجزاء معينه من الداتا فريم عن طريق الموقع ب الكى والرو
print(df2.loc['b':'c','work':])
#________________________________________________________________