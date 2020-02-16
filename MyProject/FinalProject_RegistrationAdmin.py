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
window_Registeration = Tk();
Input_Register_Lecturer_user = StringVar()
Input_Register_Lecturer_password = StringVar()
Input_Register_Lecturer_email = StringVar()
window_Registeration.title("Regiseter Your Information");
window_Registeration.geometry("580x400");
window_Registeration.configure(background='green')
window_Registeration.grid_rowconfigure(0, weight=1)
window_Registeration.grid_columnconfigure(0, weight=1)
image=PhotoImage(file="register11.png")
c=Canvas(window_Registeration,bg='green')
c.pack(fill=BOTH,expand=1)
c.create_image(0,0,image=image,anchor=NW)
def MainWindow():
    window_Registeration.destroy()
    import FinalProject_Main
main_Label=Label(c,text="Registeration Lecturer",bg="yellow",fg="blue",font=("times",20,"italic bold underline"),width="50",height="2").pack(fill=BOTH,padx=0,pady=0)
Label_User = Label(window_Registeration, text="Please,Enter user name : ", bg="yellow", relief="solid", fg="green",font=("arial", 12, "bold"), width="20", height="1").place(x=0, y=90)
Label_Password = Label(window_Registeration, text="Please,Enter Password : ", bg="yellow", relief="solid", fg="green",font=("arial", 12, "bold"), width="20", height="1").place(x=0, y=130)
Label_Email = Label(window_Registeration, text="Please,Enter Email : ", bg="yellow", relief="solid", fg="green", font=("arial", 12, "bold"), width="20", height="1").place(x=0, y=170)
Label_profession = Label(window_Registeration, text="Please,Enter profession : ", bg="yellow", relief="solid",fg="green", font=("arial", 12, "bold"), width="20", height="1").place(x=0, y=210)
Entry_User = Entry(window_Registeration, textvariable=Input_Register_Lecturer_user, width="50", justify=CENTER,bd=2).place(x=250, y=93)
Entry_Password = Entry(window_Registeration, show="*", textvariable=Input_Register_Lecturer_password, width="50",justify=CENTER,bd=2).place(x=250, y=133)
Entry_Email = Entry(window_Registeration, show="*", textvariable=Input_Register_Lecturer_email, width="50",justify=CENTER,bd=2).place(x=250, y=173)
Entry_profession = Entry(window_Registeration, show="*", textvariable=Input_Register_Lecturer_email, width="50",justify=CENTER,bd=2).place(x=250, y=213)
but_Login = Button(window_Registeration, text="Submit", fg="white", bg="blue", font="15", border=5, width=40,activebackground="blue", command=MainWindow).place(x=130, y=270)
window_Registeration.mainloop()