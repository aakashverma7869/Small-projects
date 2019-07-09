from random import randrange

fileName = 'questions.txt'

def choose_y_n(string):
    choice = input(string + " : ").lower()
    while True:
        if choice == 'n':
            return 'n'
        elif choice == 'y':
            return 'y'
        else:
            choice = input('invalid choice .... select either (y/n) : ').lower()

def choose_options(string, options):
    option_string = '/'.join(options)
    string += '(' + option_string + ') : '
    choice = input(string).upper()
    while True:
        if choice in options:
            return choice
        else:
            choice = input('invalid choice.......please try again with ('+ option_string + ') : ').upper()
            

def add_a_question():
    global fileName
    while True:
        ques = []
        print('Enter a Question : ' , end="")
        ques.append(input().strip())
        ques.append(input('enter option A : ').strip())
        ques.append(input('enter option B : ').strip())

        options = ['A', 'B']
        for i in "CDEF":
            if choose_y_n(" want to add more options (y/n)") == 'y' :
                ques.append(input("enter option " + i + " : ").strip())
                options.append(i)
            else:
                break

        ques.append(' '.join(options))
        ques.append(choose_options('Enter the option which is the answer', options))
        
        try:
            file = open(fileName, 'a')
            file.write(','.join(ques))
            file.write('\n')
        except Exception as e:
            print('error in adding question to data file: ', e)

        finally:
            file.close()
        
        if choose_y_n("would you like to add another question (y/n)") == 'n' :
            break

def new_random_questions():
    global fileName
    stop_flag = 0
    question_to_be_sent = set()
    try:
        file = open(fileName, 'r')
        questions = file.readlines()
        
        while len(question_to_be_sent) < len(questions) and len(question_to_be_sent) < 15 and stop_flag < 300:
            number = randrange(0, len(questions))
            stop_flag += 1
            question_to_be_sent.add(questions[number])
            
    except Exception as e:
        file = open(fileName, 'w')
        print('error in finding new random questions: ', e)
        

    finally:
        file.close()
        
    if stop_flag >= 100 and not ques_visited:
        print('No More Questions')
        return

    return list(question_to_be_sent)

def play_quiz():
    wrong_questions = []
    questions_correct = 0
    questions_wrong = 0
    
    ques_asked = new_random_questions()
    if not ques_asked:
        print('NO questions available')
        return
    ques_cnt = 1
    print('#########################################################')

    print('\n:):):):):) Quiz Now Starting :):):):):):)\n')
    
    for line in ques_asked:
        question = line.split(',')
        print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n')
        options = question[-2].split()
        print('Question_'+str(ques_cnt)+') ', question[0], '\n')
        for i in range(len(options)):
            print('option_'+options[i] + ' : ', question[1+i])
            
        choice = choose_options('\nChoose among options which are', options)
        if choice == question[-1][0]:
            print('\nGreat.....you are correct\n')
            questions_correct += 1
        else:
            print('\nSorry.....you are wrong\n')
            questions_wrong += 1
            wrong_questions.append(question)
        ques_cnt += 1
        print('\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n')

    print('\n\n^^^^^^^^^^^^^^^^^^^^^Quiz Over^^^^^^^^^^^^^^^^^^^\n')
    print('..........Result...........')
    print('Total Questions : ', len(ques_asked))
    print('Questions Answered Correctly = ', questions_correct)
    print('Questions Answered Incorrectly = ', questions_wrong)
    print()
    if questions_wrong > 0 :
        if choose_y_n('Would you like to see the questions you attempted incorrectly (y/n)') == 'y':
            print()
            for wrong_question in wrong_questions:
                print('Question : ', wrong_question[0])
                print('Correct Option : ', wrong_question[-1][0])
                print('\n')
    
    
                
    print('####################################################################') 


def openWindow():
    while True:
        print("\n**************************************************************************\n")
        print(':D:D:D:D:D:D:D:D  Menu :D:D:D:D:D:D:D\n')
        print("1. Add a Question")
        print('2. Play the Quiz')
        print('0. Exit')
        print('\n')
        ch = int(choose_options('Enter your Choice', ['1', '2', '0']))
        if ch == 1:
            add_a_question()
        elif ch == 2:
            play_quiz()
        elif ch==0:
            return
        
        print('************************************************************************\n')

if __name__ == '__main__':
    openWindow()
