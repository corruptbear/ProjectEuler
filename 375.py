#!/usr/local/bin/python3
import math
from EulerUtilities import *

n=50515093 #5807*8699
s0=290797 
#S(n)=S(n+6308948) starting cycle from S1=629527

s=s0
c=0
L=[s0]
for i in range(1,11):
    s=s**2 % n
    L.append(s)
 
m=0   
for i in range(1,11):
    for j in range(i,11):
        m+=min(L[i:j+1])
print(m)
    

    
    

    

    
    
