#!/usr/local/bin/python3
from EulerUtilities import *
import math

def fib(n,N):
    k=0
    s=0
    f1,f2=0,1
    while k<=n:
        if k%N==-2%N:
            s+=f2/2**k           
        f1,f2=f2,f1+f2
        k+=1
        
    print(s/4)

fib(10000,5)




        