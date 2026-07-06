def move_zeroes(arr):
    left = 0

    # Move all non-zero elements to the front
    for right in range(len(arr)):
        if arr[right] != 0:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1

    return arr


# Input
arr = [0, 1, 0, 3, 12]

result = move_zeroes(arr)

print(result)