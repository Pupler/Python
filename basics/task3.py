# 3. Sum of the number from 1 to N
def sum_to_n(n):
    result = 0
    for i in range(1, n + 1):
        result += i

    return result

try:
    number = int(input("Enter number: "))
    print(f"The sum from 1 to {number} equals {sum_to_n(number)}")

except ValueError:
    print("Value error!")