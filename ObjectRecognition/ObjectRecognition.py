import cv2
import numpy as np
import imutils
import time


prototxt = "./MobileNetSSD_deploy.prototxt.txt"
model = "./MobileNetSSD_deploy.caffemodel"

confThresh = 0.3

CLASSES = ["background","aeroplane","bicycle","bird",
           "boat","bottle","bus","car","cat","chair",
           "cow","diningtable","dog","horse","motorbike",
           "person","pottedplant","sheep","sofa","train",
           "tvmonitor","mobile"
           ]
COLORS = np.random.uniform(0,255,size=(len(CLASSES),3))

print("Model Loading..")
net = cv2.dnn.readNetFromCaffe(prototxt,model)
print("Model Loaded...")

Camera = cv2.VideoCapture(0)
time.sleep(2.0)

while True:
    success , frame = Camera.read()
    if not success:
        break
    frame = imutils.resize(frame,width=1000)
    (h,w) = frame.shape[0:2]

    imgResizeForBlob = cv2.resize(frame,(300,300))

    blob = cv2.dnn.blobFromImage(imgResizeForBlob,(1/127.5),(300,300),127.5)

    net.setInput(blob)

    detections = net.forward()

    detShape = detections.shape[2]

    for i in np.arange (0,detShape):
        confidence = detections[0,0,i,2]
        if confidence > confThresh:
            Id = int(detections[0,0,i,1])
            box = detections[0,0,i,3:7]*np.array([w,h,w,h])
            (xStart,yStart,xEnd,yEnd) = box.astype("int")

            label = "{} : {:.2f}%".format(CLASSES[Id],confidence*100)

            cv2.rectangle(frame,
                          (xStart,yStart),
                          (xEnd,yEnd),
                          COLORS[Id],
                          2
                          )

            if yStart-15 > 15:
                y = yStart - 15
            else:
                y = yStart + 15

            cv2.putText(frame,label,(xStart,y),
                        cv2.FONT_HERSHEY_SIMPLEX,0.5,
                        COLORS[Id],2)
            
    cv2.imshow("frame",frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

Camera.release()
cv2.destroyAllWindows()




            

