import cv2
import sqlite3
detector= cv2.CascadeClassifier('G:\\Softwares\\opencv\\sources\\data\\haarcascades_GPU\\haarcascade_frontalface_default.xml')

def insert_or_upd(ID,name):
    c=sqlite3.connect("D:\\Database\\Student_data.db")
    cmd="select * from Details where Id= " + str(ID)
    cur=c.execute(cmd)
    ifrec=0
    for row in cur:
        ifrec=1
    if(ifrec==1):
        cmd= "update Details set Name=" + str(name) + "where Id=" +str(ID)
    else:
        cmd="insert into Details(Id,Name) values ("+str(ID)+","+str(name)+")"
    
    c.execute(cmd)
    c.commit()
    c.close()
    
sampleNum=0

id = input('Enter your ID:')
n = input('Enter name')
insert_or_upd(id,n)

cap = cv2.VideoCapture(0)

while(True):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

        sampleNum=sampleNum+1
        cv2.imwrite("dataSet/User."+str(id)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
        
        cv2.waitKey(100)
    cv2.imshow('frame',img)
    cv2.waitKey(1);
    if (sampleNum>20):
        break
    
cap.release()
cv2.destroyAllWindows()