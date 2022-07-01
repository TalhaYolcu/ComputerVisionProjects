import cv2
import numpy as np

img = cv2.imread("Resources/cards.jpg")

cv2.imshow("Image",img)

#define a cards normal width and height
width,height=250,350

#give edges of the spesific card
pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]])

#set the normal edge coordination of the card
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

#create matrix with points and perspective
matrix = cv2.getPerspectiveTransform(pts1,pts2)

#create output image with given matrix
imgOutput=cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Output Image",imgOutput)
cv2.waitKey(0)