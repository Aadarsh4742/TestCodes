import tkinter as tk
from tkinter import *

root = Tk()
root.geometry("300x300")

f1=tk.Frame(root,bg="yellow",height=30,width=30)
f1.pack(side="top",fill="x")

f1=tk.Frame(root,bg="yellow2",height=30,width=30)
f1.pack(side="left", fill="y" )

f1=tk.Frame(root,bg="yellow3",height=30,width=30)
f1.pack(side="right",fill="y")

f1=tk.Frame(root,bg="yellow4",height=30,width=30)
f1.pack(side="bottom",fill="x")

f1=tk.Frame(root,bg="green",height=30,width=30)
f1.pack(side="top",fill="both",expand=1)

root.mainloop()