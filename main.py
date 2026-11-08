# Recursive function to generate Fibonacci numbers
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Print the Fibonacci sequence up to a given number of terms
def print_fibonacci_series(terms):
    print("Fibonacci Series:")
    for i in range(terms):
        print(fibonacci(i), end=" ")

# Example: print first 10 terms
print_fibonacci_series(10)
