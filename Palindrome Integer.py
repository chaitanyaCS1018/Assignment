def isPalindrome(x):

    if x < 0:
        return 0

    length = 0
    temp = x
    while temp > 0:
        temp //= 10
        length += 1

    reversed_half = 0
    temp = x
    for _ in range(length // 2):
        reversed_half = reversed_half * 10 + temp % 10
        temp //= 10

    if length % 2 == 1:
        temp //= 10

    return temp == reversed_half
print(isPalindrome(12121))
print(isPalindrome(123))
