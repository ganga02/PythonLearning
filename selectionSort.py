arr=[90,10,4,60]
n= len(arr)
for i in range(n):
    min_index=i
    for j in range(i+1,n):
        if arr[j]<arr[min_index]:
            min_index=j
    if min_index != i:
        temp = arr[i]
        arr[i]=arr[min_index]
        arr[min_index]=temp
print(arr)