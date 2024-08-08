import cv2
import face_recognition
import pickle 
import os

folder="trained_images"
pathList=os.listdir(folder)
imageList=[]
studentids=[]
for i in pathList:
    id=i.split(".")[0]
    studentids.append(id)
    imageList.append(cv2.imread(os.path.join(folder,i)))

def encoding(imgList):
    encodedimage=[]
    for img in imgList:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode=face_recognition.face_encodings(img)[0]
        encodedimage.append(encode)
    return encodedimage

encoded=encoding(imageList)
encodeandId=[encoded,studentids]
file=open("encodefile.p","wb")
pickle.dump(encodeandId,file)
file.close()