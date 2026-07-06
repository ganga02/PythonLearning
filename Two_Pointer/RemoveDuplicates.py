arr = [1,1,2,2,3,4]

left = 0

for right in range(len(arr)):
    if arr[left] != arr[right]:
        left += 1
        arr[left], arr[right] = arr[right], arr[left]

print(arr[:left+1])