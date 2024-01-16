# Recursive Factorial: Write a recursive function that returns the factorial of a given number.
# Hint: Remember that the factorial of a number is the product of all positive integers up to that number.

def factorial(n):
    if n < 0: return 'Error. Only 0 or positive integers!'
    elif n == 1 or n == 0:
        return 1
    return n*factorial(n-1)

print(factorial(10))