#factorial calculator recursive version

def factorial(n:int) -> int:
    #last number that factorial function can perform.
    #0! is 1
    if n <= 0:
        return 1
    #otherwise return n*(n-1)!
    else:
        return factorial(n-1)*n

if __name__ == "__main__":
    result = factorial(5)
    print(result)