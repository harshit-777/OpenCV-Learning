import  cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('sudoku.png',cv2.IMREAD_GRAYSCALE)

lap = cv2.Laplacian(img, cv2.CV_64F,ksize=3)
lap = np.uint8(np.abs(lap))

sobelx = cv2.Sobel(img,cv2.CV_64F,1,0)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=1)
sobelX = np.uint8(np.abs(sobelx))
sobelY = np.uint8(np.abs(sobely))

sobelNcom = cv2.bitwise_or(sobelX,sobelY)


title =  ['image','LAP','SobelX','SobelY','SobelCOM']
images = [img,lap,sobelX,sobelY,sobelNcom]


for i in range(5):
	plt.subplot(3,2,i+1)
	plt.imshow(images[i])
	plt.title(title[i])


plt.show()	