#!/usr/local/bin/python3
from EulerUtilities import *

def P(s,N):
    f1=1
    for i in range(1,s+1):
        f1=lcm(f1,i)
    f2=lcm(f1,(s+1))
    #print(f1,f2)
    return (N-2)//f1 - (N-2)//f2
    
print(P(3,14))
print(P(6,10**6))

result=0

for i in range(1,32):
    inc=P(i,4**i)
    #print(i,inc)
    result=result+inc
    
print('result=',result)
    