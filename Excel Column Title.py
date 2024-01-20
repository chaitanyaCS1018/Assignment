def convert_to_title(A):
    result = ""
    while A > 0:
        A -= 1
        remainder = A % 26
        result = chr(65 + remainder) + result
        A //= 26

    return result

user_input = int(input("Enter a positive integer: "))
output = convert_to_title(user_input)
print(output)