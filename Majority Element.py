def majorityElement(nums):
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1

    count = 0
    for num in nums:
        if num == candidate:
            count += 1

    return candidate if count > len(nums) // 2 else None

input_array = [2, 1, 2]
result = majorityElement(input_array)
print("Majority Element:", result)
