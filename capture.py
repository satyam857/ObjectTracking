import cv2
import numpy as np

camera_port = 0
camera = cv2.VideoCapture(camera_port)

while(True):

    # Take each frame
    status, frame = camera.read()
    if(not status):
        print("Check Your Camera")
        break
    
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of Yellow color in HSV
    lower_blue = np.array([20, 100, 100])
    upper_blue = np.array([30, 255, 255])

    # Threshold the HSV image to get only Yellow colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)
    
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    #cv2.imshow('res',res)
    #cv2.imshow('hvc',hsv)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

del(camera)
cv2.destroyAllWindows()

