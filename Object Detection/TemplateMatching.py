# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 19:11:18 2020

@author: 91842
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

main = cv2.imread('main.jpg')
main = cv2.cvtColor(main,cv2.COLOR_BGR2RGB)

template = cv2.imread('template.jpg')
template = cv2.cvtColor(template,cv2.COLOR_BGR2RGB)

plt.imshow(main)

method = ["cv2.TM_CCOEFF","cv2.TM_CCOEFF_NORMED", "cv2.TM_CCORR","cv2.TM_CCORR_NORMED", "cv2.TM_SQDIFF", "cv2.TM_SQDIFF_NORMED" ]

for m in method:
    image_copy = main.copy()
    method = eval(m)
    
    
    res = cv2.matchTemplate(image_copy, template, method) # res = heatmap
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    
    height, width, channels = template.shape
    
    bottom_right = (top_left[0]+ width, top_left[1]+height)
    
    cv2.rectangle(image_copy, top_left, bottom_right, (255,0,0), 10)
    
    # Plot the image
    
    plt.subplot(121)
    plt.title("HEATMAP")
    plt.imshow(res)
    
    plt.subplot(122)
    plt.title("Detection of Template")
    plt.imshow(image_copy)
    plt.suptitle(m)
    
    plt.show()
    print('\n')