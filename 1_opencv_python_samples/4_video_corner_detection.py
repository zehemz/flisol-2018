
# coding: utf-8

# In[3]:


import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)
while(True):
    ret, img = cap.read()
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray = np.float32(gray)
    dst = cv.cornerHarris(gray,2,3,0.04)
    dst = cv.dilate(dst,None)
    # Threshold for an optimal value, it may vary depending on the image.
    img[dst>0.0001*dst.max()]=[0,0,255] # Si se varia el entero x el maximo
    cv.imshow('frame',img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()

