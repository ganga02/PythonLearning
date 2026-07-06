def character_replacement(s, k):
    left = 0
    max_count = 0
    max_length = 0
    freq = {}

    for right in range(len(s)):
        freq[s[right]] = freq.get(s[right], 0) + 1

        max_count = max(max_count, freq[s[right]])

        window_size = right - left + 1

        if window_size - max_count > k:
            freq[s[left]] -= 1
            left += 1

        
        if right-left+1 > max_length:
            max_length=right-left+1
            start=left
            end=right
        print(freq)
    return max_length,s[start:end+1]


s = "AABABBA"
k = 1

length,array =character_replacement(s, k)
print(length)
print(array)