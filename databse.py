import mysql.connector as MySQL

def AddDataBase():
	try:
		conn = MySQL.connect(host="localhost",user="root",passwd="")
		print("Connection Created");

		cursor = conn.cursor()
		dataBase = input("Please Enter the database name")
		
		sql = "create database "+dataBase;
		print("Bye Bye your database is created Enjoy")
		cursor.execute(sql)
		conn.close()
                
		conn = MySQL.connect(host="localhost",user="root",passwd="",database = dataBase)
		cursor = conn.cursor()
		sql = "create table user(uid integer,name varchar(30),email varchar(30),phone varchar(15))"
		cursor.execute(sql)

		conn.commit()
	except Exception as e:
		print("OOPS Connection Error :",e)


def Addtable():
    
        try:
            conn = MySQL.connect(host="localhost",user="root",passwd="",database = input("In which data base you want too entry?........"))
            cursor = conn.cursor()
            sql = "create table "+input('Please Enter the table name')+ +input("Enter column name")+ +input("Enter the dsta type")                             (uid integer,name varchar(30),email varchar(30),phone varchar(15))"
            cursor.execute(sql)

            conn.commit()
               
        except Exception as e:
                print("OOPS Connection Error :",e)

    
while(True):
    print("\n****************************************************\n")
    print("1. AddDataBase")
    print("2. Create table to that database")
    print("0. Exit")
    choice = int(input("Enter Choice : "))
    if choice == 1:
            AddDataBase()
    elif choice == 2:
            Addtable()
    elif choice == 0:
            print("\nBye Bye")
            break
    else:
            print("Invalid Choice");




