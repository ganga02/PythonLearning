nums = [-3,4,0,-2,3,2]

nums.sort()

left = 0
right = len(nums) - 1

result = []

while left < right:

    total = nums[left] + nums[right]

    if total == 0:

        result.append([nums[left], nums[right]])

        left += 1
        right -= 1

        while left < right and nums[left] == nums[left - 1]:
            left += 1

        while left < right and nums[right] == nums[right + 1]:
            right -= 1

    elif total < 0:
        left += 1

    else:
        right -= 1

print(result)