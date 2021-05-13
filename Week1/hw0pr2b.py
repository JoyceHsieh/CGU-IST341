import time
import random
import math
import sys
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


username=input("Please, enter your name:")

def print_one_by_one(text):
    sys.stdout.write("\r " + " " * 60 + "\r") # /r 光标回到行首
    sys.stdout.flush() #把缓冲区全部输出
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.2)

def restart():
    print( "Welcome,", username, " to the Alice in Borderland.")
    time.sleep(2)
    while True:
        print("Are you a risk-taker?")
        a=input("Yes or No:").title()
        if a=="Yes":
            print("Great! Now I will cover your eyes")
            time.sleep(2)
            print("lead you into the dark room....")
            time.sleep(2)
            print("If you succeed to complete all challenges, the one-piece will be waiting for you in the end.!!")
            time.sleep(3)
            print("If you failed, you may be trapped in the dark forever..... ")
            time.sleep(2)
            print("Are you ready? We start in 5 seconds ")
            time.sleep(2)
            print("5")
            time.sleep(1)
            print("4")
            time.sleep(1)
            print("3")
            time.sleep(1)
            print("2")
            time.sleep(1)
            print("1")
            break
        else:
            print("We only want the brave person")
            time.sleep(2)
            print("I won't think you can survive this....")
            time.sleep(2)
            print("I ask you again!")
    print()


    #SpadesRoom
    s={"soccer", "cricket", "basketball", "hockey", "tennis", "volleyball", "table tennis", "baseball","rugby","golf"}
    time.sleep(3)
    print ("Welcome, Here is the SpadesRoom")
    time.sleep(2)
    print("In this room, you need to know top 10 popular sports in the world.")
    time.sleep(2)
    while True:
        b=input("Please, enter one sport that is in the top 10 popular sports ranking 2020:").lower()
        if b in s:
            print("Great, you can go to the next room.")
            break
        elif b=="boxing" or "running":
            print("Unfortunately, that sport was popular in 2019.")
            time.sleep(2)
            print("But you get the right direction.")
            time.sleep(2)
            print("Pleas, try again.")
        else:
            print("I never hread that sport, please choose another one?")
            time.sleep(2)
    print()



    #HeartRoom
    time.sleep(3)
    print("Welcome to the HeartRoom")
    time.sleep(2)
    print("In this room you need to guess what I am thinking.")
    time.sleep(2)
    print("I will thoghu a number from 0 to 10")
    time.sleep(2)
    print("You need to tell the number that difference plus or minus 2")
    time.sleep(2)
    print("Let's start!!")
    time.sleep(2)
    while True:
        c=int(input("Please, guess a number from 0 to 10:"))
        com=int(random.randint(0,10))
        time.sleep(2)
        print("You guess", c)
        time.sleep(2)
        print("The answer is ", com)
        x=abs(c-com)
        time.sleep(2)
        if x<=2:
            print("Congratulations! You can go to the next room.")
            break
        else:
            print("The difference is over than 2, try again")
    print()

    #DiamondsRoom
    time.sleep(3)
    print("Welcom to the DiamondsRoom")
    time.sleep(2)
    print("In this room, you need to answer the quiz.")
    time.sleep(2)
    print("Are you ready?")
    time.sleep(2)

    while True:
        d=input("Please, enter a sentence which including all 26 letters:").lower()
        if d=="the quick brown fox jumps over the lazy dog":
            print(" ")
            break
        elif d=="the quick brown fox jumps over the lazy dog.":
            print(" ")
            break
        elif d=="The quick brown fox jumps over the lazy dog":
            print(" ")
            break
        elif d=="The quick brown fox jumps over the lazy dog.":
            print(" ")
            break
        else:
            print("Oopes, wrong answer. Please, try again.")

    time.sleep(2)		
    print("Well done. You are a brilliant person")
    time.sleep(2)
    print("I believe you can complete the misstion. Good luck")
    print()

    #ClubsRoom
    time.sleep(3)
    print("Welcom to the ClubsRoom, and this is the last challenge.")
    time.sleep(2)
    print("if you succeed, the one-piece is waiting for you!")
    time.sleep(2)
    print("or you will lose in the dark forever.")

    time.sleep(2)
    print("Are you ready to face the challenge")
    time.sleep(2)
    print("Now you can see the three doors, Left, Right or Center.")
    time.sleep(2)
    print("Only one door will bring you to the treasure")
    time.sleep(2)
    print("Which door you will go?")
    time.sleep(2)

    e=input("Left, Right or Center:").title()
    if e== "Left":
        time.sleep(2)
        print_one_by_one("..........")
        time.sleep(2)
        print("This your answer.....")
        time.sleep(2)
        print("Just keep going forward")
        time.sleep(2)
        print_one_by_one("I afarid that you will never see the sky again......")
        print()
        print()
        print()
        time.sleep(2)
        print(Fore.RED + "Game over!!!")
        print()
        return "over"
    elif e== "Center":
        time.sleep(2)
        print_one_by_one("Pleas, keep going....")
        time.sleep(2)
        print("You will see your treasure at the end of the dark!")
        time.sleep(2)
        print("You are really brilliant, I hope you see you soon!!")
        print()
        print()
        print()
        time.sleep(3)
        print_one_by_one("Congratulations! GAME CLEAR!")
        return "over"
    else:
        time.sleep(2)
        print("I will see yoou soon.....")
        print()
        return "Again"
        

result=restart()
while True:
    if result=="over":
        break
    else:
        result=restart()

    




