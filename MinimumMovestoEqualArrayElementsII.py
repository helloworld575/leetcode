# leetcode 462. Minimum Moves to Equal Array Elements II

def minMov(nums):
    # ans1
    # a = sorted(nums)
    # b = a[len(a) // 2]
    # sum = 0
    # print(a, b)
    # for i in nums:
    #     sum += (abs(i - b))
    # return sum
    a = sorted(nums)
    n = len(nums)
    return sum(a[(n - 1) // 2 + 1:]) - sum(a[:n // 2])

print(minMov([1,2,3]))