import platform
from tkinter import Button, Label, Text, Tk, INSERT, END
from tkinter import messagebox, simpledialog
import os
from time import sleep

if (("save" in os.listdir()) == False):
	os.mkdir("save")
sv=[]

def g():
	if ("untitled.c" in os.listdir()):
		open("untitled.c","w").write(text.get("1.0",END))
		os.system("gcc untitled.c -o untitled")
		os.system("untitled")
	else:
		open("untitled.c","a").write(text.get("1.0",END))
		os.system("gcc untitled.c -o untitled")
		os.system("untitled")

def saveas():
	sd = simpledialog.askstring("Save as","Enter filename")
	if (sd in os.listdir("save")):
		messagebox.showerror("Error","File with this name already exists, try again with different name")
	elif (sd == ""):
		messagebox.showinfo("Message","File not saved")
	else:
		open("save/"+sd,"w").write(text.get("1.0",END))
		top.title("Abhineet Raj - "+sd)
		messagebox.showinfo("Saved","File saved successfully!")
		if (len(sv) == 0):
			sv.append("save/"+sd)
		else:
			sv[0] = "save/"+sd
def clss():
	if (platform.system() == "Windows"):
		os.system("cls")
	elif (platform.system() == "Linux"):
		os.system("clear")
	else:
		os.system("clear")

def new_f():
	if (len(sv)>0):
		sv.remove(sv[0])
	clst()

def save():
	if (len(sv) == 0):
		saveas()
	else:
		open(sv[0],"w").write(text.get("1.0",END))
		messagebox.showinfo("Saved","File saved successfully!")

def oen():
	o='';
	for i in os.listdir("save"):
		o = o+"\n"+i
	o=o+"\n"+ "Enter filename"
	sd = simpledialog.askstring("Open",o)
	if (sd in os.listdir("save")):
		text.delete("1.0",END)
		text.insert(INSERT,open("save/"+sd, "r").read())
		top.title("Abhineet Raj - "+sd)
		if (len(sv) == 0):
			sv.append("save/"+sd)
		else:
			sv[0] = "save/"+sd
	elif (sd == ""):
		messagebox.showinfo("Message","File not found")
	else:
		messagebox.showerror("Error","File not found")

def clst():
	text.delete("1.0",END)
	text.insert(INSERT,"#include <stdio.h>\n\nvoid main() {\n	\n}")

top = Tk()
Label(background="black", height=100, width=100).place(x=0,y=0)
top.title("Abhineet Raj")
top.geometry("650x440")
text = Text()
text.place(x=2,y=42)
btn = Button(text="Run", foreground="white", background="green", activebackground="white", font=("Calibri","13"), activeforeground="green", command=g)
btn1 = Button(text="Save", foreground="white", background="green", activebackground="white", font=("Calibri","13"), activeforeground="green", command=save)
btn2 = Button(text="Save as", foreground="white", background="green", activebackground="white", font=("Calibri","13"), activeforeground="green", command=saveas)
btn3 = Button(text="Open", foreground="white", background="green", activebackground="white", font=("Calibri","13"), activeforeground="green", command=oen)
btn4 = Button(text="Clear terminal", foreground="white", background="green", activebackground="white", font=("Calibri","13"), activeforeground="green", command=clss)
btn5 = Button(text="Clear text", foreground="white", background="green", activebackground="white", font=("Calibri","13"), activeforeground="green", command=clst)
btn6 = Button(text="New", foreground="white", background="green", activebackground="white", font=("Calibri","13"), activeforeground="green", command=new_f)
text.insert(INSERT,"#include <stdio.h>\n\nvoid main() {\n	\n}")
btn.place(x=1,y=2)
btn1.place(x=50,y=2)
btn2.place(x=100,y=2)
btn3.place(x=170, y=2)
btn4.place(x=225, y=2)
btn5.place(x=340, y=2)
btn6.place(x=430, y=2)

if __name__ == '__main__':
	top.mainloop()