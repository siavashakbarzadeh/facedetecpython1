import os
import cv2
import numpy
from PIL import Image
#vorod be pooshe aks
#IDs.append(ID)
#cv2.imshow("training",faceNp)
#cv2.waitKey(20)
recognizer_algorithm = cv2.createLBPHFaceRecognizer()
dataset_path = 'IMGSTORE'

def getImagesWithID(path):
	imagePaths = [os.path.join(dataset_path,f) for f in os.listdir(dataset_path)]
	faces = []
	IDs = []
	#dastoorate zakhire aksha
	#for imagePath in imagePaths:
		#facePhoto = Image.open(imagePath).convert('L')
		#faceNp = numpy.array(facePhoto,'uint8')
		#ID = int(os.path.split(imagePath)[-1].split('.')[1])
		#faces.append(faceNp)
		#IDs.append(ID)
		#cv2.imshow("training",faceNp)
		#cv2.waitKey(20)
	for imagePath in imagePaths:
		facePhoto = Image.open(imagePath).convert('L')
		faceNp = numpy.array(facePhoto,'uint8')
		ID = int(os.path.split(imagePath)[-1].split('.')[1])
		faces.append(faceNp)
		IDs.append(ID)
		cv2.imshow("training",faceNp)
		cv2.waitKey(20)
	return numpy.array(IDs), faces
#bazgashte araye az aksha
ids,faces = getImagesWithID(dataset_path)		
recognizer_algorithm.train(faces,ids)
#sakhtane file tashkhis dahande
recognizer_algorithm.save('tashkhisdahande/amoozeshi.yml')
cv2.destroyAllWindows()

#getImagesWithID(dataset_path)
