import cv2
import numpy as np

img = cv2.imread("Resources/lambo.png")
#find size of image

print(img.shape)
#(462, 623, 3)
#height,width,bgr channel number

#resize image
imgResize=cv2.resize(img,(300,200))
print(imgResize.shape)

#crop an image
imgCropeed=img[0:200,200:500]




cv2.imshow("Image",img)
cv2.imshow("Image Resized",imgResize)
cv2.imshow("Cropped Image",imgCropeed)
cv2.waitKey(0)