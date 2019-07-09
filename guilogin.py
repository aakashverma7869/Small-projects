import tkinter as tk
username = None
password = None
def loginFunc():
	global username
	global password
	print(username.get()+password.get())

def main():
	global username
	global password

	win = tk.Tk()
	#To create main window.Tk() method
	#main code for add widget is in between in these loop 
	
	username = tk.StringVar()
	password = tk.StringVar()

	win.wm_title("CEBS Login")
	win.geometry("400x400")
	
	userLabel = tk.Label(win,text="Enter User Name")
	userLabel.place(x=30,y=30,width=100,height=30)


        #Entry:It is used to input the single line text entry from the user.. For multi-line text input, Text widget is used.
	userEntry = tk.Entry(win,textvariable=username)
	userEntry.place(x=150,y=30,width=100,height=30)

	passwordLabel = tk.Label(win,text="Enter Password")
	passwordLabel.place(x=30,y=150,width=100,height=30)

	passwordEntry = tk.Entry(win,textvariable=password)
	passwordEntry.place(x=150,y=150,width=100,height=30)

        #first parameter is the parameter used to represent the parent window.
	#command: to call a function
	loginBtn = tk.Button(win,text="Login",command=loginFunc,activebackground="red")
	loginBtn.place(x=30,y=200,width=230,height=30)
	win.mainloop()


if __name__ == "__main__":
	main()
