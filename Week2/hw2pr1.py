# Name:
#
# def fac(n):
#     """Loop-based factorial function
#        Argument: a nonnegative integer, n
#        Return value: the factorial of n
#     """
#     result = 1                 # starting value - like a base case
#     for x in range(1,n+1):     # loop from 1 to n, inclusive
#         result = result * x    # update the result by mult. by x
#     return result              # notice this is AFTER the loop!

# #
# # Tests for looping factorial
# #
# print( "fac(0)   should be   1 :",  fac(0) )   
# print( "fac(5)   should be 120 :",  fac(5) ) 


#1: power(b,p)
def power(b,p):
    sum=1
    for i in range(1,p+1):
        sum= sum*b
    return sum



#2: summed(L)
def summed(L):
    result = 0
    for i in L:
        print("i is", i)
        result = result + i    # or result += e
    print(result)



#2-1: summedOdds(L)
def summedOdds(L):
    result = 0
    print(L)
    for e in L:
        if e %2==1:
            print("e is", e)
            result = result + e    # or result += e
            print("result is:", result)
    return result



 #3: untilARepeat( high )
import random

def countGuesses(hidden):
    """Uses a while loop to guess "hidden", from 0 to 99.
       Argument: hidden, a "hidden" integer from 0 to 99.
       Result: the number of guesses needed to guess hidden.
    """
    guess = random.choice(range(0, 100))     # 0 to 99, inclusive
    numguesses = 1                           # we just made one guess, above
    while guess != hidden:
        guess = random.choice(range(0, 100)) # guess again!
        # print(guess)
        numguesses += 1                      # add one to our number of guesses
    return numguesses


#3-1 
import random

def untilARepeat(N):
    L=[]
    guess1 = random.choice(range(0, Ｎ+1))
    L =L+[guess1]
    count=1
    while True:
        guess = random.choice(range(0, Ｎ+1))
        count+=1
        if  guess in L:
            L =L+[guess]
            break
        else:
            L =L+[guess]

        
    print(L,count)

#3-1-2
# def untilARepeat(N):
#     L=[]
#     guess1 = random.choice(range(0, Ｎ+1))
#     L =L+[guess1]
#     count=1
#     while True:
#         guess = random.choice(range(0, Ｎ+1))
#         L =L+[guess]
#         count+=1
#         print("this is L" , L)
#         for i in L[:-1]:
#             if i==guess:
#                 print("this is i ", i)
#                 return L,count
#                 # sys.exit()
#         # if count==10:
#         #     break
#     # print(L,count)
# a,b= untilARepeat(45)
# print(f"This final list is {a}, the count is {b}")


#3-1-3 switch 
# def untilARepeat(N):
#     L=[]
#     guess1 = random.choice(range(0, Ｎ+1))
#     L =L+[guess1]
#     count=1
#     switch=False
#     while True:
#         guess = random.choice(range(0, Ｎ+1))
#         L =L+[guess]
#         count+=1
#         print("this is L" , L)
#         for i in L[:-1]:
#             if i==guess:
#                 print("this is i ", i)
#                 switch=True
#                 #return L,count
#                 # sys.exit()
#         if count==True:
#             break
#     # print(L,count)



#3-1-4 Birthday date
import random
def rand_date():
    """returns a random date (a string)
    in month/day from (no leap year...)"""
    DiM=[0,31,28,31,30,31,30,31,31,30,31,30,31]
    month=random.choice(range(1,12+1))
    day= random.choice(range(1,DiM[month]+1))
    randomdate= str(month)+ "/" + str(day)

    return randomdate

import random

def untildate():
    L=[]
    guess1 = rand_date()
    L =L+[guess1]
    count=1
    while True:
        guess = rand_date()
        count+=1
        if  guess in L:
            L =L+[guess]
            break
        else:
            L =L+[guess]

        
    print(L,count)