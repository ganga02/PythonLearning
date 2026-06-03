def binary_search(arr,low,high,target):
    
    if low>high:
        return -1
    mid = (low+high)//2
    if arr[mid]==target:
        return mid
    elif arr[mid]>target:
        return binary_search(arr,low,mid-1,target)
    else:
        return binary_search(arr,mid+1,high,target)
arr=[10,20,30,40]
target=int(input("Enter the value to be search: "))
result = binary_search(arr,0,len(arr)-1,target)
if result != -1:
    print("Element found at position: ",result)
else:
    print("Element not found")