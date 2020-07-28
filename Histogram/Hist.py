# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 18:10:49 2020

@author: 91842
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt

dog1 = cv2.imread("Images/dog.10.jpg")

def displayImage (img):
    fig = plt.figure(figsize = (12,10))
    ax  = fig.add_subplot(111)
    ax.imshow(img, cmap = 'gray')

color = ('r', 'g', 'b')

for i,col in enumerate(color):
    hist = cv2.calcHist([dog1], [i] ,None, [256], [0,256])
    plt.plot(hist, color = col)

plt.title("Histogram")


# Masking and then showing histogram of masked area
show_dog = cv2.cvtColor(dog1, cv2.COLOR_BGR2RGB)
show_dog.shape

mask = np.zeros(show_dog.shape[:2], np.uint8)

mask[100:200, 100:200] = 255
plt.imshow(mask, cmap = 'gray');

masked_dog = cv2.bitwise_and(dog1, dog1, mask = mask)
plt.imshow(masked_dog)

masked_hist = cv2.calcHist([dog1], [1], mask, [256],[0,256])
plt.plot(masked_hist)

# Using Histogram Equalization to increase contrast
dog1 = cv2.imread("Images/dog.10.jpg", 0)
plt.imshow(dog1,cmap = 'gray')
    
eq_image = cv2.equalizeHist(dog1)
plt.imshow(eq_image, cmap = 'gray')
