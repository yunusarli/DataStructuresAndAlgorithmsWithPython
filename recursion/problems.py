def find_min_max(sequence):
    """
    Problem: Find minimum and maximum values in a sequence without using any loop
    """
    if len(sequence) == 2:
        return sequence
    else:
        first = sequence[0]
        second = sequence[1]

        if second < first:
            sequence[0],sequence[1] = sequence[1],sequence[0]

        mini = sequence[0]
        maxi = sequence[1]
        val = sequence[2]

        if val < mini:
            return find_min_max(sequence[1:])
        elif val > maxi:
            sequence[0],sequence[1] = sequence[1],sequence[0]
            return find_min_max(sequence[1:]) 
        else:
            sequence[0],sequence[2] = sequence[2],sequence[0]
            return find_min_max(sequence[1:])
        

#sequence = [0,1,2,9,3,4,-1,5,6,7,8]

#result = find_min_max(sequence)

#print(result)


def base_2_logarithm(n,count = 0):
    """
    Problem: Calculate the base 2 logarithm of the given value only by using addition and 
    integer division
    """
    if n == 1:
        return count
    else:
        return base_2_logarithm(n//2,count+1)

#print(base_2_logarithm(17))

def element_uniqueness_problem(sequence):
    """
    Problem: Solve Element uniqueness problem recursivly at most O(n^2) time complexity
    """
    if len(sequence) == 1:
        return True
    else:
        elem = sequence[0]
        draft = sequence[1:]
        contains = elem in draft
        
        if contains: return False
        return element_uniqueness_problem(draft)

#print(element_uniqueness_problem([1,2,3,4]))

def towers_of_hanoi(k,start,end,station):
    """
    Problem: Solve the towers of hanoi problem using recursion
    """
    if k == 1:
        print("Moving {} from {} to {}".format(k,start,end))
        return
    towers_of_hanoi(k-1,start,station,end)
    print("Moving {} from {} to {}".format(k,start,end))
    towers_of_hanoi(k-1,station,end,start)

towers_of_hanoi(5,"A","B","C")