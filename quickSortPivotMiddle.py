
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    pivot=arr[mid]
    left = []
    right =[]

    for i in range(len(arr)):
        if i == mid:
            continue
        if arr[i] > pivot:
            right.append(arr[i])
        else:
            left.append(arr[i])
    return quick_sort(left)+[pivot]+quick_sort(right)

arr=[8,1,5,3]
result= quick_sort(arr)
print(result)