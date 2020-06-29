import cv2
import datetime
cap = cv2.VideoCapture(0)


print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#cap.set(3,1208)  #here 3 is assosiate number of width
#cap.set(4,720)   #here 4 is assosiate number of height

#print(cap.get(3))
#print(cap.get(4))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
    	#gray = bcv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    	font = cv2.FONT_HERSHEY_SIMPLEX
    	text = 'Width:' + str(cap.get(3)) + 'Height:' + str(cap.get(4))
    	date = str(datetime.datetime.now())
    	frame=cv2.putText(frame,date,(10,50),font,0.8,(0,0,255),2,cv2.LINE_AA)
    	cv2.imshow('frame', frame)
    	if cv2.waitKey(1) & 0xFF == ord('q'):
    		break
    else:
        break

cap.release()
cv2.destroyAllWindows()