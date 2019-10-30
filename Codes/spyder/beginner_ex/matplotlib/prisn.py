# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 04:07:18 2019

@author: Ahmed Ali
"""


import numpy as np
import pandas as pd
from sklearn import svm
import sklearn as sl
import math as mh
from matplotlib import pyplot as plt
import seaborn as ses

data=pd.read_excel('F:\\Egypt.xlsx')

plt.style.use('ggplot')

data.plot(x='year',y='pooulation')

data.plot(x='year',y='pooulation',kind='bar')



data.plot(x='year',y='pooulation',kind='barh')


data.plot(x='year',y='pooulation',kind='pie')

data.plot(x='year',y='pooulation',kind='line')

ses.kdeplot(data)





plt.plot(data['year'],data['pooulation'],marker='o',markersize=8,color='red',markerfacecolor='black')




plt.plot(data['year'],data['pooulation'],linestyle=':')




plt.plot(data['year'],data['pooulation'],linestyle='-.')




plt.pie(data['pooulation'],labels=data['year'])


plt.pie(data['pooulation'],labels=data['year'],explode=[0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2])

plt.bar(data['year'],data['pooulation'])







plt.plot(data['year'],data['pooulation'],'ro')

