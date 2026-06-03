nums=[2,1,4,2,5]
k=3
max_sum=0
left=0
window_size=0
for right in range(len(nums)):
    window_size +=nums[right]
    if right-left+1 ==k:
        max_sum = max(max_sum,window_size)
        window_size -= nums[left]
        left +=1
print(max_sum)