from tkinter import *#pressana kumar
from tkinter import ttk
from tkinter import messagebox
from tkinter import ttk
from cv2 import *
import csv
import os
from datetime import datetime
#import main

front=Tk()
front.title("SMART ATTENDANCE SYSTEM")
T=Text(front)
def screen_size(S):
    W=1300
    H=600
    sw=S.winfo_screenwidth()
    sh=S.winfo_screenheight()
    x=(sw/2)-(W/2)
    y=(sh/2)-(H/2)
    S.geometry("%dx%d+%d+%d" % (W,H,x,y))
screen_size(front)
front.configure(bg="blue")
front.grid_rowconfigure(0, weight=0)
front.grid_columnconfigure(0, weight=1)
Firstline=Label(front,text="SMART ATTENDANCE SYSTEM",bg="orange",fg="black",font=("times",30,"bold"))
Firstline.grid(row=0, column=0)
Firstline.grid_rowconfigure(0, weight=0)
Firstline.grid_columnconfigure(0, weight=0)

def check():
    os.system(r'D:/project/mini_project/main.py')

L1=Button(front,text="CHECK attendence",bg="light blue",fg="black",font=("times",20,"bold"),command=check)
L1.grid(row=2,column=0)
#B1=Button(front,text="CLICK HERE",bg="white",fg="black",activebackground="green",activeforeground="white",font=("times",20,"bold"),command=Checking)
#B1.grid(row=2,column=1,padx=30,pady=10)

def Attendance():
    S2=Tk()
    
    S2.title("ATTENDANCE")
    screen_size(S2)
    sheet=ttk.Treeview(S2)
    filename=r".\attendedstudent.csv"
    data=os.path.split(filename)
    name=data[1]
    out=data[0]
    sheet["columns"]=("","Student Name","Time Check-in","Probability")
    sheet.column("#0",width=20)
    sheet.column("#1",width=100)
    sheet.column("#2",width=30)
    sheet.column("#3",width=80)
    
    sheet.heading("#0",text="")
    sheet.heading("#1",text="STUDENT NAME")
    sheet.heading("#2",text="TIME CHECK-IN")
    sheet.heading("#3",text="PROBABILITY")
    with open("attendedstudent.csv","r") as file:
        read=csv.reader(file)
        for i in read:
            if len(i)!=0:
                sheet.insert("",index="end",values=(i[0],i[1],i[2]))
    sheet.pack(fill=X)
    S2.mainloop()

L2=Button(front,text="SHOW ATTENDANCE",bg="light blue",fg="black",font=("times",20,"bold"),anchor=W,command=Attendance)
L2.grid(row=3,column=0)
#B2=Button(front,text="CLICK HERE",bg="white",fg="black",activebackground="green",activeforeground="white",font=("times",20,"bold"),command=Attendance)
#B2.grid(row=3,column=1,padx=30,pady=10)
front.mainloop()
