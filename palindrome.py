name = input("Enter string: ").lower()
def reverse_string(s):

    if s == "":
        return ""

    return reverse_string(s[1:]) + s[0]

result = reverse_string(name)

if name ==result:
    print("Palindrome")
else:
    print("Not Palindrome")