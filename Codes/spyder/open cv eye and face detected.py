# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 17:05:05 2019

@author: Ahmed Ali
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 16:47:03 2019

@author: Ahmed Ali
"""


import cv2
import theano as th
#import tensorflow as tf
#import keras as ks
import numpy as np
import pandas as pd
import sklearn as sk
import matplotlib as mp


face_cascade = cv2.CascadeClassifier('C:\\ProgramData\\Anaconda3\\pkgs\\libopencv-3.4.2-h20b85fd_0\\Library\etc\\haarcascades\\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('C:\\ProgramData\\Anaconda3\\pkgs\\libopencv-3.4.2-h20b85fd_0\\Library\\etc\\haarcascades\\haarcascade_eye.xml')


img=cv2.imread('F:\\as.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

        
        
cv2.imshow('Image',img)
#cv2.imwrite('E:\qt.png',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
