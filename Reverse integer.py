def reverse_integer(x):
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    
    sign = 1 if x >= 0 else -1
    x = abs(x)
    
    reversed_num = 0
    while x != 0:
        digit = x % 10
        if reversed_num > (INT_MAX - digit) // 10:
            return 0
        reversed_num = reversed_num * 10 + digit
        x //= 10

    return sign * reversed_num

user_input = int(input("Enter an integer: "))
output = reverse_integer(user_input)
print(output)
