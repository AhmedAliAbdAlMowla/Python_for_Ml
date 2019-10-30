# -*- coding: utf-8 -*-
"""
Created on Sun May  5 01:43:59 2019

@author: Ahmed Abd Al Mowla
"""



import numpy as np
import pandas as pd
from sklearn import svm



x=pd.read_csv('E:\\heart.csv')

a=np.array(x)

w=a[:,:13]
e=a[:,13:]
my_modl=svm.SVC(kernel='linear',C=1.0)
my_modl.fit(w,e)

print(my_modl.score(w,e))

#             test valio
print(my_modl.predict(np.array([[37,1,2,130,250,0,1,187,0,3.5,0,0,2]])))




