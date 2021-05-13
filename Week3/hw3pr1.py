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


# #3-1 
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
    return count

# LC = [untilARepeat(365) for i in range(100)]

# import itertools
# LC = [untilARepeat(365) for i in range(100)]
# flatten = itertools.chain.from_iterable
# L=list(flatten(LC))
# avg=sum(L)/len(L)
# Ma=max(L)
# Mi=min(L)
# 42 in L
# L.count(2)
# 1 in L
# 142 in L


import random

def rs():
    """ one random step """
    return random.choice( [-1, 1] )

def rwalk(radius):
    """ random walk between -radius and +radius  (starting at 0 by deafult)  """
    totalsteps = 0              # starting value of totalsteps (_not_ final value!)
    start = 0                   # start location (_not_ the total # of steps)

    while True:                 # run "forever"  (really, until a return or break)
        if start == -radius or start == radius:   
            return totalsteps   # phew!  return totalsteps  (stops the while loop)

        start = start + rs()
        totalsteps += 1         # addn totalsteps 1    (for all who miss Hmmm :-)

        # print("start:", start)  # to see what's happening / debugging
    return totalsteps
    # it can never get here!

LC = [ rwalk(5) for i in range(100) ]