#import time
import random
import os 

# CREDIT for pi code: 
# Dan Anderson - http://blog.recursiveprocess.com/2013/03/14/calculate-pi-with-python/

from decimal import *

def factorial(n):
    return 1 if n<1 else n * factorial(n-1)

def chudnovskyBig(n): # http://en.wikipedia.org/wiki/Chudnovsky_algorithm
    pi = Decimal(0)
    k = 0
    while k < n:
        pi += (Decimal(-1)**k)*(Decimal(factorial(6*k))/((factorial(k)**3)*(factorial(3*k)))* (13591409+545140134*k)/(640320**(3*k)))
        k += 1
    pi = pi * Decimal(10005).sqrt()/4270934400
    pi = pi**(-1)
    return pi

def stress():
    ran = False
    temp = 0
    #start = time.time()
    n = random.randint(2500,3500)
    #print "RUNNING for %d" % n 
    getcontext().prec = n
    temp = chudnovskyBig(10)
    return True
