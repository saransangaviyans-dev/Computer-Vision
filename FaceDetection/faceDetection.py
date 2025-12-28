import cv2

Algorithm = "haarcascade_frontalface_default.xml"                     

haar_Cascade = cv2.CascadeClassifier(Algorithm)                          # loading Allgorithm in Variable

cam = cv2.VideoCapture(0)                                               # Capturing frame

while True:

    _,image = cam.read()

    GrayImage = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)                                   #Grayscale image Conversion

    face = haar_Cascade.detectMultiScale(GrayImage,1.3, 4)                                          #Detecting faces

    for (x,y,w,h) in face:
        cv2.rectangle(image,(x,y),(x+w ,y+h),(0,255,0),2)                                      #Drawing rectangles
    cv2.imshow("FaceDection",image)                                        #showing frame

    key = cv2.waitKey(10)
    if key == 27:
        break                                    # Esc to terminate
    print(key)

cam.release()

cv2.destroyAllWindows()
    

    
