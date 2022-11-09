#!/usr/local/bin/python3
import math

def K(n):
    return n*(n+2)
    
def isSquare(n):
    return int(math.sqrt(n))**2==n
    

def isTriangle(n):
    t=2*n
    return isSquare(4*t+1)    
    
#1 3 10 22 63 133 372 780 2173 4551 12670 26530

m=3
n=1

count=0
L=[1]
while count<50:
    L.append((5*n+2*m-1))
    if abs(5*n-2*m)>1:
        L.append(abs(5*n-2*m)-1)
    m,n=3*m+8*n,3*n+m
    count+=1
L=sorted(L)
print(L)
print('sum is',sum(L[:40]))


   
