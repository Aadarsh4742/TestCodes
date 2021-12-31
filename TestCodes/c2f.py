import tkinter as tk
from tkinter import *

def calc():
    c=float(lblEnt.get())
    f=(c * (9/5)) + 32
    #--------------
    lblEntfa["text"]=str(f)+" °F"
    lblEntfa["font"]="25"

root = tk.Tk()
root.geometry("300x150")
root.title("Celsius to Fahrenheit")
f1=tk.Frame(root, height=30,width=30,pady=5)
f1.pack(side="top",fill="x")

f2=tk.Frame(root, height=30,width=30,pady=5)
f2.pack(side="top",fill="x")

f3=tk.Frame(root, height=30,width=30)
f3.pack(side="top",fill="x")
#-----------------------------------fahrenheit
lblCel=tk.Label(f1,text="Celsius: ",width=10,anchor="w")
lblCel.pack(side="left",padx=(5,0))

lblEnt=tk.Entry(f1 )
lblEnt.pack(side="left")
#-------------------------------------
lblFa=tk.Label(f2,text="Farenhait: ",width=10,anchor="w")
lblFa.pack(side="left",padx=(5,0))

lblEntfa=tk.Label(f2  )
lblEntfa.pack(side="left")
#-------------------------------------
ButtCalc=tk.Button(f3 ,text="Convert",width=10,command=calc)
ButtCalc.pack()
#-------------------------------------
root.mainloop()