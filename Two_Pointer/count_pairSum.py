def count_pairs(arr, target):
    left = 0
    right = len(arr) - 1
    count = 0

    while left < right:

        current_sum = arr[left] + arr[right]

        if current_sum == target:
            print(f"Pair Found: ({arr[left]}, {arr[right]})")
            count += 1
            left += 1
            right -= 1

        elif current_sum < target:
            left += 1

        else:
            right -= 1

    return count


# Input
arr = [1, 2, 3, 7, 8, 9]
target = 10

result = count_pairs(arr, target)

print("Total Pairs =", result)