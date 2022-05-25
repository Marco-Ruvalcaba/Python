import cv2
import sys


faceClassif = cv2.CascadeClassifier(sys.path[0] + '\haarcascade_frontalface_default.xml')

image = cv2.imread( sys.path[0] + '\Imagen_Ejemplo.jpg' , 1)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


faces = faceClassif.detectMultiScale(gray,
                                     scaleFactor=1.1,
                                     minNeighbors=5,
                                     minSize=(30, 30),
                                     maxSize=(280, 280) )
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0,255,0), 2 )

cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

