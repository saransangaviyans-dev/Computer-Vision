import cv2
import imutils

hsvLower = (160,61,135)                 #hsv values for the Object
hsvUpper = (179,255,255)

Camera = cv2.VideoCapture(0)                  #initializing Camera

while True:

    Success,frame = Camera.read()
    if not Success:                            
        break
    
    frame = imutils.resize(frame, width=1000)             #resize
    blur = cv2.GaussianBlur(frame,(11,11),0)                #blur

    hsv = cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)           # hsv Colour Convertion of frame

    mask = cv2.inRange(hsv,hsvLower,hsvUpper)              #mask 
    mask = cv2.erode(mask, None, iterations=2)               #erosion and dilation
    mask = cv2.dilate(mask,None,iterations=2) 
                                                                              #Contours
    cnts = cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]  
    center = None

    if len(cnts)>0:
        c = max(cnts,key=cv2.contourArea)
        ((x,y),radius) = cv2.minEnclosingCircle(c)
        M= cv2.moments(c)
        if M["m00"] != 0:
            center = (int(M["m10"]/M["m00"]),int(M["m01"]/M["m00"]))        #center
        else:
            center= None
        if radius > 10:
            cv2.circle(frame,(int(x),int(y)),int(radius),(0,255,255),2)          #Circle 
            cv2.circle(frame,center,5,(0,0,255),-1)                            #center dot
            #print(center,radius) 

            if radius >250:                                             #Object Position
                 print("Stop")
            else:
                if center[0] < 250:                           
                    print("Right")
                elif center[0]> 750:
                    print("Left")
                elif radius < 250:
                    print("Front")
                else:
                    print("stop")
 

    cv2.imshow("Frame",frame)

    key = cv2.waitKey(1)                                             #termination
    if key == 27:
        break



Camera.release()
cv2.destroyAllWindows()
        



            

            
