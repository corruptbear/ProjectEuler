#!/usr/local/bin/python3
from EulerUtilities import *
import math

def isSquare(n):
    return n==(math.floor(math.sqrt(n)))**2

def lattice(a,b,c,d):
    area=(a+c)*(b+d)/2
    nBoundaryPoints=gcd(b,c)+gcd(a,b)+gcd(c,d)+gcd(a,d)
    return (area+1)-nBoundaryPoints/2
    
def isFirst(a,b,c,d):
    if (a,b,c,d)>(b,c,d,a) or (a,b,c,d)>(b,c,d,a) or (a,b,c,d)>(c,d,a,b) or (a,b,c,d)>(d,a,b,c):
        return False
    return True
    
def N(a,b,c,d):
    return len(set([(a,b,c,d),(b,c,d,a),(c,d,a,b),(d,a,b,c)]))

count=0
m=100
for a in range(1,m+1):
    for b in range(a,m+1):
        for c in range(a,m+1):
            for d in range(a,m+1):
                if isFirst(a,b,c,d) and isSquare(lattice(a,b,c,d)):                    
                    count+=N(a,b,c,d)

print(count)
                    
                