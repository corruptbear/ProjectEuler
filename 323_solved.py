#!/usr/local/bin/python3
from EulerUtilities import *
import math


def C32(n):
    return math.factorial(32)//(math.factorial(n)*math.factorial(32-n))
    

def P(N):
    if N==1:
        return 1/2**32
    result=0
    for m in range(1,33):
        result+=C32(m)/(2**((N-1)*m))*(1-0.5**(N-1))**(32-m)/2**m
    return result
    

U=1000
result=0
for i in range(1,U+1):
    #print(P(i),i)
    result+=P(i)*i    
    
result=format(result, '.10f')
print(result)
    
        
    
    




    
    
    
    