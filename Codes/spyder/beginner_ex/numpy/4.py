# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 00:15:11 2019

@author: Ahmed Ali
"""
import numpy as np

lis=[1,6,8,9,7]

arr2=np.array(lis)
arr=np.arange(0,14,2)


print(arr)

print(arr[1])
#  suparray  (^_^)
print(arr[1:6])
# ex1
new_arr=np.array(arr[1:4])
# ex2
new_arr2=np.array(arr[4:])
# ex3





#  ملحوظه مهمه عند كتابة الاراى فى هذا الشكل ف ان الاراى 
#لا تأخز نسخه من الاراى اللى بتقطع منها جزء 
#ولاكن ده بيبقى ريفرنس
# يعنى اى تغير بيطرأ عل الاراى المعموله
# بيسمع ف الام وده علشان حاجه ف الامج بروسيسنج
new_arr4=arr[:5]
new_arr4[:]=60






# importatn value prod casting

# we can use .copy()
new_arr3=arr[:6].copy()
new_arr3[:3]=60
print(new_arr3)





