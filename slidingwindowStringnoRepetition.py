class Solution(object):
    def lengthOfLongestSubstring(self, s):

        seen = set()

        left = 0
        max_length = 0
        start = 0

        for right in range(len(s)):

            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])

            if right - left + 1 > max_length:
                max_length = right - left + 1
                start = left
                end=right

        return max_length,s[start:end+1]
obj = Solution()

length,arr1=obj.lengthOfLongestSubstring("abcabdbb")
print(length)
print(arr1)
