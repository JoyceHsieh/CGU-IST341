# CS5, Lab1 part 2
# Filename: hw1pr2.py
# Name: 
# Problem description: First few functions!

import math


def dbl(x):
    """Result: dbl returns twice its argument
       Argument x: a number (int or float)
       Spam is great, and dbl("spam") is better!
    """
    return 2*x

def tpl(x):
    """Return value: tpl returns thrice its argument
       Argument x: a number (int or float)
    """
    return 3*x

def sq(x):
    """Return value: tpl return the square of its argument
       Argument x: a number (int or float)
    """
    return x**x

def interp(x, y ,z):
    """Return value: Return the floating-point value that is fraction of the way between low and hi.
       Argument x: a number (float)
    """
    return (y-x)*z+x


def checkends(s):
    """Return value: returns True if the first character in s is 
       the same as the last character in s. It returns False otherwise. 
       Argument x: The string 
    """
    if s[0] == s[-1]:
        return True
    else:
        return False


def flipside(s):
    """Return value: accepts a string s and returns a string 
    whose first half is s's second half and whose second half is s's first half. 
    If len(s) (the length of s) is odd, the "first half" of s is considered 
    to have one fewer character than the second half.
       Argument x: The string 
    """
    x=len(s)//2   # x=int(len(s)/2)
    return s[x:]+s[0:x]

def convertFromSeconds(s):
    days = s // (24*60*60)  # Number of days
    s = s % (24*60*60)      # The leftover
    hours = s // (60*60)
    s = s % (60*60)
    minutes = s//60
    seconds = s%60
    return [days, hours, minutes, seconds]

