def new_game():
    guesses = []
    correct = 0
    question = 1

    for key in questions:
        print('------------')
        print(key)
        for i in options[question-1]:
            print(i)
        guess = input('enter a,b or c:   ').upper()
        guesses.append(guess)
        correct += check_answer(questions.get(key),guess)
        question+=1
    display_score(correct, guesses)


def check_answer(answer,guess):
   if answer == guess:
       print('correct')
       return 1
   else:
       print('wrong')
       return 0


def display_score(correct,guesses):
    print('---------')
    print('results')
    print('---------')
    print('answers: ',end=' ')
    for i in questions:
        print(questions.get(i), end=' ')
    print()
    print('your guess: ', end=' ')
    for i in guesses:
        print(i, end='')
    print()

    score = (correct/len(questions)) * 100
    print(f"Your score is {score} %")
def play_again():
    response = input('you want play again (yes/no):').upper()
    if response=='YES':
        return True
    else:
        return False


questions = {
    'who created python': 'A',
    'what year was it created': 'C',
    'python name was gotten from what': 'C',
    'is the earth round?': 'A',
    'who is the president of nigeria':'B'
}
options = [
    ['A. guiddo van rossum', 'B. elon muskertee', 'C. mark nsukkabread'],
    ['A. 1989', 'B. 2000', 'C. 1991'],
    ['A. a snake', 'B. a food', 'C. a show'],
    ['A.  true', 'B.False', 'C.bighead'],
    ['A. bubu','B. obj','C.tinubu']
]

new_game()

while play_again():
    new_game()
print('bye bighead')