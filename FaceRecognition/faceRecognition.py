import cv2,os
import numpy as np                              # Import numpy module

algorithm = "haarcascade_frontalface_default.xml"       # Load Haar Cascade file

datasets = "dataSets"                              # Dataset folder
(width,height) = (130,100)                     # (w.h) for dataset image

images = []                                       # initially images,labels are Lists
labels = []
names = {}
id =0

print("Training Model.....Please Wait")


for (dirs,folder,file) in os.walk(datasets):           # Walk through the folder
    for fname in folder:
        names[id] = fname
        sub_path = os.path.join(datasets,fname)

        for filename in os.listdir(sub_path):
            imagepath = os.path.join(sub_path,filename)
            image = cv2.imread(imagepath,0)
            if image is None:
                continue
            images.append(image)
            labels.append(id)

        id+=1
images = np.array(images)                 # Array conversion
labels = np.array(labels)


model = cv2.face.FisherFaceRecognizer_create()         # Recognizer Model Creation
model.train(images,labels)                      # Model training 

print("Model Trained Successfully...")
    
haarCascade = cv2.CascadeClassifier(algorithm)       # Load Haar Cascade algorithm

Camera = cv2.VideoCapture(0)
cnt =0

while True:
    success , frame = Camera.read()           #Check frame
    if not success:
        break

    grayIm = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)         # Grayscale Image

    faces = haarCascade.detectMultiScale(grayIm,1.3,5)        
    for (x,y,w,h) in faces:
        face = grayIm[y:y+h,x:x+w]                  # crop face region
        face_resize = cv2.resize(face,(width,height))


        prediction = model.predict(face_resize)          # Model Predicting
        label , confidence = prediction

        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)      

        if confidence < 800:
            name = names[label]

            cv2.putText(frame,f"{name} - {int(confidence)}",(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,255,255),2)
            print(name)
            cnt=0
        
        else:
            cnt+=1
            cv2.putText(frame,"Unknown",(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255),2)
            print("Unknown Person")
            if cnt >100:
                cv2.imwrite("unknownVisitor.jpg",frame)
                cnt =0
                
    cv2.imshow("Frame",frame)         # Display Frame


    if cv2.waitKey(10) == 27:        # Termination
        break


Camera.release()
cv2.destroyAllWindows()
    
    





        
