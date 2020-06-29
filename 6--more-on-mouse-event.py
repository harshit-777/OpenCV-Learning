import numpy as np
import cv2


def click_event(events,x,y,flags,param):    #all parametes take such argument its in general
        if events == cv2.EVENT_LBUTTONDOWN:
        	cv2.circle(img,(x,y),3,(0,0,255),-1)
            points.append(x,y)
            if len(points) >= 2:
                cv2.line(img,points[-1],poinii]
            cv2.imshow('image',img)

    	
img = cv2.imread('lena.jpg',1)   #define the black image
cv2.imshow('image',img)
points = []
cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
