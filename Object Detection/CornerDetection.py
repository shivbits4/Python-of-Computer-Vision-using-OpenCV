# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 20:11:26 2020

@author: 91842
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

main = cv2.imread("main.jpg")
main = cv2.cvtColor(main, cv2.COLOR_BGR2RGB)

# 
gray_main = cv2.cvtColor(main, cv2.COLOR_RGB2GRAY)

plt.imshow(gray_main, cmap ='gray')

# Apply Harris Corner Detection
# For Harris corner detection we need image to be have float value

gray_main = np.float32(gray_main)

dst = cv2.cornerHarris( src = gray_main, blockSize = 2, ksize = 5, k = 0.04)
plt.imshow(dst, cmap = 'gray')

dst = cv2.dilate(dst, None)
plt.imshow(dst, cmap = 'gray')

main[dst > 0.01*dst.max()] = [255,0,0]
plt.imshow(main)

# Shi Tomasi Detection
main = cv2.imread("main.jpg")
main = cv2.cvtColor(main, cv2.COLOR_BGR2RGB)

# 
gray_main = cv2.cvtColor(main, cv2.COLOR_RGB2GRAY)

corners = cv2.goodFeaturesToTrack(gray_main, 90 ,0.01,10)

corners = np.int0(corners)

for i in corners:
    x,y = i.ravel()
    cv2.circle(main, (x,y), 3, (255,0,0), -1)


plt.imshow(main)