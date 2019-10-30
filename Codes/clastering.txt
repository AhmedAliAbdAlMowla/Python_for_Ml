# -*- coding: utf-8 -*-
"""
Created on Sun May  5 03:40:04 2019

@author: Ahmed Abd Al Mowla
"""




import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

from matplotlib import style



data=pd.read_csv('E:\\heart.csv')

data_in_array=np.array(data)

w=data_in_array[:,:13]
e=data_in_array[:,13:]
my_modl=KMeans(n_clusters=2)
my_modl.fit(w,e)
print(my_modl.labels_)
print(my_modl.score(w,e))

colors=["g.","r.","c.","y."]



x=w[:,:1]    
y=w[:,3:4]

print(my_modl.predict(np.array([[37,1,2,130,250,0,1,187,0,3.5,0,0,2]])))



plt.scatter(x,y)



plt.scatter(my_modl.cluster_centers_[:,1],my_modl.cluster_centers_[:,1],marker="x",s=250,linewidths=5)
plt.show()
    
    