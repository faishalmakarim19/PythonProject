import random

def play():
    print("'r' for rock, 'p' for paper, and 's' for scissor")
    user1 = input("What's your choice ?")
    comp = random.choice(['p','s','r'])
    
    print(f"the computer choose {comp}")
    
    if (user1 == comp):
        print("It's a Tie")    
    elif isWin(user1, comp):
        print("You Win")
    else:
        print("You Lost")
    
def isWin(player,opponent):
    if (player=='r' and opponent=='s') or (player=='s' and opponent=='p') or (player=='p' and opponent=='r'):
        return True
    
    return False
    
play()
    