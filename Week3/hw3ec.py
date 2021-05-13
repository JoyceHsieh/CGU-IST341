# CS 5 Gold, hw3ec
# filename: hw3ec.py
# Name:
# problem description: List comprehensions

# this gives us functions like sin and cos...
import math as ma



# two more functions (not in the math library above)

def dbl(x):
    """Doubler!  argument: x, a number"""
    return 2*x

def sq(x):
    """Squarer!  argument: x, a number"""
    return x**2

# examples for getting used to list comprehensions...

def lc_mult(N):
    """This example accepts an integer N
       and returns a list of integers
       from 0 to N-1, **each multiplied by 2**
    """
    return [2*x for x in range(N)]

def lc_idiv(N):
    """This example accepts an integer N
       and returns a list of integers
       from 0 to N-1, **each divided by 2**
       WARNING: this is INTEGER division...!
    """
    return [float(x//2) for x in range(N)]

def lc_fdiv(N):
    """This example accepts an integer N
       and returns a list of integers
       from 0 to N-1, **each divided by 2**
       NOTE: this is floating-point division...!
    """
    return [x/2 for x in range(N)]

assert lc_mult(4) == [0, 2, 4, 6]
assert lc_idiv(4) == [0, 0, 1, 1]
assert lc_fdiv(4) == [0.0, 0.5, 1.0, 1.5]

# Here is where your functions start for the lab:

# Step 1, part 1
def unitfracs(N):
    """Be sure to improve this docstring!
    """
    
    return [x/N for x in range(N)]


def scaledfracs(low, hi, N):
    """It creates N left endpoints uniformly through the interval [low, hi)
    """

    return [low+((hi-low)/N)*x for x in range(N)]

def sqfracs(low, hi, N):
    """sqfracs is very similar to scaledfracs except that each value is squared.
    """
    l=(hi-low)/N
    return [(low+(l*x))**2 for x in range(N)]

def f_of_fracs(f, low, hi, N):
    """ the examples given above to create at least three assert statements for f_of_fracs .
    """
    l=(hi-low)/N
    return [f((low+(l*x))) for x in range(N)]


def integrate(f, low, hi, N):
    """Integrate returns an estimate of the definite integral
       of the function f (the first argument)
       with lower limit low (the second argument)
       and upper limit hi (the third argument)
       where N steps are taken (the fourth argument)

       integrate simply returns the sum of the areas of rectangles
       under f, drawn at the left endpoints of N uniform steps
       from low to hi
    """
    l=(hi-low)/N
    return [l*(sum(f_of_fracs(f, low, hi, N)))]


def c(x):
    """c is a semicircular function of radius two"""
    return (4 - x**2)**0.5

"""
Q1:
The calls to integrate(dbl, 0, 10, 4) and integrate(dbl, 0, 10, 1000), shown above, produce a little less than 100.
In a sentence explain why integrate will always underestimate the correct value of this particular integral.

Answer:
Because the integrate is trying to use rectangles to cover the whole area of a triangle. 
The more rectangles you divide in triangle, you can more close the correct area value.
But integrate still divide the area of the triangle, 
thus the value will be underestimate and never surpass the triangle area and only infinitely close it.

overestimated:
When the line is not straight but curve like we want to calculate the area of circle.
We will face the overestimated situation.
We can draw the rectangles in the circle, and we also can drwa the rectangles over the circle.
If we do the over part, our value will be always overestimated the really vaule.


"""

"""
Q2:
In[]: integrate(c, 0, 2, 2)
Out[]: [3.732050807568877]

In[]: integrate(c, 0, 2, 20)
Out[]: [3.2284648797549815]

In[]: integrate(c, 0, 2, 200)
Out[]: [3.1511769448395297]

In[]: integrate(c, 0, 2, 2000)
Out[]: [3.1425795059119643]

In[]: integrate(c, 0, 2, 20000)
Out[]: [3.1416922378179906]

In[]: integrate(c, 0, 2, 200000)
Out[]: [3.1416026404419823]

The function c is the equation to calculate pi and x is radius.
As the result, when the  N goes to infinity, the output will be infinitely close to the pi.
The pi we know is 3.14159265359, and we can see when the N is 200000, the value is 3.1416026.
It's close but not the pi, we are still looking fot the pi value.
The equation we try is to cover the circle area by the rectangles.
But it's impossible,we only can infinitely close to the correct value but not the precise value.

"""