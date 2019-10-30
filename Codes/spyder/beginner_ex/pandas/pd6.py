# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 02:00:33 2019

@author: Ahmed Ali
"""

import numpy as np
import pandas as pd

#   ال groupby                                

df=pd.DataFrame({'Key':['A','B','C','A','B','C'],
                 'data':range(6) })

print(df)
print(df.groupby('Key').sum())

# شوف يا اخى الجروبى دى اداه جامده بتجمع القيم المتشابهه وبتجمع قيمهم
# مع بعض وتديلهم نفس المفتاح مثلا اذا كانت القيم مفاتيح زى المثال


print(df.groupby('Key').describe()) #جروبى مع ديسكريب علشانالبيانات الاحصائيه


#فرد للبيانات الاحصائيه 
print(df.groupby('Key').describe().unstack()) 


df=pd.DataFrame({'Key':['A','B','C','A','B','C'],
                 'data1':range(6),
                 'data2':np.random.randint(0,10,6)
        })
print(df)
#_____________________________________________________________
#اجريت ده بناء عل الشروط بيجيب 
#الصغير ف داتا1 ولو لقيهم متساوين يجيب الكبير فداتا2
df2=df.groupby('Key').aggregate({'data1':'min','data2':'max'})
#_____________________________________________________________
print(df2)





