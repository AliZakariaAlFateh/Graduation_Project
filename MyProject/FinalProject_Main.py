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
main_window=Tk()
main_window.title("Face_Detection") #title for window.
main_window.geometry("660x370")
main_window.grid_rowconfigure(0,weight=1)
main_window.grid_columnconfigure(0,weight=1)
# main_window.geometry("700x400")
image = PhotoImage(file="FaceDetection.png")
c = Canvas(main_window, bg='green')
c.pack(fill=BOTH, expand=1)
c.create_image(0, 0, image=image, anchor=NW)
main_Label=Label(c,text="Attendance System By Face Recognation ",bg="yellow",fg="blue",font=("times",20,"italic bold underline"),width="50",height="2").pack(fill=BOTH,padx=0,pady=0)

def Registration_Student():
    main_window.destroy()
    import FinalProject_Registration_GeneratPhotos
    FinalProject_Registration_GeneratPhotos.GUI_Object_Oriented().show_frame()

def Login_Admin():
    main_window.destroy()
    import FinalProject_LogIn_Admin
    FinalProject_LogIn_Admin.GUI_Object_Oriented_LogInAdmin().show_frame()
def Team():
    Window_Team=Tk();
    Window_Team.title("Regiseter Your Information");
    Window_Team.geometry("700x400");
    Window_Team.configure(background='green',relief="solid")
    Window_Team.grid_rowconfigure(0, weight=1)
    Window_Team.grid_columnconfigure(0, weight=1)
    Label_Header=Label(Window_Team,text="Our Team  ",bg="yellow",fg="blue",font=("times",20,"italic bold underline"),width="50",height="2").pack(fill=BOTH,padx=0,pady=10)
    Label_1=Label(Window_Team,text="Ahmed Ali Abd-El Rasheid",bg="blue",relief="solid",fg="white",font=("times",20,"italic bold underline"),width="40",height="1").pack(fill=BOTH,padx=0,pady=13)
    Label_2 = Label(Window_Team,text="Ahmed Yousef Fathey",bg="blue",relief="solid",fg="white",font=("times",20,"italic bold underline"),width="40",height="1").pack(fill=BOTH,padx=0,pady=16)
    Label_3=Label(Window_Team,text="Ali Zakaria Kamel Thabet",bg="blue",relief="solid",fg="white",font=("times",20,"italic bold underline"),width="40",height="1").pack(fill=BOTH,padx=0,pady=22)
    Label_4 = Label(Window_Team,text="Omar Abd-El Salam Ebrahiem",bg="blue",relief="solid",fg="white",font=("times",20,"italic bold underline"),width="40",height="1").pack(fill=BOTH,padx=0,pady=25)

def Registeration_Lecturer():
    main_window.destroy()
    import FinalProject_RegistrationAdmin


but_Registeration_Lecturer=Button(main_window,text="Registeration_Lecturer",fg="white",bg="red",font="15",border=5,relief=GROOVE,bd=5,width=20,activebackground="blue",command=Registeration_Lecturer)
but_Registeration_Lecturer.place(x=50,y=150)
but_Login_Lecturer=Button(main_window,text="Login_Lecturer",fg="white",bg="red",font="15",border=5,relief=GROOVE,bd=5,width=20,activebackground="blue",command=Login_Admin)
but_Login_Lecturer.place(x=270,y=150)
but_Registeration_Student=Button(main_window,text="Registeratio_Student",fg="white",bg="red",font="15",border=5,width=20,activebackground="blue",command=Registration_Student)
but_Registeration_Student.place(x=270,y=200)
but_Close=Button(main_window,text="Close",fg="white",bg="red",font="15",border=5,width=20,activebackground="blue",relief=GROOVE,bd=5,command=main_window.destroy)
but_Close.place(x=270,y=250)
but_Team=Button(main_window,text="Project_Team",fg="white",bg="red",font="15",border=5,width=20,activebackground="blue",command=Team)
but_Team.place(x=270,y=300)
main_window.mainloop()