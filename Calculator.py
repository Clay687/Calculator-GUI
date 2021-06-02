from tkinter import *
from PIL import Image,ImageTk
import math
import pkg_resources.py2_warn
import win32gui , win32con

def click(event):
    text = event.widget.cget("text")
    # print(text)

    if text=="=":
        if value.get().isdigit():
            new_value = int(value.get())

        else:
            try:
                new_value = eval(screen.get())
            except Exception as e:
                new_value = "Error"
        value.set(new_value)
    elif text == "C":
        value.set("")
        screen.update()

    elif text=="π":
        value.set("3.14159")

    elif text=="n!":
        num = value.get()
        fact = math.factorial(int(num))
        value.set(fact)
        screen.update()

    elif text=="x\u00b2":
        num = value.get()
        square = int(num) * int(num)
        value.set(square)
        screen.update()

    else:
        value.set(value.get() + text)
        screen.update()

root = Tk()
hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hide,win32con.SW_HIDE)

root.geometry("360x475")
root.minsize(360,475)
root.maxsize(360,475)
root.title("Calculator")
root.wm_iconbitmap("C:\\Users\\prince\\Desktop\\GUI\\Required files\\Calculator.ico")
root.configure(background="#E8E8E8")

value = StringVar()
value.set("")

screen = Entry(root,textvar=value,font="Calibri 30",width=16,background="#E8E8E8")
screen.place(x=17,y=60,height=40)


btn = Button(root,text="C",font="Calibri 20",padx=25,background="white")
btn.bind("<Button-1>",click)
btn.place(x=5,y=415)

btn = Button(root,text="0",font="Calibri 20",padx=25,background="white")
btn.bind("<Button-1>",click)
btn.place(x=90,y=415)

btn = Button(root,text=".",font="Calibri 20",padx=25,background="white")
btn.bind("<Button-1>",click)
btn.place(x=180,y=415)

btn = Button(root,text="=",font="Calibri 20",padx=25,background="#63C5DA")
btn.bind("<Button-1>",click)
btn.place(x=270,y=415)

btn = Button(root,text="1",font="Calibri 20",padx=25,background="white")
btn.bind("<Button-1>",click)
btn.place(x=5,y=355)

btn = Button(root,text="2",font="Calibri 20",padx=25,background="white")
btn.bind("<Button-1>",click)
btn.place(x=90,y=355)

btn = Button(root,text="3",font="Calibri 20",padx=22,background="white")
btn.bind("<Button-1>",click)
btn.place(x=180,y=355)

btn = Button(root,text="+",font="Calibri 20",padx=25,background="white")
btn.bind("<Button-1>",click)
btn.place(x=270,y=355)

btn = Button(root,text="4",font="Calibri 20",padx=25,background="white")
btn.bind("<Button-1>",click)
btn.place(x=5,y=295)

btn = Button(root,text="5",font="Calibri 20",padx=25,background="white")
btn.bind("<Button-1>",click)
btn.place(x=90,y=295)

btn = Button(root,text="6",font="Calibri 20",padx=22,background="white")
btn.bind("<Button-1>",click)
btn.place(x=180,y=295)

btn = Button(root,text="-",font="Calibri 20",padx=27,background="white")
btn.bind("<Button-1>",click)
btn.place(x=270,y=295)

btn = Button(root,text="7",font="Calibri 20",padx=25,background="white")
btn.bind("<Button-1>",click)
btn.place(x=5,y=235)

btn = Button(root,text="8",font="Calibri 20",padx=25,background="white")
btn.bind("<Button-1>",click)
btn.place(x=90,y=235)

btn = Button(root,text="9",font="Calibri 20",padx=23,background="white")
btn.bind("<Button-1>",click)
btn.place(x=180,y=235)

btn = Button(root,text="*",font="Calibri 20",padx=25,background="white")
btn.bind("<Button-1>",click)
btn.place(x=270,y=235)

btn = Button(root,text="π",font="Calibri 20",padx=25,background="white")
btn.bind("<Button-1>",click)
btn.place(x=5,y=175)

btn = Button(root,text="n!",font="Calibri 20",padx=21,background="white")
btn.bind("<Button-1>",click)
btn.place(x=90,y=175)

btn = Button(root,text="x\u00b2",font="Calibri 20",padx=20,background="white")
btn.bind("<Button-1>",click)
btn.place(x=180,y=175)

btn = Button(root,text="/",font="Calibri 20",padx=25,background="white")
btn.bind("<Button-1>",click)
btn.place(x=270,y=175)


root.mainloop()
