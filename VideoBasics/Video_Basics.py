# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 17:53:04 2020

@author: 91842
"""

import cv2

# Reading frames from Webcam
cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
geight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))



while True:
    
    ret, frame = cap.read();
    
    cv2.imshow('frame', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()

# Reading existing video file
 
cap = cv2.VideoCapture('001_0.mpg')

if cap.isOpened() == False:
    print('File not found')

frames = []



while cap.isOpened():
    
    ret ,frame = cap.read()
    
    
    if ret ==True:
        
        frames.append(frame)
        cv2.imshow('frame', frame)
        
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    
    else:
         break

cv2.imshow('frame', frames[12])

cap.release()
cv2.destroyAllWindows()
        
   
