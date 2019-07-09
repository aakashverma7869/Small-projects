import tkinter as tk
from tkinter import messagebox
number = None
val = "";
A = 0
operator =""
def Entry1():
        global val
        val = val+"1"
        number.set(val)
def Entry2():
        global val
        val = val+"2"
        number.set(val)
def Entry3():
        
        global val
        val = val+"3"
        number.set(val)
def Entry4():
        global val
        val = val+"4"
        number.set(val)
def Entry5():
        global val
        val = val+"5"
        number.set(val)
def Entry6():
        global val
        val = val+"6"
        number.set(val)    
def Entry7():
        global val
        val = val+"7"
        number.set(val)
def Entry8():
        global val
        val = val+"8"
        number.set(val)
def Entry9():
        global val
        val = val+"9"
        number.set(val)
def EntryMul():
        global val
        global A
        global operator
        operator ="*"
        A = int(val)
        
        val = val+"*"
        number.set(val)
        
def EntryDivide():
        global val
        global A
        global operator
        operator = "/"
        A = int(val)
        val = val+"/"
        number.set(val)

def EntryAdd():
        global val
        global A
        global operator
        operator = "+"
        A = int(val)
        val = val+"+"
        number.set(val)
def EntrySub():
        global val
        global A
        global operator
        operator = "-"
        A = int(val)
        val = val+"-"
        number.set(val)
def Clear():
        global val
        global operator
        global A
        val = "";
        operator="";
        A = ""
        number.set(val)
def EntryEqual():
        global val
        global A
        global operator
        val2 = val
        if operator == "+":
                x = int(val2.split("+")[1])
                C = A+x
                number.set(C)
                val = str(C)
        elif operator =="-":
                x = int(val2.split("-")[1])
                C = A-x
                number.set(C)
                val = str(C)
        elif operator =="*":
                x = int(val2.split("*")[1])
                C = A*x
                number.set(C)
                val = str(C)
        elif operator =="/":
                x = int(val2.split("/")[1])
                if(x == 0):
                        messagebox.showerror("Error","Division 0 is not support")
                        A = ""
                        val = ""
                        data.set(val)
                else:
                        C = int(A/x)
                        number.set(C)
                        val = str(C)
def EntryZero():
        global val
        val = val+"0"
        
        number.set(val)
        
def main():
	global number
	win = tk.Tk()
	#To create main window.Tk() method
	#main code for add widget is in between in these loop 
	
	number = tk.StringVar()

	win.wm_title("Calculator")
	win.geometry("600x600")
	
	userLabel = tk.Label(win,text="Calculator Display")
	userLabel.place(x=8,y=20,width=200,height=150)


        #Entry:It is used to input the single line text entry from the user.. For multi-line text input, Text widget is used.
	userEntry = tk.Entry(win,textvariable=number)
	userEntry.place(x=200,y=30,width=300,height=160)
	userEntry.config(font=("Courier", 80))

        #first parameter is the parameter used to represent the parent window.
	#command: to call a function
	loginBtn = tk.Button(win,text="1",command=Entry1,activebackground="red")
	loginBtn.place(x=30,y=200,width=100,height=50)
	loginBtn = tk.Button(win,text="2",command=Entry2,activebackground="blue")
	loginBtn.place(x=150,y=200,width=100,height=50)
	loginBtn = tk.Button(win,text="3",command=Entry3,activebackground="blue")
	loginBtn.place(x=280,y=200,width=100,height=50)
	loginBtn = tk.Button(win,text="4",command=Entry4,activebackground="yellow")
	loginBtn.place(x=400,y=200,width=100,height=50)
	loginBtn = tk.Button(win,text="5",command=Entry5,activebackground="yellow")
	loginBtn.place(x=30,y=300,width=100,height=50)
	loginBtn = tk.Button(win,text="6",command=Entry6,activebackground="yellow")
	loginBtn.place(x=150,y=300,width=100,height=50)
	loginBtn = tk.Button(win,text="7",command=Entry7,activebackground="yellow")
	loginBtn.place(x=280,y=300,width=100,height=50)
	loginBtn = tk.Button(win,text="8",command=Entry8,activebackground="yellow")
	loginBtn.place(x=400,y=300,width=100,height=50)
	loginBtn = tk.Button(win,text="9",command=Entry9,activebackground="yellow")
	loginBtn.place(x=30,y=400,width=100,height=50)
	loginBtn = tk.Button(win,text="0",command=EntryZero,activebackground="yellow")
	loginBtn.place(x=280,y=500,width=100,height=50)
	loginBtn = tk.Button(win,text="X",command=EntryMul,activebackground="yellow")
	loginBtn.place(x=150,y=400,width=100,height=50)
	loginBtn = tk.Button(win,text="/",command=EntryDivide,activebackground="yellow")
	loginBtn.place(x=280,y=400,width=100,height=50)
	loginBtn = tk.Button(win,text="+",command=EntryAdd,activebackground="yellow")
	loginBtn.place(x=400,y=400,width=100,height=50)
	loginBtn = tk.Button(win,text="-",command=EntrySub,activebackground="yellow")
	loginBtn.place(x=30,y=500,width=100,height=50)
	loginBtn = tk.Button(win,text="=",command=EntryEqual,activebackground="yellow")
	loginBtn.place(x=150,y=500,width=100,height=50)
	loginBtn = tk.Button(win,text="Clear",command=Clear,activebackground="yellow")
	loginBtn.place(x=400,y=500,width=100,height=50)
	win.mainloop()


if __name__ == "__main__":
	main()
