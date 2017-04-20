import numpy as np
import cv2
import sqlite3


doorbin = cv2.VideoCapture(0)
tashkhischehre = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#doorbin = cv2.VideoCapture(0)------ >khandane doorbin
#tashkhischehre = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')---->tashkhis chehre

#vorood be paygahdade

def insertINTOdatabese(id,name):
	connection = sqlite3.connect("DBSET.db")
	command = "SELECT * FROM RECORD WHERE ID="+ str(id)
	cursor=connection.execute(command)
	ifrecordexist=0
	for row in cursor:
		ifrecordexist=1
	if (ifrecordexist==1):
	    command = "UPDATE RECORD SET ESM="+str(name)+"WHERE ID="+str(id)	
	else:
		command = "INSERT INTO RECORD(ID,ESM) Values("+str(id)+","+str(name)+")"
		connection.execute(command)
		connection.commit()
		connection.close()
#vorood be paygahdade
		
#cv2.imwrite("IMGSTORE/User."+str(id)+"."+str(sampleNum)+".jpg",gray_color[y:y+h,x:x+w])
# cv2.rectangle(img,(x,y),(x+w-10,y+h-10),(132,201,190),3)
#cv2.waitKey(100)

print ("it is compulsory")
id = raw_input('please enter your id*: ')
name = raw_input('please enter your name*: ')
#vorood ebtedaii
insertINTOdatabese(id,name)
sampleNum=0

while (True):
	ret,img = doorbin.read()
	gray_color=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	faces = tashkhischehre.detectMultiScale(gray_color,1.3,3)
	
	for(x,y,w,h) in faces:
            sampleNum=sampleNum+1
            cv2.imwrite("IMGSTORE/User."+str(id)+"."+str(sampleNum)+".jpg",gray_color[y:y+h,x:x+w])
            cv2.rectangle(img,(x,y),(x+w-10,y+h-10),(132,201,190),3)
            cv2.waitKey(100)
            
#gereftane soorat
#cv2.imshow("face",img)
#zamane takhir
#cv2.waitKey(1)
	cv2.imshow("face",img)	
	cv2.waitKey(1)
	if (sampleNum>20):
	    break 
	
doorbin.release()		
cv2.destroyAllWindows()
