import cv2
import face_recognition
import pickle
import csv
from datetime import datetime

cap=cv2.VideoCapture(0)
file =open("encodefile.p","rb")
encodewithIds=pickle.load(file)
file.close()
encImg,studentid=encodewithIds
def find_index(matches):
    indexes=[]
    for i in range(len(matches)):
        if matches[i]:
            indexes.append(i)
    return indexes
with open("attendedstudent.csv","w") as file:
                writer=csv.writer(file)
                writer.writerow(["student name","time check-in","probability"])
attendedstudent=set()
while True:
    ret,img=cap.read()
    imgS=cv2.resize(img,(0,0),None,0.25,0.25)
    imgS=cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)
    curFacepos=face_recognition.face_locations(imgS)
    curfaceEnco=face_recognition.face_encodings(imgS,curFacepos)
    for enco,faceloc in zip(curfaceEnco,curFacepos):
        matches=face_recognition.compare_faces(encImg,enco)
        facedis=face_recognition.face_distance(encImg,enco)
        index=find_index(matches)
        for i in index:
            print(studentid[i])
            print(int(facedis[i]*100))
            with open("attendedstudent.csv","a+") as file:
                writer=csv.writer(file)
                if studentid[i] not in list(attendedstudent) and (int(facedis[i]*100)<=50):
                    writer.writerow([studentid[i],datetime.now().time(),facedis[i]])
                    attendedstudent.add(studentid[i])         
    
    cv2.imshow("image",img)
    if cv2.waitKey(1)==ord("q"):
        break
