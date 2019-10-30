# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 01:26:18 2019

@author: Ahmed Ali
"""

import numpy as np
import pandas as pd

#                             String 

data=['ahmed','ali','Sheref','khaled']

print(pd.Series(data).str.len())


print(pd.Series(data).str.startswith('p'))


print(pd.Series(data).str.startswith('a'))

print(pd.Series(data).str.endswith('d'))

# when he dont find string return -1

print(pd.Series(data).str.find('ah'))

print(pd.Series(data).str.find('l'))

# ال جاست ده شبه المحازاه من اليمين والمحازاه من الشمال بيظبط النص
# هنديله رقم وليككن 20 مثلا معناعها ان الكلمه والمسافات عددهم لا يتجاوز20
print(pd.Series(data).str.ljust(20))# من اليسار

print(pd.Series(data).str.rjust(20))# من اليمين



print(pd.Series(data).str.center(20))#توسيط 


print(pd.Series(data).str.zfill(10))#تكملة الفراغات اصفار تنفع مع الارقام


print(pd.Series(data).str.islower())#الكلمة كلها سمول ولا 

print(pd.Series(data).str.isupper())#الكلمة كلها كبتل ولا 

# يعنى هل اول حرف ف الكلمه كبتل والباقى سمول ولا 
print(pd.Series(data).str.istitle())


print(pd.Series(data).str.isalpha()) #كلها حروف ولا

print(pd.Series(data).str.isdigit())#فيها ارقام ولا

print(pd.Series(data).str.isalnum())#مفيهاش ولا فراغ ولا

print(pd.Series(data).str.isdecimal())# هل تحتوى عل ارقام ولا 

print(pd.Series(data).str.upper())#الكل كبيتل 


print(pd.Series(data).str.capitalize())# بيخليهالك تيتل يعنى الاول كبتل بس

#خلى الكبتل سمول والسمول كبتل
print(pd.Series(data).str.swapcase())
