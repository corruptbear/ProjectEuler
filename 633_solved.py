#!/usr/local/bin/python3
from EulerUtilities import *
import math

    
N=10000000
a=sift(N)

p1,p2,p3,p4,p5,p6,p7=0,0,0,0,0,0,0
for x in a:
    d=x**2-1
    p1+=1/d
    p2+=1/d**2
    p3+=1/d**3
    p4+=1/d**4
    p5+=1/d**5
    p6+=1/d**6
    p7+=1/d**7                      

def B7(x1,x2,x3,x4,x5,x6,x7):
    S=x1**7+21*x1**5*x2+35*x1**4*x3+105*x1**3*x2**2+35*x1**3*x4
    S+=210*x1**2*x2*x3+105*x1*x2**3+21*x1**2*x5+105*x1*x2*x4
    S+=70*x1*x3**2+105*x2**2*x3+7*x1*x6+21*x2*x5+35*x3*x4+x7
    return S
    

X=0-B7(-p1,-p2,-2*p3,-6*p4,-24*p5,-120*p6,-720*p7)/5040
scaling=6/math.pi**2
print(X*scaling)   



    
            
            

    


    

