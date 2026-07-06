def min_subarray_len(target, nums):
    left = 0
    current_sum = 0
    min_len = float('inf')

    for right in range(len(nums)):
        current_sum += nums[right]

        while current_sum >= target:
            min_len = min(min_len, right - left + 1)
            current_sum -= nums[left]
            left += 1

    if min_len == float('inf'):
        return 0

    return min_len


# Input
target = 7
nums = [2, 3, 1, 2, 4, 3]

print(min_subarray_len(target, nums))


(or)


def min_subarray_len(target, nums):
    left = 0
    current_sum = 0
    min_len = float('inf')

    start = -1
    end = -1

    for right in range(len(nums)):
        current_sum += nums[right]

        while current_sum >= target:

            # If current window is smaller
            if right - left + 1 < min_len:
                min_len = right - left + 1
                start = left
                end = right

            current_sum -= nums[left]
            left += 1

    if min_len == float('inf'):
        return 0, []

    return min_len, nums[start:end+1]


target = 7
nums = [2, 3, 1, 2, 4, 3]

length, subarray = min_subarray_len(target, nums)

print("Minimum Length:", length)
print("Minimum Subarray:", subarray)