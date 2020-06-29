#Templet finding in larger image
import cv2
import numpy as np
img = cv2.imread('messi5.jpg')
img2 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
template = cv2.imread('messi55.jpg',0)
w,h = template.shape[::-1]

res = cv2.matchTemplate(img2,template,cv2.TM_CCOEFF_NORMED)
print(res)
thres = 0.92
loc = np.where(res >= thres)
print(loc)

for pt in zip(*loc[::-1]):
	cv2.rectangle(img,pt,(pt[0]+w,pt[1]+h),(0,0,255),2)

cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

