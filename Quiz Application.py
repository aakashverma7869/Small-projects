from random import randrange

questions = []

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
    while True:
        ques = {}
        print('Enter a Question : ' , end="")
        ques['question'] = input()
        ques['option_A'] = input('enter option A : ')
        ques['option_B'] = input('enter option B : ')

        options = ['A', 'B']
        for i in "CDEF":
            if choose_y_n(" want to add more options (y/n)") == 'y' :
                ques['option_'+i] = input("enter option " + i + " : ")
                options.append(i)
            else:
                break

        ques['options'] = options
        ques['answer'] = choose_options('Enter the option which is the answer', options)

        questions.append(ques)
        if choose_y_n("would you like to add another question (y/n)") == 'n' :
            break


def new_random_questions():
    ques_visited = []
    cnt = 0
    stop_flag = 0
    while len(ques_visited) < len(questions) and cnt < 15 and stop_flag < 100:
        number = randrange(0, len(questions))
        stop_flag += 1
        if number in ques_visited:
            continue
        ques_visited.append(number)
        cnt += 1

    if stop_flag >= 100 and not ques_visited:
        print('No More Questions')
        return

    return ques_visited

    

def play_quiz():
    wrong_questions = []
    questions_correct = 0
    questions_wrong = 0
    
    ques_asked = new_random_questions()
    if not ques_asked:
        print('NO questions available')
        return
    ques_cnt = 0
    print('#########################################################')

    print('\n:):):):):) Quiz Now Starting :):):):):):)\n')

    for q_no in ques_asked:
        for u, v in questions[q_no].items():
            if u == 'answer' or u == 'options':
                continue
            elif u == 'question':
                print(u.upper(), ques_cnt+1, ' : ', v, '\n')
            else:
                print(u.upper(),  ' : ', v)

        choice = choose_options('\nChoose among options which are', questions[q_no]['options'])
        if choice == questions[q_no]['answer']:
            print('\nGreat.....you are correct\n')
            questions_correct += 1
        else:
            print('\nSorry.....you are wrong\n')
            questions_wrong += 1
            wrong_questions.append(questions[q_no])
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
                print('Question : ', wrong_question['question'])
                print('Correct Option : ', wrong_question['answer'])
                print('\n')
    
    
                
    print('####################################################################') 



def openWindow():
    while True:
        print("\n**************************************************************************\n")
        print(':D:D:D:D:D:D:D:D  Menu :D:D:D:D:D:D:D\n')
        print("1. Add a Question")
        print('2. Play the Quiz')
        print('0. Exit')
        print('\nEnter your Choice')
        ch = int(input())
        if ch == 1:
            add_a_question()
        elif ch == 2:
            play_quiz()
        elif ch==0:
            return
        
        print('************************************************************************\n')

if __name__ == '__main__':
    openWindow()
