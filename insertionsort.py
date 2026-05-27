arr=[90,1,-3,60]

n = len(arr)
for i in range(1,n):
    current = arr[i]
    j = i-1
    while j>=0 and arr[j]>current:
        arr[j+1]=arr[j]
        j=j-1
    arr[j+1]=current
print(arr)

