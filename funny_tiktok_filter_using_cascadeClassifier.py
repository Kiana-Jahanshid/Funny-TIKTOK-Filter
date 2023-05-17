import cv2 


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 50)
face_detector = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml") 

pic = cv2.imread('input/4.png',-1)
pic = cv2.resize(pic , (700 , 750))

while True :   
      
    cv2.imshow(" Background " , pic)   
    x , frame = cap.read()
    faces = face_detector.detectMultiScale(frame)  
    for face in faces :
        x , y , w , h  = face
        pic [y:y+int((h/2))+5 , x+30:x+int(w)-30] = frame[y:y+int((h/2))+5   , x+30:x+int(w)-30] #eye
        #pic[y+110:y+int((h/2))+100 , x+30:x+int(w)-30] = frame[y+110:y+int((h/2))+100 , x+30:x+int(w)-30] #lip+nose

    if cv2.waitKey(25) & 0xFF == ord("b"):
        break

