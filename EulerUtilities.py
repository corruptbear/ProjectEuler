#!/usr/local/bin/python3
import math
from random import randint
from functools import reduce
import itertools

def binary(L,x):  #if found, return index; else return the index of the first greater item
    if x<L[0] or x>L[-1]:
        return -1
    minI=0
    maxI=len(L)-1
    midI=(minI+maxI)//2
    
    while maxI-minI>1:
        if x>L[midI]:
            minI=midI
        elif x<L[midI]:
            maxI=midI
        elif x==L[midI]:
            return midI
        midI=(minI+maxI)//2

    if x==L[maxI]:
        return maxI
    if x==L[minI]:
        return minI
    return minI+1


def prod(A):
    return reduce((lambda x, y: x * y), A)
    
def factors(d):
    L=[[k**i for i in range(d[k]+1)] for k in d.keys()]  
    c=[prod(l) for l in itertools.product(*L)]
    return sorted(c)

def sift(n):
    A=[True]*(n+1)
    A[1]=False
    max_i=int(math.sqrt(n))+1
    for i in range(2,max_i):
        if A[i]:
            A[i*i::i]=[False]*(n//i+1-i)
    return [int(i) for i in range(1,n+1) if A[i]]
    
def decompWithList(n,L):
    assert (L[-1]**2>n),'prime list not sufficiently long'       
    current=n
    decomp={}
    for p in L:
        if current==1:
            break
        if p>math.sqrt(current):
            decomp[current]=1
            break
        if current%p==0:
            decomp[p]=1
            current=current//p
            while current>1:
                if current%p==0:
                    decomp[p]=decomp[p]+1
                    current=current//p
                else:
                    break
    return decomp
    
def decompAll(N):
    D=[]
    for i in range(N+1):
        D.append({})
    P=sift(N)
    for p in P:
        for i in range(1,N//p+1):
            current=i*p
            c=0
            while current%p==0:
                c+=1
                current=current//p
            D[i*p][p]=c 
    return D

def gcd(a,b):
    large=max(a,b)
    small=min(a,b)
    r=large%small
    while r!=0:
        large=small
        small=r
        r=large%small
    return small

def lcm(a,b):
    return (a*b)//gcd(a,b)

def pascals_triangle(n):
    x = [1]
    yield x
    for i in range(n - 1):
        x = [sum(i) for i in zip([0] + x, x + [0])]
        yield x

def digits(n,base):
    num=int(n)
    L=[]
    while True:
        d=num//int(base)
        r=num-d*int(base)
        L.append(int(r))
        num=d
        if num==0:
            break
    return list(reversed(L))
    
def evaluate(L,base):
    n=0
    exp=0
    for i in reversed(L):
        n+=i*base**exp
        exp+=1
    return n
    
    
def Miller_Rabin(p, base):
    '''
    The result False implies that p is definitely not prime.
    The result True implies that p **might** be prime.
    '''
    result = 1
    exponent = p-1
    modulus = p
    bitstring = bin(exponent)[2:] # Chop off the '0b' part of the binary expansion of exponent
    for bit in bitstring: 
        sq_result = result*result % modulus 
        if sq_result == 1:
            if (result != 1) and (result != exponent): 
                return False  # a ROO violation occurred
        if bit == '0':
            result = sq_result 
        if bit == '1':
            result = (sq_result * base) % modulus
    if result != 1:
        return False  
    return True  
    
    
def is_prime(p, witnesses=50):  # witnesses is a parameter with a default value.
    '''
    For p < 2^64, the test is deterministic, using known good witnesses.
    Good witnesses come from a table at Wikipedia's article on the Miller-Rabin test,
    based on research by Pomerance, Selfridge and Wagstaff, Jaeschke, Jiang and Deng.
    For larger p, a number (by default, 50) of witnesses are chosen at random.
    '''
    if (p%2 == 0): # Might as well take care of even numbers at the outset!
        if p == 2:
            return True
        else:
            return False 
    
    if p > 2**64:  # We use the probabilistic test for large p.
        trial = 0
        while trial < witnesses:
            trial = trial + 1
            witness = randint(2,p-2) 
            if Miller_Rabin(p,witness) == False:
                return False
        return True
    
    else:  # We use a determinisic test for p <= 2**64.
        verdict = Miller_Rabin(p,2)
        if p < 2047:
            return verdict # The witness 2 suffices.
        verdict = verdict and Miller_Rabin(p,3)
        if p < 1373653:
            return verdict # The witnesses 2 and 3 suffice.
        verdict = verdict and Miller_Rabin(p,5)
        if p < 25326001:
            return verdict # The witnesses 2,3,5 suffice.
        verdict = verdict and Miller_Rabin(p,7)
        if p < 3215031751:
            return verdict # The witnesses 2,3,5,7 suffice.
        verdict = verdict and Miller_Rabin(p,11)
        if p < 2152302898747:
            return verdict # The witnesses 2,3,5,7,11 suffice.
        verdict = verdict and Miller_Rabin(p,13)
        if p < 3474749660383:
            return verdict # The witnesses 2,3,5,7,11,13 suffice.
        verdict = verdict and Miller_Rabin(p,17)
        if p < 341550071728321:
            return verdict # The witnesses 2,3,5,7,11,17 suffice.
        verdict = verdict and Miller_Rabin(p,19) and Miller_Rabin(p,23)
        if p < 3825123056546413051:
            return verdict # The witnesses 2,3,5,7,11,17,19,23 suffice.
        verdict = verdict and Miller_Rabin(p,29) and Miller_Rabin(p,31) and Miller_Rabin(p,37)
        return verdict # The witnesses 2,3,5,7,11,17,19,23,29,31,37 suffice for testing up to 2^64


def legendre(a, p):
    return pow(a, (p - 1) // 2, p)
 
def tonelli(n, p):
    #assert legendre(n, p) == 1, "not a square (mod p)"
    if legendre(n, p) != 1:
        return -2
    q = p - 1
    s = 0
    while q % 2 == 0:
        q //= 2
        s += 1
    if s == 1:
        return pow(n, (p + 1) // 4, p)
    for z in range(2, p):
        if p - 1 == legendre(z, p):
            break
    c = pow(z, q, p)
    r = pow(n, (q + 1) // 2, p)
    t = pow(n, q, p)
    m = s
    t2 = 0
    while (t - 1) % p != 0:
        t2 = (t * t) % p
        for i in range(1, m):
            if (t2 - 1) % p == 0:
                break
            t2 = (t2 * t2) % p
        b = pow(c, 1 << (m - i - 1), p)
        r = (r * b) % p
        c = (b * b) % p
        t = (t * c) % p
        m = i
    return r   
      
