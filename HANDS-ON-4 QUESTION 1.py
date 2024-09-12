def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fib(n-1) + fib(n-2)

n = int(input("Enter any value to calculate Fibonacci sequence(n): "))

result = fib(n)
print(f"Fibonacci({n}): {result}")
