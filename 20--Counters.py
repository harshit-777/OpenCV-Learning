#c0ntours are used for shape analysis 
import numpy as np
import cv2


img = cv2.imread('opencv-logo.png')
img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


ret ,thresh = cv2.threshold(img1,127,255,0)
contours ,hirechy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
print("NO of Countours" + str(len(contours)))
print(contours[0])

cv2.drawContours(img,contours,-1,(0,255,0),3)


cv2.imshow('Image',img)
cv2.imshow('Image GRAY',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()