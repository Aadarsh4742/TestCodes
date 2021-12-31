import tkinter as tk
#------------
frame_options={"bg":"yellow" ,"pady":5,"padx":10,"bd":2,"relief":"solid"}
EntryOptions={"side":"left", "fill":"x", "expand":True}
#------------
root = tk.Tk()
root.geometry('400x300+200+200')
root.attributes("-toolwindow",False)
"""
#--------f1------
f1=tk.Frame(root,frame_options)
f1.pack(side="top",fill="x")
print(f1.keys())
#-----f2
f2=tk.Frame(root,frame_options)
f2.pack(side="top",fill="x")
#-----w1--------
l1=tk.Label(f1,text="First Name:")
l1.pack(side="left" )
#--- entry1---
ent1=tk.Entry(f1)
ent1.pack(EntryOptions)
#------w2---------
l2=tk.Label(f2,text="Last Name:")
l2.pack(side="left" )
#--- entry1---
ent2=tk.Entry(f2)
ent2.pack(EntryOptions)
#--------------
"""
ni=0
for x in ["First Name","Last Name","Job","Age","Phone","Address"]:
    f= tk.Frame(root, frame_options)
    f.pack(side="top", fill="x")
    f.widgetName=f"Frame{ni}"
    #-------
    l = tk.Label(f,width=10,anchor="w", text=x+": ")
    l.pack(side="left")
    l.widgetName=f"Label{ni}"
    # --- entry1---
    ent = tk.Entry(f)
    ent.pack(EntryOptions)
    ent.widgetName=f"Entry{ni}"
    print(ent.widgetName)
    #-------
    ni=ni+1
#--------------
fr_b=tk.Frame(root,bg="green",height=30)
fr_b.pack(side="bottom" ,fill="both",expand=True)
#------butt--------
b1=tk.Button(fr_b,text="Save",width=12)
b1.pack(side="left")
#------------------
#print(root.children)
#print(type(root.nametowidget("object .!Frame0") ))
root.mainloop()