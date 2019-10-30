# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 13:23:25 2019

@author: Ahmed Ali
"""


import numpy as np
import pandas as pd

 #data frame     مهم جداااااااا
     
 
arr=np.array([
         
         [10,20,30,40],
         [20,30,40,50],
         [30,40,50,60],
         [40,50,60,70],
         [50,60,70,80]
         
              ])

col=['Math','Physics','French','Chemisty']
row=['a','b','c','d','e']
 
Grade=pd.DataFrame(arr,index=row,columns=col)
 
print(Grade)
 #___________________________________________________________

print(Grade.loc[Grade.Math >21  ])  #طباعة الصفوف اللتى درجة الماث فيها اكبرمن21

#طباعة العمودين المعينين ف الصفوف التى توافى للشرط 
print(Grade.loc[Grade.Physics>=30,['Math','Chemisty']])
#قيس عل ذلك ممكن تحط الشروط اللى انت عايزها 
#______________________________________________________________
#                             sort    
print(Grade.sort_values(['Math'] ,ascending=False))
 
print(Grade.sort_values(['Math'],ascending=True)) 

#يتم الترتيب تنازليا او تصاعديا بناء عن اسيندانج ترواوفولس
#المكان اللى فيه ماث ده العمود اللى هيتم الترتيب عليه 
#______________________________________________________________
#                     رســــــــــم               
Grade.plot()
Grade.plot(kind='bar')
Grade.plot(kind='barh')
#______________________________________________________________
print(Grade.max())
print(Grade.min())    # بجيب القيم لكل الاعمده
print(Grade.std())
print(Grade.mean())

print(Grade['Math'].max())              # بجيب القيم ل اعمده معينه 
print(Grade['French'].min())
print(Grade['Math'].mean())
print(Grade['French'].std())
















     