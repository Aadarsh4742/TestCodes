import tkinter as tk
import tkinter.ttk as ttk
#--------------------
MyWindow=tk.Tk()
MyWindow.geometry("500x170")
MyWindow.title("Find and Repalce")
MyWindow.attributes("-toolwindow",True)

#-------Top----------
RFrame=tk.Frame(MyWindow,  width=150,padx=10 )
RFrame.pack(side="right",fill="y")
#--------------------
TopFrame=tk.Frame(MyWindow,  height=50,pady=5)
TopFrame.pack(side="top",fill="x")
#--------------------
TopFrame1=tk.Frame(MyWindow,  height=50,pady=5)
TopFrame1.pack(side="top",fill="x")
#--------------------
FindButt=tk.Button(RFrame,text="Find Next",width=10, )
FindButt.pack(side="top",pady=(10,5))
#--------------------
RepButt=tk.Button(RFrame,text="Replace",width=10 )
RepButt.pack(side="top",pady=(0,5))
#--------------------
RepallButt=tk.Button(RFrame,text="Replace All",width=10 )
RepallButt.pack(side="top",pady=(0,5))

#--------------------
canButt=tk.Button(RFrame,text="Cancel",width=10 )
canButt.pack(side="top",pady=(0,5))
#--------------------
#====================
lbl=tk.Label(TopFrame,text="Find What:",width=20)
lbl.pack(side="left")
#--------------------
lbl=tk.Entry(TopFrame,width=40 )
lbl.pack(side="left")
#--------------------
#====================
lbl=tk.Label(TopFrame1,text="Replace with:",width=20)
lbl.pack(side="left")
#--------------------
lbl=tk.Entry(TopFrame1,width=40 )
lbl.pack(side="left")
#--------------------
MyWindow.mainloop()
#--------------------