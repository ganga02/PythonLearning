class Solution(object):
    def threeSum(self, nums): #[-4, -2, -2, -1, 0, 1, 1, 2, 2]
        nums
        nums.sort()
        result = []

        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:

                total = nums[i] + nums[left] + nums[right]

                if total == 0:

                    result.append([nums[i], nums[left], nums[right]])

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

        return result
        
obj = Solution()

nums = [-4, -2, -2, -1, 0, 1, 1, 2, 2]

result = obj.threeSum(nums)

print(result)