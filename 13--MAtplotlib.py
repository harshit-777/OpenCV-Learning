import cv2
import matplotlib.pyplot as plt
#matplot lib read image in RBG formate and cv read in BGR we need to convert image 

img = cv2.imread('lena.jpg')
cv2.imshow('image',img)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

plt.imshow(img)
#plt.xticks([])   to hide ticks we use the [] in plt.xticks
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()