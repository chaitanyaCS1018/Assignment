def generate(numRows):
    result = []

    for i in range(numRows):
        row = [1] * (i + 1)

        for j in range(1, i):
            row[j] = result[i - 1][j - 1] + result[i - 1][j]

        result.append(row)

    return result

numRows = int(input("Enter the number of rows for Pascal's triangle: "))
pascals_triangle = generate(numRows)

print("Pascal's Triangle:")
for row in pascals_triangle:
    print(row)
