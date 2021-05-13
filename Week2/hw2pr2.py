
import random  

def rs():
    """rs chooses a random step and returns it.
       Note that a call to rs() requires parentheses.
       Arguments: none at all!
    """
    return random.choice([-1, 1])


import time

def rwpos(start, nsteps):
    """ rwpos models a random walker that
        * starts at the int argument, start
        * takes the int # of steps, nsteps

        rwpos returns the final position of the walker.
    """
    time.sleep(0.1)
    print('location is', start)
    if nsteps == 0:
        return start
    else:
        newpos = start + rs()  # take one step
        return rwpos(newpos, nsteps - 1)


import time
import sys

def rwsteps(start, low, high):
    """ rwsteps models a random walker that
        * starts at the int argument, start  
        * goes UNTIL reaching low or high
          (low will always be less than high)

        rwsteps returns the number of steps the
        walker needed to reach the lower or upper bound
    """
    sys.stdout.flush()   # forces Python to print everything _now_
    time.sleep(0.1)      # and then sleep for 0.1 seconds
    
    print("low, high, start are", low, high, start)   # show all of the arguments, as numbers...
    print('Netflix|'+"♥"*(start-low) + ' (≧д≦ヾ)' + "♥"*(high-start)+ '|Disney+')     # this is the beginning of a "terminal-graphics" wandering...
    time.sleep(0.05)

    if start <= low or start >= high:
        return start

    else:
        newpos = start + rs()   # take one step, from start to newpos!
        return 1 + rwsteps(newpos, low, high)



#_____1 VS 2_____
import random  
def run():
    return random.choice([1, 2, 3])

def zrun():
    return random.choice([1,2])

def race(w1, w2, z, end):
    """ race models are two-person are chased by Zombie 
    and running to the Shelter as soon as possible
    w1,w2 are the person start point
    z is Zombiestart point
    when the person who get into the Shelter or catch by the Zombie
    the game is over.

    """
    sys.stdout.flush()   # forces Python to print everything _now_
    time.sleep(0.1)      # and then sleep for 0.1 seconds

    print("w1, w2, start are", w1, w2, z, end) 
    print("☆"*(z) +'🧟'+"☆"*(w1-z) + '🏃‍♀' + "☆"*(end-w1)+ 'Shelter')  
    print("☆"*(z) +'🧟'+"☆"*(w2-z) + '🏃‍♂' + "☆"*(end-w2)+ 'Shelter')  

    if w1>=end or w2>=end:
        return 1
    elif z>=w1 or z>=w2:
        return 1
    else:
        w1 += run()
        w2 += run()
        z += zrun()
        return 1+ race(w1, w2, z, end)


#Doodle
# import random  
# def move():
#     return random.choice([-1,1])

# def doodle(start, long):
#     """ doodle model is the doodle will randmo go right or left one step
#     each time, and after ten times, the model will return the number
#     which mean the star eaten by doodle

#     """

#     sys.stdout.flush()   # forces Python to print everything _now_
#     time.sleep(0.1)      # and then sleep for 0.1 seconds

#     print("Start at", start, long) 
#     print("|"+"☆"*(start) +'😋'+"☆"*(long-start)+"|")
#     count=0
#     for i in range(1,10):
#         n=move()
#         #print("Move:", n, start) 
#         if n>=0:
#             print("|"+"☆"*(start+abs(n))+'😋'+"☆"*(long-(start+abs(n)))+"|")
#             start= start+1
#             count+=1
#         else:
#             print("|"+"☆"*(start-abs(n))+'😋'+"☆"*(long-(start-abs(n)))+"|")
#             start= start-1
#             count+=1
#     return count
