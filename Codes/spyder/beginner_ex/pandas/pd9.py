# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 02:20:18 2019

@author: Ahmed Ali
"""

import numpy as np
import pandas as pd

 # الملفات                                

#القرائه من ملف csv
df=pd.read_csv('D:\\IRIS.csv')
print(df)             
# القرائه من ملف اكسل            
df2=pd.read_excel('D:\\yourcopy.xlsx')

print(df2)
print(df.head(20))

print(df.head(5))
ar=np.array(np.random.randint(1,12,25)).reshape(5,5)

col=['a','b','c','d','e']
row=['aa','bb','cc','dd','ee']

df3=pd.DataFrame(ar,columns=col,index=row)


#الكتابه للملفات 
#ولو الملف موش موجود هيتم أنشائه
df3.to_excel('D:\\test.xlsx',sheet_name ='sheet 1')

# لو البيانات موجوده بس الاعمده ملهاش اسماء ممكن تضيف الاسماء انت 


ar2=np.array(np.random.randint(0,30,30)).reshape(6,5)

df4=pd.DataFrame(ar2)

df4.to_excel('D:\\test2.xlsx')
col2=['aa','bb','cc','dd','ee']
#هنا هيضيف الكولوم 2 للداتا فريم 
filedata=pd.read_excel('D:\\test2.xlsx',names=col2)
print(filedata)
#بقله خلى بالك الشاشه اللى هتعرضلى عليها عرضها 100 رقم علشان يعرض
pd.set_option('display.width',100)
#معناها لو عندك ارقام عشريه كبيره هاتلى 3 ارقام بس بعد العلامه
pd.set_option('precision',3)
print(df)

desc=df.describe()

print(desc)
