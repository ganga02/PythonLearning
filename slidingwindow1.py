nums=[1,2,3,4,1,2,5,6,4]
k=3
window_size=0
max_sum=0
left=0
best_window=[]
for right in range(len(nums)):
    window_size += nums[right]
    if right-left+1 == k:
        if window_size > max_sum:
            max_sum=window_size
            best_window=nums[left:right+1]
        window_size -= nums[left]
        left+=1
print(best_window)
print(len(best_window))
sum=0
for i in best_window:
    sum +=i
print(sum)
print(sum/round(k,2))