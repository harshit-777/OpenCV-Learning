import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('opencv-logo.png')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

kernel = np.ones((5,5),np.float32)/25
dest = cv2.filter2D(img,-1,kernel)
#BLUR METHOD
blur = cv2.blur(img,(5,5))
#Gussian filter diff weight in x and y kernel in centre have high weight ...side have small weight
Guss = cv2.GaussianBlur(img,(5,5),0) 
median = cv2.medianBlur(img, 5)
bilateralFilter = cv2.bilateralFilter(img, 9, 75, 75)


title = ['image','2D_COnv','Blur','Gussian','median','bilateral']
image = [img,dest,blur,Guss,median,bilateralFilter]

for i in range(6):
	plt.subplot(2,3,i+1)
	plt.imshow(image[i])
	plt.title(title[i])


plt.show()

#Homogeneous filter is yhe most simple filter each oyput pixel is the mean of its kernel neighbours
#Kernel is convolution matrix or mask, it is used for blurring sharping embossing egde detection and more
#LPF -low pass flter is remove noice
#HPF- remove edges in images
#MEdian filter is  something that replaces each pixel with median of its neighbour pixel