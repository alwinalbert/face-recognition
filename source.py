import cv2
face_cap = cv2.CascadeClassifier("C:/Users/alwin/AppData/Local/Programs/Python/Python312/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
video_play = cv2.VideoCapture(0)
while True:
    ret , video_data=video_play.read()
    col = cv2.cvtColor(video_data,cv2.COLOR_BGR2GRAY)
    face = face_cap.detectMultiScale(col,
                                     scaleFactor=1.1,
                                     minNeighbors=5,
                                     #maxSize=(30,30),{if needed},
                                     flags=cv2.CASCADE_SCALE_IMAGE)
    for (x,y,w,h) in face:
        cv2.rectangle(video_data,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("live",video_data)
    if cv2.waitKey(10) == ord("a"):
        break
video_play.release()
