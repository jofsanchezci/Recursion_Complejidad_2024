def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

n = int(input("Enter a number: "))
print(f"Fibonacci number (Recursive): {fibonacci_recursive(n)}")
