
def intersect(nums1, nums2):

    result = []

    d = {}

    for num in nums1:
        d[num] = d.get(num, 0) + 1

    for num in nums2:
        if num in d and d[num] > 0:
            result.append(num)
            d[num] -= 1

    return result

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
res=intersect(nums1,nums2)
print(res)