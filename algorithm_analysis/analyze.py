def find_max(a_list):
    """ an O(n) function to find the maximim number 
        Note that the average case to find number of change max is O(log(n)) #nth harmonic number
    """

    max = a_list[0]
    for num in a_list:
        if num>max:
            max = num
    return max

def prefix_average(S):
    """Return list such that, for all j, A[j] equals average of S[0], ..., S[j]."""
    length = len(S)
    A = [0]*length

    for j in range(length):
        total = 0
        for k in range(j+1):
            total += S[k]
        A[j] = total/(j+1)

    return A

    # The big-oh notation for this function is O(n^2)

def prefix_average2(S):
    """Return list such that, for all j, A[j] equals average of S[0], ..., S[j]."""
    
    n = len(S)
    A = [0]*n
    for j in range(n):
        A[j] = sum(S[:j+1])/(j+1)

    return A
    # The big-oh notation for this function is O(n^2)

def prefix_average3(S):
    n = len(S)
    A = [0]*n
    total = 0
    for i in range(n):
        total += S[i]
        A[i] = total / (i+1)
    return A
    #The big-oh notation for this algorithm is O(n)
            
if __name__ == "__main__":  
    print(prefix_average([1,2,3,4,5,6,7,8,9]))
    print(prefix_average2([1,2,3,4,5,6,7,8,9]))
    print(prefix_average3([1,2,3,4,5,6,7,8,9]))