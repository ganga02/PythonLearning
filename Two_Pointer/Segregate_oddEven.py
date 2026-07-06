def segregate_even_odd(arr):
    left = 0
    right = len(arr) - 1

    while left < right:

        # Move left until an odd number is found
        while left < right and arr[left] % 2 == 0:
            left += 1

        # Move right until an even number is found
        while left < right and arr[right] % 2 != 0:
            right -= 1

        # Swap odd and even
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]

            left += 1
            right -= 1

    return arr


# Input
arr = [12, 17, 70, 15, 22, 65, 21, 90]

result = segregate_even_odd(arr)

print(result)