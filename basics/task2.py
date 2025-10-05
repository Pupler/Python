# 2. Is even
def is_even(n):
    return n % 2 == 0

try:
    number = int(input("Enter ur number: \n"))
    print(is_even(number))

except ValueError:
    print("Value error!")