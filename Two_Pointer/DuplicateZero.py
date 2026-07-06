def duplicate_zeros(arr):
    temp = []

    for num in arr:
        temp.append(num)

        if num == 0:
            temp.append(0)
    print(temp)
    # Copy back only up to the original array length
    for i in range(len(arr)):
        arr[i] = temp[i]

    return arr


# Input
arr = [1, 0, 2, 3, 0, 4, 5, 0]

print(duplicate_zeros(arr))