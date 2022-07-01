import cv2
import numpy as np

#draw shape and text on image

#create matrix filled with 0s
#image will be full black

img = np.zeros((512,512,3),np.uint8)

#color it to blue
#bgr
#img[:]=255,0,0

#color a part of it to green
#img[200:300,100:300]=0,255,0

#draw a line from origin to opposite corner
#source image,start point,end point,color,thickness
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)

#draw a rectangle with fill
cv2.rectangle(img,(0,0),(250,350),(0,0,255),cv2.FILLED)

#draw a circle
cv2.circle(img,(400,50),30,(255,255,0),5)

#put a text
cv2.putText(img," OPENCV ",(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),1)


cv2.imshow("Image",img)
cv2.waitKey(0)
