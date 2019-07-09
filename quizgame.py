
questions = []
cnt = 1
Options = []
corrects = []
def AddQuestion():
    global cnt
    question = {}
    Option = {}
    correct = {}
    question["id"] = cnt
    Option['id'] = cnt
    correct['id'] = cnt
    cnt +=1
    question['fname'] = input("Enter the question :")
    
    Option['a']=input("Enter the first Option")
    Option['b']=input("Enter the Secondd Option")
    z = input("Do you want to enter more option Y/N")
    if(z=='Y' or z=='y'):
            Option['c']=input("Enter the third option")
            z = input("Do you want to enter more option Y/N")
            if(z=='Y' or z=='y'):
                    Option['d']=input("Enter the fourth option")
    correct['f']=input("please enter the correct option a/b/c/d?")
    flag = 0
    for usr in questions:
            if usr['fname'] == question['fname']:
                    flag = 1
                    break		
    if flag == 0:
            questions.append(question)
            print("\nQuestion Registered\n")
    if flag ==1:	
            print(question['fname']," Already exist question")
    Options.append(Option)
    corrects.append(correct)
def PlayQuiz():
    p = 0    
    for user in questions:
            
            print("\n************************************\n")
            print("Id \t: ",user['id'])
            print("Question \t: ",user['fname'])
            for i in Options:
                    if (i['id']==user['id']):
                        print("Option A\t:",i['a'])
                        print("Option B\t:",i['b'])
                        print("Option C\t:",i['c'])
                        print("Option D\t:",i['d'])
                        m = input("Please enter the  your answere")
                        for j in corrects:
                                if(j['id']==user['id']):
                                        if(j['f']==m):
                                                print("your answere is correct")
                                        
                                                p = p+1
                                        print("Total score is", +p) 
            print("\n************************************\n")

while(True):
    print("\n****************************************************\n")
    print("1. AddQuestion")
    print("2. PlayQuiz")
    print("0. Exit")
    choice = int(input("Enter Choice : "))
    if choice == 1:
            AddQuestion()
    elif choice == 2:
            PlayQuiz()
    elif choice == 0:
            print("\nBye Bye")
            break
    else:
            print("Invalid Choice");




            
