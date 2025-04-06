import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissor. \nChoose: ")
    computer = random.choice(['r', 'p', 's'])
    print(f"Computer choose: {computer}")

    if user == computer:
        return "It's a tie"
    
    if is_win(computer, user):
        return "You Win!"

    return 'You Lost!'
    

def is_win(computer, user):

    if (user == "r" and computer == 's') or (user == "p" and computer == 'r' ) or (user == "s" and computer == 'p'):
        return True

print(play())