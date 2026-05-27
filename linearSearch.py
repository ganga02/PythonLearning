n = int(input("Enter the no. of Elements: "))
arr = []

for i in range(n):
    value = int(input())
    arr.append(value)

target = int(input("Enter the element to search: "))
found = False

for i in range(len(arr)):
    if arr[i] == target:
        found = True
        break
if found:
    print("Element found")
else:
    print("Element not found")