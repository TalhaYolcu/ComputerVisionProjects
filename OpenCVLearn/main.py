import cv2
import numpy as np

#show an image
#img=cv2.imread("Resources/lena.png")
#cv2.imshow("Output",img)
#cv2.waitKey(0)


#show video capture
#cap = cv2.VideoCapture("Resources/test_video.mp4")
#while True:
    #success,img=cap.read()
    #cv2.imshow("Video",img)
    #if cv2.waitKey(1) & 0xFF == ord('q'):
        #break


#show webcam
#cap = cv2.VideoCapture("0")
#cap.set(3,640)
#cap.set(4,480)
#cap.set(10,100)

#while True:
    #success,img=cap.read()
    #cv2.imshow("Video",img)
    #if cv2.waitKey(1) & 0xFF == ord('q'):
        #break



img=cv2.imread("Resources/lena.png")

#kernel matrix
kernel=np.ones((5,5),np.uint8)

#Gives a gray image
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Give a blur image
imgBlur=cv2.GaussianBlur(imgGray,(7,7),0)

#edge detector
imgCanny = cv2.Canny(img,150,200)

#dialation-increase thickness of line
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)

#opposite of dilation
imgEroded=cv2.erode(imgDialation,kernel,iterations=1)

cv2.imshow("Gray image",imgGray)
cv2.imshow("Blur image",imgBlur)
cv2.imshow("Canny image",imgCanny)
cv2.imshow("Dilation image",imgDialation)
cv2.imshow("Eroded image",imgEroded)

cv2.waitKey(0)

