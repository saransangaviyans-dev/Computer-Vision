import cv2,os         # Import Modules

algorithm = "haarcascade_frontalface_default.xml"
datasets = "datasets"
sub_path = "steve"

path = os.path.join(datasets,sub_path)
if not os.path.isdir(path):                   # If folder does not exist, create it
    os.mkdir(path)

(width,height) = (130,100)
cascade = cv2.CascadeClassifier(algorithm)         # Load haar Alogorithm

if cascade.empty():
    print("ERROR: Haar Cascade not loaded")
    exit()

Camera = cv2.VideoCapture(0)                   # Camera initialization

count = 1
while count < 51:
    (_,frame) = Camera.read()
    grayIm = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)          # Grayscale Image

    faces = cascade.detectMultiScale( grayIm , 1.3 , 4 )
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        face = grayIm[y:y+h , x:x+w]                                    # Crop only Face in frame
        face_resize = cv2.resize(face,(width,height))                # Resize
        cv2.imwrite("%s/%s.png" %(path,count),face_resize)                  # Write to the Folder  
        print(count)
        count+=1

    cv2.imshow("frame",frame)
    key = cv2.waitKey(1)                                      # Termination
    if key ==  27:
        break


Camera.release()
cv2.destroyAllWindows()
