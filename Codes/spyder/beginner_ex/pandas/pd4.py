# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 14:20:20 2019

@author: Ahmed Ali
"""

import numpy as np
import pandas as pd

arr=np.random.randint(3,12,20).reshape(5,4)

col=['Math','French','English','programing']
row=['a','b','c','d','e']

Grade=pd.DataFrame(arr,index=row,columns=col)

print(Grade)
#____________________________________________
# مقادير احصائيه 
print(Grade.corr())   #  بيديلك العلاقات بينهم علاقات التقارب 
print(Grade.skew()) #  مقدار الانحراف
#____________________________________________

print(Grade)

    Grade['Total']=[0,0,0,0,0] #انشاء عمود جديد

for i in col:
    Grade['Total']+=Grade['Math']

print(Grade)

Grade['Math']*=2
print(Grade)
#_________________________________________________________________
# eval بتنفذ اللى هتديهولها ف شكل استرنج وترجعلكالقيمه 
result =pd.eval("(Grade.Math+Grade.English)/2")

print(result)

Grade['NEW']=pd.eval("Grade.Math+Grade.French")

print(Grade)
#_____________________________________________________________________
#             query    بتديلها الشروط اللى انت عايزها
# وبترجعلك داتا فريم فيه الحجات المطابق       
 
result2=Grade.query('French>6 and programing>4')

print(Grade)
print(result2)



result3=Grade.query('French>3 and programing>4')
print(result3)

result4=Grade.query('French==6 or programing==6')
print(result4)
#______________________________________________________________________
re1=Grade.Math >12
re2=Grade.English>6
re3=re1&re2
print(Grade[re3])   # mask trick

#__________________________________________
def make_df(coles,ind):
    data={c:[str(c)+str(i) for i in ind]for c in coles}
    return pd.DataFrame(data,ind)
                                   # فنكشن روشنه كدا بترجع الداتا فريم 
print(make_df('ABC',range(3)))

