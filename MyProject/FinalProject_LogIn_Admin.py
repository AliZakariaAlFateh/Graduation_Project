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
class GUI_Object_Oriented_LogInAdmin():
    def show_frame(self):
        window_login=Tk();
        window_login.title("Regiseter Your Information");
        window_login.geometry("600x370");
        Input_Login_Lecturer_user= StringVar()
        Input_Login_Lecturer_password= StringVar()
        window_login.configure(background='green')
        window_login.grid_rowconfigure(0, weight=1)
        window_login.grid_columnconfigure(0, weight=1)
        image = PhotoImage(file="Registeration_Photo.png")
        c = Canvas(window_login, bg='green')
        c.pack(fill=BOTH, expand=1)
        c.create_image(0, 0, image=image, anchor=NW)
        def After_Submitting():
            name=Input_Login_Lecturer_user.get()
            password=Input_Login_Lecturer_password.get()
            window_login.destroy()
            import Final_Project_AfterSubmitting_Admin
            Final_Project_AfterSubmitting_Admin.AfterSubmittingAdminclass().show_frame()
        # def getDataFromLogin():
        #     name=Input_Login_Lecturer_user.get()
        #     password=Input_Login_Lecturer_password.get()
        #     return name
        Label_Header=Label(c,text="Login ",bg="yellow",fg="blue",font=("times",20,"italic bold underline"),width="50",height="2").pack(fill=BOTH,padx=0,pady=0)
        Label_User=Label(window_login,text="Please,Enter user name: ",bg="yellow",relief="solid",fg="green",font=("arial",12,"bold"),width="20",height="1").place(x=0,y=90)
        Label_Password = Label(window_login,text="Please,Enter Password: ",bg="yellow",relief="solid",fg="green",font=("arial", 12, "bold"),width="20",height="1").place(x=0,y=130)
        Entry_User = Entry(window_login, textvariable=Input_Login_Lecturer_user,width="50",justify=CENTER,bd=4).place(x=250,y=93)
        Entry_Password = Entry(window_login,show="*", textvariable=Input_Login_Lecturer_password,width="50",justify=CENTER,bd=4).place(x=250,y=133)
        but_Login = Button(window_login, text="Submit", fg="white", bg="red", font="15", border=5, width=15, activebackground="blue",command=After_Submitting).place(x=280, y=210)
        window_login.mainloop()
# GUI_Object_Oriented_LogInAdmin().show_frame()