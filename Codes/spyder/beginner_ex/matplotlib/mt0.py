# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd

from matplotlib import pyplot as plt

plt.style.use('classic')

df=pd.DataFrame(np.array(np.random.randint(0,20,30)).reshape(6,5))


plt.plot(df)

x=[1,5,6,9,10,11]
y=[2,6,7,10,8,12]
plt.plot(x)

plt.plot(x,y)

x1=np.linspace(0,10)
y1=np.sin(x1)
plt.style.use('ggplot')

plt.plot(x1,y1)

#تعملهم كمبيل هما ال 3 مع بعض علشان يكتب الليبل 
plt.ylabel('Time')
plt.xlabel('work')
plt.plot(x,y)


#طريقه اخرى ل كتابة الليبل هترن ال4 مع بعض 
ax=plt.axes()
ax.set_xlabel('time')
ax.set_ylabel('work')
plt.plot(x,y)
#تحديد الاماكن اللى بيتقابل فيها اكس و واى
plt.plot(x,y,marker='o')





