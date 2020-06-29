import cv2
import numpy as np

#img = cv2.imread('lena_copy.png',1)
img = np.zeros([512,512,3],np.uint8) #py we can make black image here in list 512 height and next is width

img = cv2.line(img,(0,0),(255,255),(255,0,0),6)   #here 0,0 is the starting points and  second is ending after that (B,G,R) formate atter that thickness og the line is given 
img = cv2.arrowedLine(img,(0,255),(255,255),(0,255,0),6)
font = cv2.FONT_HERSHEY_DUPLEX
img = cv2.putText(img,"Beauty",(10,500),font,4,(255,255,0),10,cv2.LINE_AA)
img = cv2.circle(img,(447,63),63,(0,255,0),10)
img = cv2.rectangle(img,(384,0),(510,128),(0,0,255),7)
cv2.imshow('image',img)



cv2.waitKey(0)
cv2.destroyAllWindows()