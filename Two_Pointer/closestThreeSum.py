def closest_pair(arr, target):
    

    min_diff = float('inf')
    pair = ()
    for i in range(len(arr)-1):
        left=i+1
        right=len(arr)-1
        while left < right:

            current_sum = arr[i]+arr[left] + arr[right]
            diff = abs(target - current_sum)

            if diff < min_diff:
                min_diff = diff
                pair = (arr[i],arr[left], arr[right])

            if current_sum < target:
                left += 1

            elif current_sum > target:
                right -= 1

            else:
                break

    return pair


# Input
arr = [1, 3, 6, 7, 10]
target = 15

result = closest_pair(arr, target)

print("Closest Pair =", result)