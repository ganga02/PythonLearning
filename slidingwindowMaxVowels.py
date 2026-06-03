class Solution(object):
    def maxVowels(self, s, k):

        vowels = {'a', 'e', 'i', 'o', 'u'}

        left = 0
        vowel_count = 0
        max_count = 0

        for right in range(len(s)):

            if s[right] in vowels:
                vowel_count += 1

            if right - left + 1 == k:

                max_count = max(max_count, vowel_count)

                if s[left] in vowels:
                    vowel_count -= 1

                left += 1

        return max_count

obj=Solution()
result = obj.maxVowels("contaminatiou",3)
print(result)