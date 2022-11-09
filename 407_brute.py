#!/usr/local/bin/python3
from EulerUtilities import *
import itertools
import math

def addDict(d1,d2):
    D={}
    for k in d1.keys():
        D[k]=d1[k]
    for k in d2.keys():
        D[k]=d2[k]
    return D
    
    
def factors2(d,lim):
    L=[[k**i for i in range(d[k]+1)] for k in d.keys()] 
    c=L[-1] 
    length=len(L)
    for l in L[-2:-length-1:-1]:
        c=list(filter(lambda y:y<=lim,[x[0]*x[1] for x in itertools.product(c,l)]))
    return sorted(c)
    
    
N=10**7 #change here
D=decompAll(N)

A=[1]*(N+1)
A[1]=0

upper=N

for i in range(3,N):
    d1=D[i]
    d2=D[i-1]
   
    d=addDict(d1,d2)
       
    f=factors2(d,upper)
    #f=factors(d)
    k=binary(f,i)
    
    for factor in f[k:]: 
        #if factor>upper:
        #    break
        #i**2 = 1 mod factor
        if i>A[factor] and i<factor:
            A[factor]=i  
print(sum(A[1:]))