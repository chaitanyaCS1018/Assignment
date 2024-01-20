def find_intersection(arr1, arr2):
    result = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            result.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1

    return result


arr_A = [1, 2, 3, 3, 4, 5, 6]
arr_B = [3, 3, 5]

output = find_intersection(arr_A, arr_B)
print(output)
