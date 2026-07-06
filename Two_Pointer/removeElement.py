def remove_element(arr, val):
    left = 0

    for right in range(len(arr)):

        if arr[right] != val:
            arr[left] = arr[right]
            left += 1

    return left


# Input
arr = [3, 2, 2, 3]
val = 3

k = remove_element(arr, val)

print("Number of elements =", k)
print("Array =", arr[:k])