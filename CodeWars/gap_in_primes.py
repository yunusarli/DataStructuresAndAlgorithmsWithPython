"""

The prime numbers are not regularly spaced. For example from 2 to 3 the gap is 1. From 3 to 5 the gap is 2. From 7 to 11 it is 4. Between 2 and 50 we have the following pairs of 2-gaps primes: 3-5, 5-7, 11-13, 17-19, 29-31, 41-43

A prime gap of length n is a run of n-1 consecutive composite numbers between two successive primes (see: http://mathworld.wolfram.com/PrimeGaps.html).

We will write a function gap with parameters:

g (integer >= 2) which indicates the gap we are looking for

m (integer > 2) which gives the start of the search (m inclusive)

n (integer >= m) which gives the end of the search (n inclusive)

n won't go beyond 1100000.

In the example above gap(2, 3, 50) will return [3, 5] or (3, 5) or {3, 5} which is the first pair between 3 and 50 with a 2-gap.


"""
#Note: This is not the optimal solution in case of memory usage

def find_primes(start,stop):
    lookup_num = start
    primes = list()
    
    while stop >= start:
        flag = True
        for i in range(2,lookup_num):
            if lookup_num%i == 0:
                
                flag =  False
        
        if flag:
            primes.append(lookup_num)
        start += 1
        lookup_num = start
    return primes

def gap(g,m,n):
    primes = find_primes(m,n)
    if len(primes) == 0:
        return None
    start = 0
    counter = 1
    while start<len(primes):
        curr = primes[start]
        while counter<len(primes):
            next = primes[counter]
            if next-curr == g:
                return [curr,next]
            counter += 1 
        start += 1
        counter = start+1
    return None