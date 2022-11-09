#!/usr/local/bin/python3
import math
from decimal import Decimal

def comb(N,k):
    return Decimal(int(math.factorial(N))//int((math.factorial(k)*math.factorial(N-k))))
    

def unchange(M,pFlip):
    a=Decimal(0)
    for i in range(0,M+1,2):
        a+=Decimal(((1-pFlip)**(M-i))*(pFlip**i))*comb(M,i)
    return a

#flip probability per-turn of the K-th element in N-array    
def f(N,k): 
    return Decimal((2*k*(N-k+1)-1)/(N*N))

#correct but slow        
def calc(N,M):
    c=Decimal(0)
    for k in range(1,N+1):
        inc=unchange(M,f(N,k))
        #print(k,inc)
        c+=inc
    return c
    
#faster but still not enough    
def calc2(N,M):
    result=Decimal(0)
    for i in range(0,M+1,2):
        #print(i)
        multiplier=comb(M,i)
        c=0
        div=N*N
        for k in range(1,N//2+1): #symmetry, for even value only
            z=(2*k*(N-k+1)-1)/div
            c+=((1-z)**(M-i))*(z**i)       
        result+=Decimal(2*c)*multiplier       
    return result 
    

#for i in range(1,10**10+1):
#    if 4000*f(10**10,i)>10: #3-3751408, 10-12515665
#        print(i)
#        print(unchange(4000,f(10**10,i)))
#        break


    





    
    
    