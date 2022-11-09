#!/usr/local/bin/python3
from EulerUtilities import *


def test(N):
    current=[i for i in range(1,N+1)]
    c=0
    while len(current)>1:
        #print(current)
        c+=1
        if c%2==1:
            current=current[1::2]
        if c%2==0:
            current=list(reversed(current[-2:-len(current)-1:-2]))
    return current[0]
    
''''
N=1
low=2**N
high=low*2
for i in range(low,high):
    print(i,test(i))
 '''  
#observations    
# e(2n)=e(2n+1).  
# e(2n)=2*(n+1-e(n))

# e(2^(2k-1))=e(2^(2k))

# e(2^(2k-1)) ~ e(2^(2k)-1) first part second part same; first part is e(2^(2k-2)) ~ e(2^(2k-1)-1) shift by 2^(2k-2)
# e(2^(2k)) ~ e(2^(2k+1)-1) first part same as e(2^(2k-1)) ~ e(2^(2k)-1) second part is first part shifted by 2^(2k-1) 
                           


def S(N): #sum 1 ~~ 2**e-1.  S(e)-S(e-1)=info(e)[2]
    if N==1:
        return 1
    if N==2:
        return 5
    if N==3:
        return 17
    s=17        
    for i in range(3,N):
        s+=partialSum(i)[2]
        #print(i,pairsum,pair,pairsum*pair)
    return s
    
    
def partialSum(N): #sum 2**N ~ 2**(N+1)-1
    if N==1:
        return (1,4,4)
    if N==2:
        return (2,6,12)
    pair=2**(N-1)  
    if N%2==0:
        t=N//2+1
        pairsum=int(2+(4**(t)-4)//3)
    elif N%2==1:
        t=(N-1)//2+1
        pairsum=int(2+(4**(t)-4)//3+2**N)      
    return (pair,pairsum,pair*pairsum)
    

def intervalSum(x,y):  #inclusive , x is power of 2
    if x==2 and y==3:
        return 4
    if x==2 and y==2:
        return 2
    e=int(math.log2(x)) 
    mid=2**e+2**(e-1)-1
    if y<=mid:
        if e%2==1:
            return intervalSum(x//2,y-x+x//2)+(2**(e-1))*(y-x+1)
        elif e%2==0:
            return intervalSum(x//2,y-x+x//2)       
    elif y>mid:
        if e%2==1:
            return partialSum(e-1)[2]+(2**(e-1))*(2**(e-1))+intervalSum(x,y-2**(e-1))
        elif e%2==0:
            return partialSum(e-1)[2]+intervalSum(x,y-2**(e-1))+2**(e-1)*(y-2**(e-1)-x+1)


def calc(x): #inclusive
    e=int(math.log2(x))
    s=S(e) #sum 1 ~~ 2**e-1.  S(e)-S(e-1)=info(e)[2]
    return s+intervalSum(2**e,x)
    
print(calc(10**18)%987654321)
    


 
