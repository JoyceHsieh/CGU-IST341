import random
import time


def dart():
    """ throws one dart between (-1,-1) and (1,1)
          returns True if it lands in the unit circle; otherwise, False
    """
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    
    if x**2 + y**2 < 1:
        return True  # HIT (within the unit circle)
    else:
        return False # missed (landed in one of the corners)

LC=[ dart() for x in range(42) ]

#Q1
def forpi(n):
    """ throws N darts, estimating pi """
    pi = 4.0     # a suitably poor initial estimate
    throws = 0  # no throws yet 
    hits = 0    # no "hits" yet  (hits ~ in the circle)
    for i in range(1, n+1):
        dart()
        if dart()==True: 
            throws +=1
            hits +=1
            pi= 4* hits/ throws
            time.sleep(0.02)
            print(hits, "hits out  of", throws ,"so that pi is", pi )
        else:
            throws +=1
            hits +=0
            pi= 4* hits/ throws
            time.sleep(0.02)
            print(hits, "hits out  of", throws,"so  that pi is", pi )
    
    return pi


#Q2
import math

x=math.pi
def whilepi(error):
    x=math.pi
    throws = 0  # no throws yet 
    hits = 0 
    pi = 4.0
    while True:
        dart()
        if dart()==True:
            throws +=1
            hits +=1
            pi= 4* hits/ throws
            time.sleep(0.02)
            print(hits, "hits out  of", throws ,"so that pi is", pi )
            if abs(x-pi)<=error:
                break
        else:
            throws +=1
            hits +=0
            pi= 4* hits/ throws
            time.sleep(0.02)
            print(hits, "hits out  of", throws,"so  that pi is", pi )
            if abs(x-pi)<=error:
                break
    return throws