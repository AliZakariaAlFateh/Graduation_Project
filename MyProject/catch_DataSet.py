import cv2,os
from  tkinter import*
import numpy as nnn
from PIL import Image
import pickle
import dlib
# import face_recognition
#detector = dlib.get_frontal_face_detector()
from tkinter import messagebox
main_window=Tk()
main_window.title("Face_Detection") #title for window.
main_window.geometry("700x400")
main_window.configure(background='green')
main_window.grid_rowconfigure(0,weight=1)
main_window.grid_columnconfigure(0,weight=1)
main_Label=Label(main_window,text="Attendance System By Face Recognation ",bg="yellow",fg="blue",font=("times",20,"italic bold underline"),width="50",height="2")
main_Label.place(x=0,y=10)
#Face Detection for our project
faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
cam=cv2.VideoCapture(0)
input='true'
input1=StringVar()
def FaceDetection():
    in1 = input1.get()
    samplnum=0
    while (True):
        ret,img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceDetect.detectMultiScale(gray, 1.3, 5);
        for (x, y, w, h) in faces:
            samplnum=samplnum+1
            cv2.imwrite("Data_Set/User."+str(in1)+"."+str(samplnum)+".jpg",gray[y:y+h,x:x+w])
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.waitKey(100)
        cv2.imshow("Face Detection , press q to close the camera .", img)
        cv2.waitKey(1)
        if(samplnum==100):
            break;


    cam.release();
    cv2.destroyAllWindows();
b1=Button(main_window,text="Take_Photo",fg="white",bg="red",font="15",border=5,width=15,command=FaceDetection,activebackground="blue")
b1.place(x=40,y=80)
b2=Button(main_window,text="Close",fg="white",bg="red",font="15",border=5,width=15,activebackground="blue",command=main_window.destroy)
b2.place(x=40,y=130)
text_1=Entry(main_window,textvariable=input1,width="50").place(x=250,y=90)
# text_1.place(x=40,y=170)
main_window.mainloop()