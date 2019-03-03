# leetcode 565. Array Nesting


def arrayNesting(nums):
    maxs = 0
    for i in range(len(nums)):
        size = 0
        j = i
        while nums[j]>=0:
            size+=1
            lastj = j
            j = nums[lastj]
            nums[lastj]=-1
        print(nums)
        maxs = max(size,maxs)
    return maxs


print(arrayNesting([5,4,0,3,1,6,2]))