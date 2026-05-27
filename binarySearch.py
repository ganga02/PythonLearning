n = int(input("Enter no.of Elements: "))
print("Enter Elements in ascending order")
arr=[]
for i in range(n):
    value = int(input())
    arr.append(value)
target = int(input("Enter element to find: "))
print(len(arr))
low = 0
high = len(arr)-1
found = False

while low <= high:
    mid = (low+high)//2;
    if(arr[mid]==target):
        print("Element found at position: ",mid+1)
        found = True
        break
    elif arr[mid]<target:
        low = mid+1
    else:
        high = mid-1

if not found:
    print("Element not found")
