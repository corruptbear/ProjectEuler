#!/usr/local/bin/python3
from EulerUtilities import *


N=50000000
primes=sift(int(math.sqrt(2*N**2-1)))

L=[True]*(N+1)

for p in primes:
    R8=p%8
    if R8==1:
       R=tonelli((p+1)//2,p)
       L[R::p]=[False]*((N-R)//p+1)
       L[p-R::p]=[False]*((N-p+R)//p+1)
       if R<p-R:
           t=R
       else:
           t=p-R
       if 2*t**2-1==p:
           L[t]=True

    if R8==7:
       R=pow((p+1)//2,(p+1)//4,int(p))
       L[R::p]=[False]*((N-R)//p+1)
       L[p-R::p]=[False]*((N-p+R)//p+1)
       if R<p-R:
           t=R
       else:
           t=p-R
       if 2*t**2-1==p:
           L[t]=True
        
A=[int(i) for i in range(2,N+1) if L[i]]

print(len(A))


'''
#brute force
count=0
L=[]
for i in range(2,N+1):
    R7=i%7
    if R7==2 or R7==5:
        continue
    R17=i%17
    if R17==3 or R17==14:
        continue
    R23=i%23
    if R23==9 or R23==14:
        continue
    R31=i%31
    if R31==4 or R31==27:
        continue
    R71=i%71
    if R71==6 or R71==65:
        continue
    R97=i%97
    if R97==7 or R97==90:
        continue
    
    S=2*i**2-1  
    if is_prime(S):
        #print(i,S,decompWithList(S,primes))
        L.append(i)
        count+=1        
print(count+5)
print(L)
'''

        


    

    

