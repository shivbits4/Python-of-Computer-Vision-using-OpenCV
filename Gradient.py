# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 00:16:02 2020

@author: 91842
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt


dog1 = cv2.imread("Images/dog.10.jpg",0)
dog2 = cv2.imread("Images/dog.14.jpg",0)
dog3 = cv2.imread("Images/dog.16.jpg",0)

def displayImage (img):
    fig = plt.figure(figsize = (12,10))
    ax  = fig.add_subplot(111)
    ax.imshow(img, cmap = 'gray')

# X sobel gradient
# Edge detection in X axis
displayImage(dog2)
sobelx = cv2.Sobel(dog2, cv2.CV_64F, 1, 0, ksize = 5)
displayImage(sobelx)

# Y sobel gradient
# Edge detection in Y axis
displayImage(dog2)
sobely = cv2.Sobel(dog2, cv2.CV_64F, 0, 1, ksize = 5)
displayImage(sobely)

# laplacian gradient
# Edge detection in X and Y axis
displayImage(dog1)
laplacian = cv2.Laplacian(dog1, cv2.CV_64F)
displayImage(laplacian)

 
