import cv2              #openCV module
import imutils           #imutils module


Cam = cv2.VideoCapture(0)      # initializing camera

firstFrame = None

while True:
    _,frame = Cam.read()

    frame = imutils.resize(frame, width=1000)                  #resizing the frame

    grayImage = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)           #converting to grayScale Image

    blurImage = cv2.GaussianBlur(grayImage,(21,21), 0)              # apply blur to reduce noises

    if firstFrame is None:
        firstFrame = blurImage
        continue
    diff = cv2.absdiff(firstFrame , blurImage)                             #difference btw firt image and current imagessss
    
    thresh =cv2.threshold(diff,25,255,cv2.THRESH_BINARY)[1]                         # make it to B/W image
    
    thresh = cv2.dilate(thresh,None,iterations=2)                            # fill the white spaces

    cnts = cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)           # find the border of  moving object
    cnts=imutils.grab_contours(cnts)                                                         # grabing the all contours c = [c1,c2,c3 ...]

    status = "Normal"
     
    for c in cnts:
        if cv2.contourArea(c) <500:        # ignore small objects
            
            continue
        status = "Moving Object detected"

        (x,y,w,h) = cv2.boundingRect(c)
        

        cv2.rectangle(frame , (x,y), (x+w,y+h),(0,0,255),3)         # put  rectangle on the moving object
        
    print(status)
    
    text = "No Motion" if status == "Normal" else "Moving Object Detected"
    color = (0,255,0) if status == "Normal" else (0,0,255)

    cv2.putText(
    frame,
    text,
    (10, 20),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.5,
    color,
    2
    )
          # put text 
        
                    
                    

    cv2.imshow("Camera",frame)           # ouptut

    key = cv2.waitKey(10)
    print(key)

    if  key == 27:
        break

Cam.release()
cv2.destroyAllWindows()
