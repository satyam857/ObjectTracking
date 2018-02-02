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

    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None

    #check there is any Yello Object 
    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))    
        cv2.circle(frame, (int(x), int(y)), int(radius),(0, 255, 255), 2)
        cv2.circle(frame, center, 5, (0, 0, 255), -1)
 
    # show the frame to our screen
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
        
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

del(camera)
cv2.destroyAllWindows()

