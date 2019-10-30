# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 18:33:24 2019

@author: Ahmed Ali
"""


 
 
import numpy as np
import pandas as pd
from sklearn import svm
import sklearn as sl
import math as mh

 
model=svm.SVR(kernel='linear' , C=1.0)

fl=pd.read_excel('F:\\qq.xlsx')

arx=np.array(fl)

xd=arx[:,0]
xdy=arx[:,1]
xd=np.array(xd).reshape(21,1)
model.fit(xd,xdy)
print(model.score(xd,xdy))

print(model.predict([[120]]))
