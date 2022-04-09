#linear recursive sum
def recursive_sum(S,n):
    #n will be the length of the element
    if n == 0:
        return 0
    else:
        return recursive_sum(S,n-1) + S[n-1]


def reverse_recursively(S,start,stop):
    #this is also a linear recursive algorithm
    if start < stop-1:
        S[start],S[stop-1] = S[stop-1],S[start]
        return reverse_recursively(S,start+1,stop-1)


def binary_sum(S,start,stop):
    print(S,start,stop)
    
    if start >= stop:
        return 0
    elif start == stop-1:
        return S[start]
    else:
        mid = (start + stop) // 2
        return binary_sum(S,start,mid) + binary_sum(S,mid,stop)


print(binary_sum([1,2,3,4,5,6,7,8,9],0,9))
