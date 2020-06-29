#How to read image in opencv--
import cv2
import cv2
path = "/home/ind/Desktop/opencv-master/lena.jpg"
img = cv2.imread(path,0)


#Esc(27) key is press and s(ord('s')) for save
cv2.imshow("newpic",img)
k = cv2.waitKey(0)
if k == 27: #to cancal with esc key
	cv2.destroyAllWindows()
elif k == ord('s'):
	cv2.imwrite('lena_copy.png',img)
	cv2.destroyAllWindows()