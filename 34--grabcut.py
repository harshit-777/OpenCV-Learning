import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('lena.jpg')
mask = np.zeros(img.shape[:2],np.uint8)

bgd = np.zeros((1,65),np.float64)
fgd = np.zeros((1,65),np.float64)

rect = (180,130,200,400)

cv2.grabCut(img,mask,rect,bgd,fgd,5,cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]
plt.imshow(img)
plt.colorbar()
plt.show()