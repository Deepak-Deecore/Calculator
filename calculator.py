#impoting libs
import tkinter
from tkinter import messagebox

#main windows
root=tkinter.Tk()
root.title("Calculator")
root.geometry("420x470")
root.minsize(420,470)
root.maxsize(420,470)

#defining command functions
#for overall calculation
def cal():
    try:
        value.set(eval(value.get()))
    except:
        tkinter.messagebox.showerror(title="ERROR", message="Illegal Entries!!!\n\nPlease try again")
#for squareroot
def sqrt():
    try:
        value.set(float(value.get())**0.5)
    except:
        tkinter.messagebox.showerror(title="ERROR", message="Illegal Entries!!!\n\nPlease try again")
#for the factorial
def fact():
    try:
        valint=int(float(val.get()))
        count=1.0
        for i in range(1,valint+1):
            count=count*float(i)
        value.set(count)
    except:
        tkinter.messagebox.showerror(title="ERROR", message="Illegal Entries!!!\n\nPlease try again")
    
#creating GUI    
value=tkinter.StringVar()
val=tkinter.Entry(root,textvariable=value,font="serif 20",width=25,borderwidth=5,justify="right")
val.grid(row=0,column=0,columnspan=4,pady=20)
tkinter.Button(root,text="C",command=lambda :val.delete(0,tkinter.END),font="serif 10 bold",height= 3, width=4).grid(row=1,column=0,padx=30,pady=7)
tkinter.Button(root,text="√",command=sqrt,font="serif 10 bold",height= 3, width=4).grid(row=1,column=1,padx=30,pady=7)
tkinter.Button(root,text="/",command=lambda :value.set(value.get()+"/"),font="serif 10 bold",height= 3, width=4).grid(row=1,column=2,padx=30,pady=7)
tkinter.Button(root,text="<_",command=lambda :val.delete(len(val.get())-1,tkinter.END),font="serif 10 bold",height= 3, width=4).grid(row=1,column=3,padx=30,pady=7)
tkinter.Button(root,text="7",command=lambda :value.set(value.get()+"7"),font="serif 10 bold",height= 3, width=4).grid(row=2,column=0,padx=30,pady=7)
tkinter.Button(root,text="8",command=lambda :value.set(value.get()+"8"),font="serif 10 bold",height= 3, width=4).grid(row=2,column=1,padx=30,pady=7)
tkinter.Button(root,text="9",command=lambda :value.set(value.get()+"9"),font="serif 10 bold",height= 3, width=4).grid(row=2,column=2,padx=30,pady=7)
tkinter.Button(root,text="*",command=lambda :value.set(value.get()+"*"),font="serif 10 bold",height= 3, width=4).grid(row=2,column=3,padx=30,pady=7)
tkinter.Button(root,text="4",command=lambda :value.set(value.get()+"4"),font="serif 10 bold",height= 3, width=4).grid(row=3,column=0,padx=30,pady=7)
tkinter.Button(root,text="5",command=lambda :value.set(value.get()+"5"),font="serif 10 bold",height= 3, width=4).grid(row=3,column=1,padx=30,pady=7)
tkinter.Button(root,text="6",command=lambda :value.set(value.get()+"6"),font="serif 10 bold",height= 3, width=4).grid(row=3,column=2,padx=30,pady=7)
tkinter.Button(root,text="-",command=lambda :value.set(value.get()+"-"),font="serif 10 bold",height= 3, width=4).grid(row=3,column=3,padx=30,pady=7)
tkinter.Button(root,text="1",command=lambda :value.set(value.get()+"1"),font="serif 10 bold",height= 3, width=4).grid(row=4,column=0,padx=30,pady=7)
tkinter.Button(root,text="2",command=lambda :value.set(value.get()+"2"),font="serif 10 bold",height= 3, width=4).grid(row=4,column=1,padx=30,pady=7)
tkinter.Button(root,text="3",command=lambda :value.set(value.get()+"3"),font="serif 10 bold",height= 3, width=4).grid(row=4,column=2,padx=30,pady=7)
tkinter.Button(root,text="+",command=lambda :value.set(value.get()+"+"),font="serif 10 bold",height= 3, width=4).grid(row=4,column=3,padx=30,pady=7)
tkinter.Button(root,text="!",command=fact,font="serif 10 bold",height= 3, width=4).grid(row=5,column=0,padx=30,pady=7)
tkinter.Button(root,text="0",command=lambda :value.set(value.get()+"0"),font="serif 10 bold",height= 3, width=4).grid(row=5,column=1,padx=30,pady=7)
tkinter.Button(root,text=".",command=lambda :value.set(value.get()+"."),font="serif 10 bold",height= 3, width=4).grid(row=5,column=2,padx=30,pady=7)
tkinter.Button(root,text="=",command=cal,font="serif 10 bold",height= 3, width=4).grid(row=5,column=3,padx=30,pady=7)

#end the mainloop
root.mainloop()