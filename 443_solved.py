#!/usr/local/bin/python3
from EulerUtilities import *

n,v=4,13
while n<10**4:
    n=n+1
    inc=gcd(n,v)
    v=v+inc
    if inc!=1:
        print('n-1=',n-1,'g(n-1)=',v-inc,'gcd(n,g(n-1))=',inc,'n=',n,'g(n)=',v)

def search_next(a,b,interval):
    n,v=a,b
    #explore phase
    while n-a<interval:
        n=n+1
        v=v+gcd(n,v)
    #exploration finished. jump to the next pair
    n=v-n-1
    v=3*n
    return (n,v)

def calc(a,b,interval,target):
    n,v=a,b
    while n-a<interval:
        n=n+1
        v=v+gcd(n,v)
    return target-n+v
    
a=405641
b=1216923
interval=5000000
target=10**15

while a*2<target:
    (a,b)=search_next(a,b,interval) 
    print(a,b,'interval=',interval)
    
print(calc(a,b,interval,target))

    
        
