import cv2,os
from tkinter import *
from tkinter import messagebox
from tkinter import font
# import pyQt4
# import face_recognition
import numpy as nnn
from PIL import Image
# import face_recognition.api
import pickle
import dlib
class FaceDetectionClass():
    def Detection_Faces(self):
        faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
        cam = cv2.VideoCapture(0)
        # font=cv2.cv2.InitFont(cv2.cv2.CV_FONT_HERSHEY_SIMPLEX,1,.5,0,2,1) #Creates a font.
        while (True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = faceDetect.detectMultiScale(gray, 1.3, 5);
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
            # cv2.cv2.PutText(cv2.cv2.fromarray(img),"UnKnown_Face",(x,y+h+20),font,(0,0,255)) #Draws a text.
            # cv2.waitKeyEx(80)
            cv2.imshow("Face Detection , press q to close the camera .", img)
            if (cv2.waitKey(1) == ord('q')):
                break;

        cam.release();
        cv2.destroyAllWindows();


# FaceDetectionClass().Detection_Faces()
