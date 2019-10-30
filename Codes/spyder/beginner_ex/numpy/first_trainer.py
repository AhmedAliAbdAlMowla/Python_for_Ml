# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 01:59:19 2019

@author: Ahmed Ali
"""
import numpy as np
import pandas as pd
from sklearn import svm
import sklearn as sl

x=[[0,0,1],[2,2,3],[4,4,0]]
y=[0.5,2.5,7]

my_model=svm.SVR()
my_model.fit(x,y)

print('score',my_model.score(x,y))
print('out for [1,1,0] is ',my_model.predict([[1,1,0]]))

file_name='vcr_finalized_model.sav'
sl.externals.joblib.dump(my_model,file_name)

#بعد ماخزنت الموديل تقدر تعمله لود عل طول من غير تدريب
#looded_model=sl.externals.joblib.load(file_name)


#print('score',my_model.score(x,y))
#print('out for [1,1,0] is ',my_model.predict([[1,1,0]]))


#ف الصفحه التانيه هتلاقى العمل بدون تدريب