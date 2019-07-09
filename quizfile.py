def AddQuestionReadable():
        file = open ("QuizReadable.txt","w")

        while True:
                name = input("Enter question \t: ")
                optionA = input("Enter the option A \t: ")
                optionB = input("Enter the option A \t: ")
                a = input("Do you want to enter more Option?")
                if(a=='n' or a=='N'):



                       correct = input("Enter the correct option") 
                       file.write(name+","+optionA+","+optionB+"correct"+correct+"\n")
                optionC = input("Enter the option C \t: ")
                b = input("Do you want to enter more Option?")
                if(b=='n' or b=='N'):
                       correct = input("Enter the correct option") 
                       file.write(name+"\n Option A:  "+optionA+"\n Option B:  "+optionB+"\n Option C:   "+optionC+"\n")
                optionD = input("Enter the Option D")
                correct = input("Enter the correct option")
                file.write(name+"\nOption A  "+optionA+"\nOption B:   "+optionB+"\n Option C:   "+optionC+"\n Option D:   "+optionD+"correct:"+correct)
                choice  = input("Do you want to add more Question(Y/N) : ")
                if choice == 'n' or choice == 'N':
                        break;

        file.close()
def AddQuestion():
        file = open ("Quiz.txt","a")

        while True:
                name = input("Enter question \t: ")
                optionA = input("Enter the option A\t: ")
                optionB = input("Enter the option A\t: ")
                a = input("Do you want to enter more Option?")
                if(a=='n' or a=='N'):
                       file.write(name+","+optionA+","+optionB+"\n")
                optionC = input("Enter the option C \t: ")
                b = input("Do you want to enter more Option?")
                if(b=='n' or b=='N'):
                       file.write(name+","+optionA+","+optionB+","+optionC+"\n")
                optionD = input("Enter the Option D")
                correct = input("Enter the correct Option")
                file.write("Question:   "+name+  "Option A:  "+optionA+  "Option B:  "+optionB+  "Option C:  "+optionC+    "Option D:  "+optionD+","+correct+"\n")
                choice  = input("Do you want to add more Question(Y/N) : ")
                if choice == 'n' or choice == 'N':
                        break;
        
        file.close()

def PlayQuiz():
                
                file = open("Quiz.txt","r")
                
                users = file.readlines()
                for user in users:
                        userdata=user.split(",")
                        print(userdata[0])
                        ans = input("please enter your ans")
                        print(userdata[1][0])
                        if(userdata[1][0] == ans):
                                print("your ans is correct")
                        else:
                                print("Your ans is incorrect")
                file.close()




                  
       
                #users = file.readlines()
                
                #a=str(users)
                #user_data = a.split("correct:")
                #print(str(user_data[0]))
                #s = input("enter your answere?")
                #print(user_data[1])
                #if(user_data[1]==s):
                 #       print("your answere is correct")

while(True):
        print("\n****************************************************\n")
        print("1. AddQuestion")
        print("2. PlayQuiz")
        print("3. AddQuestionReadable")
        print("0. Exit")
        choice = int(input("Enter Choice : "))
        if choice == 1:
            AddQuestion()
        elif choice == 2:
                
            PlayQuiz()
        elif choice == 3:
            AddQuestionReadable()
        elif choice == 0:
            print("\nBye Bye")
            break
        else:
            print("Invalid Choice");

