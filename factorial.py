# the following is a recursive function that solves factorial

def factorial(n):
    fact = 0
    if n == 0:
        return 1
    else:
        fact = n * factorial(n-1)
    return fact

print(factorial(5))
