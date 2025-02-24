"""
Create a decorator function to check that the argument passed to the function factorial is a non-negative integer:

Create a factorial function which finds the factorial of a number.

Use the decorator to decorate the factorial function to only allow factorial of non-negative integers.
"""

def check_num(func):
    def wrapper(n):
        if not isinstance(n,int) or n<0:
            raise ValueError("n must be a non-negative integer")
        return func(n)
    return wrapper 

@check_num
def findFact(n):
    if n==0 or n==1:
        return 1 
    return n*findFact(n-1)

result=findFact(10)
print(result)