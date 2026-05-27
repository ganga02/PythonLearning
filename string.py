str = "ganga"
count = 0
for i in str:
    if i in "aeiou":
        count +=1
print(count)

if str == str[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
