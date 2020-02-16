import cv2,os
from tkinter import *
from tkinter import messagebox
from tkinter import font
from PIL import Image
# import pyQt4
# import face_recognition
import numpy as nnn
from PIL import Image
# import face_recognition.api
import pickle
import dlib
class AfterSubmittingAdminclass():
    def show_frame(self):
        Controlwindow = Tk();
        Controlwindow.title("Regiseter Your Information");
        Controlwindow.geometry("700x400");
        Controlwindow.configure(background='green', relief="solid")
        Controlwindow.grid_rowconfigure(0, weight=1)
        Controlwindow.grid_columnconfigure(0, weight=1)
        image = PhotoImage(file="Capture1.png")
        c = Canvas(Controlwindow, bg='green')
        c.pack(fill=BOTH, expand=1)
        c.create_image(0, 0, image=image, anchor=NW)
        var_level=StringVar()
        def welcom():
            # import FinalProject_LogIn_Admin
            # name=FinalProject_LogIn_Admin.GUI_Object_Oriented_LogInAdmin().show_frame().getDataFromLogin()
            messagebox.showinfo("Inputs","Mr : kkk ,"+"The report has not prepared yet . " )

        def Detection_Faces():
            # level=var_level.get()
            import Final_Project_Face_Detection
            Final_Project_Face_Detection.FaceDetectionClass().Detection_Faces()
        but_Detection = Button(Controlwindow, text="Detection _Photo", fg="white", bg="red", font="15", border=5, width=20, command=Detection_Faces, activebackground="blue")
        but_Detection.place(x=260, y=140)
        Label_Header = Label(c, text="Report For Attendance ", bg="yellow", fg="blue",font=("times", 20, "italic bold underline"), width="50", height="2").pack(fill=BOTH,padx=0, pady=0)
        but_Report = Button(Controlwindow, text="Show _Report", fg="white", bg="red", font="15", border=5,width=15, activebackground="blue", command=welcom).place(x=280, y=250)
        Label_Header = Label(Controlwindow, text="Enter lvel ",width=20, bg="yellow", fg="blue",font=("times", 15, "italic bold underline"),height="1").place(x=0, y=90)
        Entry_Level = Entry(Controlwindow, textvariable=var_level, width="50", justify=CENTER).place(x=250, y=90)
        Controlwindow.mainloop()

# AfterSubmittingAdminclass().show_frame()