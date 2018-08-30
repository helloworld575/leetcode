

nums = [1,1]
k=2
def checkSubarraySum(nums,k):
    if len(nums) < 2:
        return False
    if k == 0:
        for i in nums:
            if i != 0:
                return False
        return True
    for i in range(0, len(nums)):
        sum = nums[i]
        for j in range(i + 1, len(nums)):
            sum += nums[j]
            if sum % k == 0:
                return True
    return False
print(checkSubarraySum(nums,k))