import random

def play():
    user = input("r for rock, s for scissir, p for paper")
    comp = random.choice(['r','p','s'])
    if user == comp:
        return "tie"
    if is_win(user,comp):
        return 'you won'
    return 'you lost'



def is_win(player,opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True


print(play())