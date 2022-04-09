"""
Binary search algorithm using recursion
In a sorted list binary search can be implemented
"""



def binary_search(sorted_list,target):
    length = int(len(sorted_list)/2)

    #if there is no element left return -1
    if length == 0:
        return -1
    else:
        #view list decreasing flow
        print("Sorted List",sorted_list)
        #if element was found return element
        if sorted_list[length] == target:
            return True,target
            #if element is smaller than target, call function with bigger half
        elif target > sorted_list[length]:
            return binary_search(sorted_list[length:],target)
        #otherwise call function with smaller half of the list.
        elif target < sorted_list[length]:
            return binary_search(sorted_list[:length],target)


result = binary_search([1,2,3,4,5,6,7,8,9],10)

print(result)    