#!/usr/local/bin/python3
from EulerUtilities import *

    
    
    
def isRoot(x,prime,L):
    n=prime-1  
    current=n
    decomp={}
    for k in L:
        if current==1:
            break
        if k>math.sqrt(current):
            decomp[current]=1
            if pow(x,n//current,prime)==1:
                return False
            break
        if current%k==0:
            decomp[k]=1
            if pow(x,n//k,prime)==1:
                return False
            current=current//k
            while current>1:
                if current%k==0:
                    decomp[k]=decomp[k]+1
                    current=current//k
                else:
                    break
    return True
    
    


P=sift(10**4)
c=0
s=0
for p in P[1:]: #for p>2
    k=tonelli(5, p)
    if k<0:
        continue
    if (k**2-5)%(4*p)==0:
        k=int((1+k)//2)
    elif ((p-k)**2-5)%(4*p)==0:
        k=int((1+(p-k))//2)
    if isRoot(k,p,P) or isRoot(p+1-k,p,P):
        c+=1
        s+=p

print(c+1,s+5) #compensate for 5
            
         