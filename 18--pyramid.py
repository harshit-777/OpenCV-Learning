import cv2


img = cv2.imread('lena.jpg')

layer = img.copy()
gp = [layer]

for i in range(6):
	layer = cv2.pyrDown(layer)
	gp.append(layer)
	#cv2.imshow(str(i),layer)

layer = gp[5]
cv2.imshow("Upper level of GP",layer)
lp= [layer]
for i in range(5,0,-1):
	gaussian = cv2.pyrUp(gp[i])
	lapa = cv2.subtract(gp[i-1],gaussian)
	cv2.imshow(str(i),lapa)



cv2.imshow('Original',img)
cv2.waitKey(0)
cv2.destroyAllWindows()