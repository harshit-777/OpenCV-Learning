import cv2
import matplotlib.pyplot as plt
import numpy as np 

def nothing(x):
	print(x)


img = cv2.imread('messi5.jpg',0)
cv2.namedWindow('image')

cv2.createTrackbar("B",'image',0,255,nothing)
cv2.createTrackbar("G",'image',0,255,nothing)
canny = cv2.Canny(img,cv2.getTrackbarPos('B','image'),cv2.getTrackbarPos('G','image'))


title = ['image','canny']
images = [img,canny]

for i in range(2):
	plt.subplot(1,2,i+1)
	plt.imshow(images[i])
	plt.title(title[i])


plt.show()	




# canny edge detectore is an edge detection operatore that used a multi stage alogorithm ti detect a wide range of edges in images.
# the canny used---
# Noise reduction Gradient  Calculation Non maximum Double threshold Edge Tracking Hyteresics