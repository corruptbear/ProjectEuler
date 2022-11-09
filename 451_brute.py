#!/usr/local/bin/python3
from EulerUtilities import *
import itertools
import math



def qr(n):
    for i in range(2,n//2+1):
        if i**2 % n == 1:
            return i
    return 1
    

        

def decompAll(N):
    D=[]
    for i in range(N+1):
        D.append({})
    P=sift(N)
    for p in P:
        for i in range(1,N//p+1):
            current=i*p
            c=0
            while current%p==0:
                c+=1
                current=current//p
            D[i*p][p]=c 
    return D
    
    
def addDict(d1,d2):
    D={}
    for k in d1.keys():
        D[k]=d1[k]
    for k in d2.keys():
        if not k in D.keys():
            D[k]=d2[k]
        else:
            D[k]+=d2[k]       
    return D
    
    
def addDictOdd(d1,d2):
    D={}
    for k in d1.keys():
        D[k]=d1[k]
    for k in d2.keys():
        D[k]=d2[k]
    return D

def addDictEven(d1,d2):
    D={}
    for k in d1.keys():
        D[k]=d1[k]
    for k in d2.keys():
        if k==2:
            D[k]+=d2[k]
        else:
            D[k]=d2[k]
    return D
    

    

    
def isSquare(x):
    return x==int(math.sqrt(x))**2
    
    

            
            
def factors2(d,lim):
    L=[[k**i for i in range(d[k]+1)] for k in d.keys()] 
    c=L[-1] 
    length=len(L)
    for l in L[-2:-length-1:-1]:
        c=list(filter(lambda y:y<=lim,[x[0]*x[1] for x in itertools.product(c,l)]))
    return sorted(c)
        
       

N=10**5 #change here
D=decompAll(N)

A=[1]*(2*N+1)
upper=2*N
for i in range(3,N):
    d1=D[i-1]
    d2=D[i+1]
   
    d=addDict(d1,d2)
       
    f=factors2(d,upper)
    #f=factors(d)
    k=binary(f,2*i)
    
    for factor in f[k:]: 
        #if factor>upper:
        #    break
        #i**2 = 1 mod factor
        if factor-i>A[factor]:
            A[factor]=factor-i  
       
print(sum(A[3:]))


#1177096 14223825129

#75 134.35 181.53





    
    


    
    
            
