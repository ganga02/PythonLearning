s = "abcdaabbcceee"

best_window = ""
left = 0
k = 3

for right in range(len(s)):
    if right - left + 1 == k:

        print(f"Window = {s[left:right+1]}")

        if s[left:right+1] > best_window:
            best_window = s[left:right+1]
            print(f"best_window = {best_window}")

        left += 1

print("Final:", best_window)