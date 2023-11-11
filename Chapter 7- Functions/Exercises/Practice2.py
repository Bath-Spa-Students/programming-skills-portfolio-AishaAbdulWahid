# Q2. Write a Python function that calculates the factorial of a given positive integer using recursion (a defined function can call itself).
# Factorial (3! = 3 * 2 * 1 = 6)

def factorial(n):   # Define a function named 'factorial' that takes an argument 'n'.
    if n == 0:   # If bas case: if 'n' is zero
        return 1   # Return 1 because the factorial of 0 is 1.
    else:   # Recursive case: if 'n' is not zero
        return n * factorial(n-1)   # Return 'n' multiplied by the factorial of 'n-1'.
print(factorial(6))