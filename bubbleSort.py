arr=[5,2,8,1]

n = len(arr)

for i in range(n):
    for j in range(n-1-i):
        if arr[j]>arr[j+1]:
            temp = arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp

print(arr)