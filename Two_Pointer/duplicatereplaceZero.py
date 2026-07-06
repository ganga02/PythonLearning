arr = [1, 0, 2, 3, 0, 4, 5, 0]
i=0
while i< len(arr)-1:
    if arr[i]==0:
        arr[i+1]=0
        i+=2
    else:
        i+=1
print(arr)

#output=[1,0,0,3,0,0,5,0]