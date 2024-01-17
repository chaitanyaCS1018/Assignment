def plusOne(digits):
    n = len(digits)
    carry = 1
    for i in range(n - 1, -1, -1):
        total = digits[i] + carry
        digits[i] = total % 10
        carry = total // 10

    if carry:
        digits.insert(0, carry)

    return digits

input_array = [1, 2, 3]
output_array = plusOne(input_array)
print(output_array)
