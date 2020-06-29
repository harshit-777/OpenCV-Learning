import  numpy as np
import cv2 
cap = cv2.VideoCapture('vtest.avi')
#fgbg = cv2.createBackgroundSubtractorMOG2()
fgbg = cv2.createBackgroundSubtractorKNN()


while True:
	ret,frame = cap.read()
	if frame is None:
		break

	fgmask = fgbg.apply(frame)
	

	cv2.imshow('Frmae',frame)
	cv2.imshow('FG MASK',fgmask)

	key = cv2.waitKey(30)
	if key == 'q' or key == 27:
		break
cap.release()
cv2.destroyAllWindows()		

		