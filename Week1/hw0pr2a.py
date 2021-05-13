
import random

def rps():
    """ this plays a game of rock-paper-scissors
        (or a variant of that game)
        inputs: none        (prompted text doesn't count as an argument)
        outputs: none       (printing doesn't count as a result)
    """
    
    u={"rock","paper","scissors"}
    while True:
	    user=input("Please, choose your weapon: ").lower()
	    if user in u:
		    break
	    else:
		    print("Enter error!! Please, try again")
    print("we can start the gmae!")

    com=random.choice(["rock","paper","scissors" ])

    print('The user (you)   chose', user)
    print('The computer (I) chose', com)
    print()

    if com == "rock":
        if user == "rock":
            print("Tie, Try again?")
        elif user == "paper":
            print("User(you) win!")
        else:
            print("Computer win, Better luck next time!")
    elif com == "paper":
        if user == "rock":
            print("Computer win, Better luck next time!")
        elif user == "paper":
            print("Tie, Try again?")
        else:
            print("User(you) win!")
    else:  #scissors
        if user == "rock":
            print("User(you) win!")
        elif user == "paper":
            print("Computer wim, Better luck next time!")
        else:
            print("Tie, Try again?")
    print()
