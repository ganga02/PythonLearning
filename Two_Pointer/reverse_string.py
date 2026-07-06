def reverse_string(s):
    left = 0
    right = len(s) - 1

    while left < right:
        # Swap characters
        s[left], s[right] = s[right], s[left]

        left += 1
        right -= 1

    return s

# Input
s = list("hello")   # Convert string to list
result = reverse_string(s)

print("".join(result))