
# coding: utf-8

# In[3]:


import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('demo.jpg', 1)
blue, green, red = cv.split(img)
img2 = cv.merge([red,green,blue])
plt.imshow(img2, cmap = 'gray', interpolation = 'bicubic')
#plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()

