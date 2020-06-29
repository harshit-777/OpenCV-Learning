import cv2
import numpy as np
#mask binary image in which operation is performed
img = np.zeros((512,512,3),np.uint8)
img = cv2.rectangle(img,(200,0),(300,100),(255,255,255),-1)
img2 = cv2.imread("gradient.png")
img = cv2.resize(img,(512,512))
img2 = cv2.resize(img2,(512,512))
#Method 
#bitAnd = cv2.bitwise_and(img,img2)
#bitOR = cv2.bitwise_or(img,img2)
#bitXOR = cv2.bitwise_xor(img,img2)
bitNOT = cv2.bitwise_not(img,img2)



cv2.imshow("img",img)
cv2.imshow("img2",img2)
#cv2.imshow("bitAnd",bitAnd)
#cv2.imshow('bitOR',bitOR)
#cv2.imshow('bitXOR',bitXOR)
cv2.imshow('bitNOT',bitNOT)




cv2.waitKey(0)
cv2.destroyAllWindows()

