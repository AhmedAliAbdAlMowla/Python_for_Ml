# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 18:28:44 2019

@author: Ahmed Ali
"""

import numpy as np


num=[1,3,9,7]
print(type(num))

nv=np.array(num)
print(type(nv))

mat=[[1,2],[9,6]]
print(type(mat))

matp=np.array(mat)
print(type(matp))


print(len(mat))
print(len(matp))

#   defrant betwen size and lenth 
print(matp.size)

lst=list(range(0,10))

print(lst)
mtx=np.arange(0,10)
mtx2=np.arange(0,15,3)

print(mtx)
print(mtx2)

n1,n2=1,9

# creat matrex  like range put defrint in consept row and col
n1,n2=np.mgrid[2:5,4:7]

# vector of zeros
z=np.zeros(7)
# vector of ones
one=np.ones(8)

# matrex of zeros
zz=np.zeros((3,4))

# matrex of ones
ones=np.ones((3,4))

# matrex of num 
fl=np.full((6,7),34)

# فيكتور رنج من 0 ل 15 وبيزود ب ال 0.1
mtx2=np.arange(0,15,0.1)
mtx2
# بيرجع فيكتور وانا
# بديله انا عايز كام رقم وخلاص مليش دعوة ب الستيب
mtx3=np.linspace(0,15,30)

# فيه نوعين للراندم
# اول نوع القيم من 0 ل 1 وده(youne form distrpiotion)  
# النوع الثانى جوسين دستربيوشن وده من  -1  ل 1 

#اول نوع 

# new vector ranam valiue betwen 0,1 -> (youne form distrpiotion)
randvec=np.random.rand(5)
# new matrex 5*4 ranam valiue betwen 0,1 -> (youne form distrpiotion)
randmtx=np.random.rand(5,4)

randmtx*=10

# ثانى نوع 
# لاحظ التغير ف الفنكشن  حرف ال  ان 
jusin=np.random.randn(5,4)

mtx4=np.random.randint(0,50,20)
print(mtx4)



