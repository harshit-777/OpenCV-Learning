import cv2
import numpy as np
img = cv2.imread('messi5.jpg')
img2 = cv2.imread('opencv-logo.png')

#print(img.shape)
#print(img.size)
#print(img.dtype)

#b,g,r = cv2.split(img)
#img = cv2.merge((b,g,r))


#ball = img[280:340,330:390] #ball copy to other place
#img[273:333,100:160] = ball


#add method of opencv 
img = cv2.resize(img,(512,512))
img2 = cv2.resize(img2,(512,512))

# add weight  input image name 0.8 is 80% of first 0.2 is 20% of second and 0 is gamma value which is scalar
dest = cv2.addWeighted(img,0.8,img2,0.2,0)

#dest = cv2.add(img,img2)


 
cv2.imshow('image',dest)
cv2.waitKey(0)
cv2.destroyAllWindows() 





#ROI region of intrest