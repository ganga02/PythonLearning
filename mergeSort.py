
def merge_sort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        left = merge_sort(arr[:mid])
        right= merge_sort(arr[mid:])

        i=0;j=0;k=0
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                arr[k] = right[j]
                j+=1
            else:
                arr[k]=left[i]
                i+=1
            k+=1
        while i < len(left):
            arr[k]=left[i]
            i+=1
            k+=1
        while j < len(right):
            arr[k]=right[j]
            j+=1
            k+=1
    return arr

arr=[90,2,60,50]

merge_sort(arr)
print(arr)