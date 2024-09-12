def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fib(n-1) + fib(n-2)

n = int(input("Enter any value to calculate Fibonacci sequence(n): "))

result = fib(n)
print(f"Fibonacci({n}): {result}")




''' fib(5) -> fib(4) -> fib(3) -> fib(2) -> fib(1) -> fib(0)
Return to fib(2) and fib(1), then return to fib(3).
fib(5) -> fib(4) calls fib(2) -> fib(1) -> fib(0).
fib(5) calls fib(3) -> fib(2) -> fib(1) -> fib(0) '''
