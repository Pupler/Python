# 1. Factorial of a number
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

try:
    number = int(input("Enter the number: \n"))
    print(f"The factorial of number {number} is {factorial(number)}")

except ValueError:
    print("Value error!")