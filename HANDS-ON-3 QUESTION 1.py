

def compute_value(y):
    return (lambda x: x * x + 1)(y)

try:
    user_input = int(input("How many y to calculate? "))
    result = compute_value(user_input)
    print(f"After calculation: {result}")
except ValueError:
    print("Enter a valid integer:")

