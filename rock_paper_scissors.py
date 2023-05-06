import random



def rps():  
    user = input("Pick r for rock, s for scissors and p for paper: ")
    comp = random.choice(["r", "s", "p"])
    print(f"You pick {user} and computer pick {comp}")
    if user == comp:
        return print("tie")
    elif isWin(user,comp):
        return print("You won against computer!!!")
    else:
        return print("Computer won against you :(")

    
def isWin(user,comp):
    # r>s, p>r , s>p
    if (user == "r" and comp == "s" )or(user == "p" and comp == "r")or(user == "s" and comp == "p") :
        return True
rps()