# 4. Fibonacci numbers
def fibonacci(n):
    if n < 0:
        return "The number must be positive"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

try:
    number = int(input("Enter a number: "))
    print(f"F({number}) = {fibonacci(number)}")
except ValueError:
    print("Error! Enter a number.")