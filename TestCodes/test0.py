import tkinter as tk
#------------

#------------
root = tk.Tk()
root.geometry('400x300+200+200')
#------------
b1=tk.Frame(root, bg="yellow",height=30)
b1.pack(side="top",fill="x" )
#------------
b1=tk.Frame(root, bg="yellow2",width=30)
b1.pack(side="left",fill="y" )
#------------
b1=tk.Frame(root, bg="yellow3",width=30)
b1.pack(side="right",fill="y" )
#------------
b1=tk.Frame(root, bg="yellow4",height=30)
b1.pack(side="bottom",fill="x" )
#------------
b1=tk.Frame(root, bg="green")
b1.pack(side="left",fill="both" ,expand=True)
print(b1.keys())
#------------
root.mainloop()