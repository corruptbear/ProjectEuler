#!/usr/local/bin/python3
import math
from EulerUtilities import *

def digits(n,base):
    num=int(n)
    L=[]
    while True:
        d=num//int(base)
        r=num-d*int(base)
        L.append(int(r))
        num=d
        if num==0:
            break
    return list(reversed(L))
    
def evaluate(L,base):
    n=0
    exp=0
    for i in reversed(L):
        n+=i*base**exp
        exp+=1
    return n
    
def G(n):
    g=n
    k=2
    while True:
        d=digits(g,k)
        print(d,k,g)
        g=evaluate(d,k+1)-1  
        print(d,k,g)     
        if g==0:
            break
        k+=1
    print(k-1)
    
def G2(n):
    g=n
    k=2
    while True:
        d=digits(g,k)
        print(d,k)
        last=d[-1]
        if last!=0:
            d[-1]=0
            g=evaluate(d,k+last+1)-1
            k+=last
            if g<=0:
                print(k-2)
                break
            k+=1
        if last==0:
            g=evaluate(digits(g,k),k+1)-1 
            if g==0:
                print(k-1)
                break
            k+=1   
                  


def r2(k):
    c=1562500
    if k<=1562509:
        return 2**k % 10**9
    else:
        return (512 * 2**((k-9) % 1562500))%10**9

def G4(n):
    g=n
    k=2
    while True:
        d=digits(g,k)
        if len(d)==3:
            print(d)
            break
        g=evaluate(d,k+1)-1      
        if g==0:
            break
        k+=1
        
    for i in range(0,d[0]+1):
        k=(k%10**9)*r2(k%10**9)%10**9       
    return k-3

#G2(8)            
s=2517
for i in range(8,16):
    s+=G4(i)

print(s%10**9)

