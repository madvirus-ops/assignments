import random
def computerguess(x):
    low =1 
    high = x 
    feedback = ""
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low
        feedback = input("is {} too high, too low, or correct    ".format(guess))
        if feedback =='l':
            low = guess + 1
        elif feedback == 'h':
            high = guess -1
    print("we guessed correctly")


computerguess(10000)