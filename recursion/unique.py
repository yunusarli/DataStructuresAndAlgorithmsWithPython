#recursion sometimes can become very unefficient.
#In the following example to find unique element we used recursive implementation and 
#the big-Oh will become O(2^n) which is incredibly inefficient.

def unique(S,start,stop):

    if stop - start <= 1: return True
    elif not unique(S,start,stop-1): return False
    elif not unique(S,start+1,stop): return False
    else: return S[start] != S[stop-1]


#print(unique([1,2,3,4,5,1,2],0,7))

def bad_fibonacci(n):
    if n<=1:
        return n
    else:
        return bad_fibonacci(n-2) + bad_fibonacci(n-1)