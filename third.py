import cv2
import sqlite3
import pickle
import numpy as nmp

faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
tashkhischeshm = cv2.CascadeClassifier('haarcascade_eye.xml')

doorbin = cv2.VideoCapture(0)

rec = cv2.createLBPHFaceRecognizer()
rec.load("tashkhisdahande\\amoozeshi.yml")

def readFromDatabase(id):
	connection = sqlite3.connect("DBSET.db")
	command = "SELECT * FROM RECORD WHERE ID="+str(id)
	cursor = connection.execute(command)
	profile=None
	for row in cursor:
		profile=row
	connection.close()	
	return profile

id = 0
font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL,2,1,0,2)
while (True):
	ret,img = doorbin.read()
	gray_color=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	faces = faceDetect.detectMultiScale(gray_color,1.3,2)
	for(x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,110),2)

		id,conf=rec.predict(gray_color[y:y+h,x:x+w])
		profile=readFromDatabase(id)
		if profile!=None:
			cv2.cv.PutText(cv2.cv.fromarray(img),str(profile[1])+" "+str(conf),(x,x+h-10),font,255)
	cv2.imshow("face",img)	
	eye_gray = gray_color[y:y+h, x:x+w]
	eye_color = img[y:y+h, x:x+w]
	eyes = tashkhischeshm.detectMultiScale(eye_gray)
	for (ex,ey,ew,eh) in eyes:
		cv2.rectangle(eye_color, (ex,ey), (ex+ew,ey+eh),(0,255,0),2)
	if(cv2.waitKey(1)) == ord('q'):
		break
doorbin.release()		
cv2.destroyAllWindows()
