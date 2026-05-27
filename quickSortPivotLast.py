
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot=arr[-1]
    left = []
    right =[]

    for i in range(len(arr)-1):
        
        if arr[i] > pivot:
            right.append(arr[i])
        else:
            left.append(arr[i])
    return quick_sort(left)+[pivot]+quick_sort(right)

arr=[8,1,5,3]
result= quick_sort(arr)
print(result)