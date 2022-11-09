#!/usr/local/bin/python3
from EulerUtilities import *

import math


def a(N):
    r=math.sqrt(N)
    return N-int(r)*r #always<r
    

#s=sift(10**7+10**4)

#idx=binary(s,10**7)


def g(a,x):
    if x<a:
        return 1
    return g(a,x-1)+g(a,x-a)

for n in range(3,40):
    print(n,g(math.sqrt(n),n))


    