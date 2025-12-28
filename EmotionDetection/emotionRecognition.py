from facial_emotion_recognition import EmotionRecognition  # import module
import cv2

er = EmotionRecognition(device='cpu')              # initialization

Camera = cv2.VideoCapture(0)                          # capaturing frame

while True:
    _ , frame = Camera.read()                                

    frame = er.recognise_emotion(frame, return_type='BGR')                   #Recogition of emotions 
    cv2.imshow("EMOTION DETECTION",frame)

    key = cv2.waitKey(1)
    if key == 27:
        break                                             # Esc to terminate
Camera.release()
cv2.destroyAllWindows()


