nums=[1,2,3,4,5]
prefix =[0]*5
prefix[0]=nums[0]
for i in range(1, len(nums)):
    prefix[i]=prefix[i-1]+nums[i]
print(prefix)