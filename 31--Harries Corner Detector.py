#Harries Corner Detector--
import numpy as np 
import cv2
img = cv2.imread('chessboard.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
dist = cv2.cornerHarris(gray,2,3,0.04) #argument block size,ksizee =aperature para,k=harries detectore
dist = cv2.dilate(dist,None)

img[dist>0.01* dist.max()] = [0,0,255]
cv2.imshow('dist',img)

cv2.waitKey(0)
cv2.destroyAllWindows()