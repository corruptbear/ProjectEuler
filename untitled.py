#!/usr/local/bin/python3
from EulerUtilities import *

from bisect import *
import collections

import math
import random


    
    

class Solution:
    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """
        n=int(n)
        r=n-1
        
        for m in range(int((math.log2(n+1))),2,-1):
            print(m)
            t=self.isM1(n,m)
            if t!=-1:
                r=t
                return t
        return str(r)
            
    
    def isM1(self,n,m):
        hi=int(n**(1/(m-1)))+1
        lo=int(n**(1/(m)))
        while hi-lo>1:
            mid=int((hi+lo)/2)
            val=(pow(mid,m)-1)/(mid-1)
            if val>n:
                hi=mid
            elif val<n:
                lo=mid
            elif val==n:
                return mid
        if (pow(hi,m)-1)/(hi-1)==n:
            return hi
        if (pow(lo,m)-1)/(lo-1)==n:
            return lo
        return -1
            
            
S=Solution()
for i in range(14919921443713777,14919921443713778):
    print(S.smallestGoodBase(i))            
        
        

def lookNext(s):
    idx=0
    maxIdx=len(s)-1
    L=""
    c=s[0]
    count=1
    while True:
        idx+=1
        if idx>maxIdx:
            L=L+str(count)+str(c)
            break
        if s[idx]==c:
            count+=1
            continue
        elif s[idx]!=c:
            L=L+str(count)+str(c)
            c=s[idx]
            count=1
    return L
    
a="1"        
for i in range(2,10): 
    a=lookNext(a)
    print(a)        

#9:311312(71)+11131221(49)

            
    