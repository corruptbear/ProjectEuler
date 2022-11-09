#!/usr/local/bin/python3
from EulerUtilities import *
import itertools
import math
import heapq

N=500500
modulo=500500507
s=sift(10**7)
P=s[:N]

#priority queue solution
h=[]
for p in P:
    heapq.heappush(h,p)

result=1
for i in range(N):
    small=heapq.heappop(h)
    value=small**2
    heapq.heappush(h,value)  
    result=(result*small) % modulo
print(result) 
    

'''
A=[0]*len(P)
A[0]=1
l=1
val=[p for p in P]
val[0]=4


for i in range(N):
    #print(A)
    if i==N-1:
        break
    
    b=int(math.ceil((math.sqrt(l))))
    sub=val[:b]
    v=min(sub)
    pos=sub.index(v)
    #print(i,pos,l,P[pos]**2,P[l])

    
    if v>val[l]:
         pos=l
         l+=1
    A[pos]+=1
    val[pos]=pow(P[pos],2**A[pos])

result=1
for k in range(l):
    result=result*pow(P[k],2**A[k]-1,modulo)%modulo
    
print(result)
'''

    


        
    
        

        

            
        
    
        
    
    

