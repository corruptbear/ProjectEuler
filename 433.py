#!/usr/local/bin/python3

def step(a,b):
    s=0
    if a<b:
        s+=1
    large=max(a,b)
    small=min(a,b)
    r=large%small
    s+=1
    while r!=0:
        large=small
        small=r
        r=large%small
        s+=1
    return s
    

def S(N):
    s=0
    m=0
    for x in range(2,N+1):
        if x%100==0:
            print(x)
        for y in range(1,x):
            t=step(x,y)
            #print(x,y,t)
            if t>m:
                m=t
                #print(t,x,y)
            s+=2*t+1
    s=s+N
    return s

print(S(5*10**6))
        
        