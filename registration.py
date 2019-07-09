users = []
cnt = 0
def registerUser():
	global cnt
	user = {}
	user["id"] = cnt
	cnt +=1
	user['fname'] = input("Enter First Name :")
	user['lname'] = input("Enter Last Name :")
	user['email'] = input("Enter Email :")
	user['phone'] = input("Enter Phone :")
	user['uname'] = input("Enter User Name :")
	user['type'] = input("Enter User Type(A/U) :")
	user['password'] = input("Enter Password :")
	user['active']=1
	flag = 0
	for usr in users:
		if usr['email'] == user['email']:
			flag = 1
			break
		elif usr['phone'] == user['phone']:
			flag = 2
			break
		elif usr['uname'] == user['uname']:
			flag = 3
			break
	if flag == 0:
		users.append(user)
		print("\nUser Registered\n")
	elif flag ==1:
		print(user['email']," Already exist")
	elif flag ==2:
		print(user['phone']," Already exist")
	elif flag ==3:
		print(user['uname']," Already exist")

def loginUser(uname,password):
	for user in users :
		if user['uname'] == uname and user['password'] == password:
			print("\n\nWelcome : ",user['fname']," ",user['lname'])
			if user['type'] == 'a' or user['type']== 'A':
				print("1. Delete User")
				print("2. Display All Users")
				print("0. Exit")
				choice  = int(input("Enter Choice : "))
				if choice == 1:
					email = input("Enter Email id to be Removed : ")
					removeUserByEmail(email)
				elif choice == 2:
					displayAllUsers()
				elif choice == 0:
					print("Bye Bye")
			else:
				searchUser(uname)		
		else:
			print("Invalid Email/Password")
def updateUser(srch):
	pass

def removeUserByEmail(email):
	flag = 0
	for i in users:
		if i['email'] == email:
			flag = 1
			if (flag ==1):
				i.pop('uname')
		else:
			print("Invalid email please enter again email")




def displayAllUsers():
	pass

def searchUser(search):
	flag = 0
	for user in users:
		if user['fname'] == search or user['lname'] == search or user['email'] == search or user['phone'] == search or user['uname'] == search:
			flag = 1
			print("\n************************************\n")
			print("Id \t: ",user['id'])
			print("Name \t: ",user['fname']," ",user['lname'])
			print("Email \t: ",user['email'])
			print("phone \t: ",user['phone'])
			print("User Name \t: ",user['uname'])
			print("Type \t: ",user['type'])
			print("Status \t: ",user['active'])
			print("\n************************************\n")
	if flag == 0:
		print("No User found with ",search);
while(True):
	print("\n****************************************************\n")
	print("1. Register User")
	print("2. Search User")
	print("3. Login User")
	print("4. Update User")
	print("0. Exit")
	choice = int(input("Enter Choice : "))
	if choice == 1:
		registerUser()
	elif choice == 2:
		srch = input("Enter User Name/Email/Phone : ")
		searchUser(srch)
	elif choice == 3:
		uname = input("Enter User uName : ")
		password = input("Enter Password : ")
		loginUser(uname,password)
	elif choice == 4 : 
		srch = input("Enter UserName/Email/Phone : ")
		updateUser(srch)
	elif choice == 0:
		print("\nBye Bye")
		break
	else:
		print("Invalid Choice");




	
