# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 01:58:07 2019

@author: Ahmed Ali
"""

import numpy as np
import pandas as pd


  #         Date   التواريخ
  
  
s="4th of July, 2018"

x=pd.to_datetime(s) #حولها من استرنج ل تاريخ 
 
print(x) # 2018-07-04 00:00:00

y= x - pd.to_timedelta(np.arange(20),'D')

print(y)
  
  
  
  
   # ابق اسمع باقى المحاضره علشان اتبضنت 