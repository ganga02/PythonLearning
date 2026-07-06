def segregate_positive_negative(arr):
    left = 0
    right = len(arr) - 1

    while left < right:

        # Move left until a positive number is found
        while left < right and arr[left] < 0:
            left += 1

        # Move right until a negative number is found
        while left < right and arr[right] >= 0:
            right -= 1

        # Swap positive and negative
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]

            left += 1
            right -= 1

    return arr


# Input
arr = [-12, 11, -13, -5, 6, -7, 5]

result = segregate_positive_negative(arr)

print(result)