#回溯综合

#1. 子集合subset
#sol1：无重复子集合
nums = [1,2,3]
n_list = []

def subset(n_list,nums):
    nums = sorted(nums)
    backtrack(n_list, nums, [], 0)
    return n_list
def backtrack(n_list,nums,tmp,start):
    #注意，python多维数组时，append的是指针，所以tmp的改变会显示到所有的数组项上去
    n_list.append(tmp.copy())
    for i in range(start,len(nums)):
        tmp.append(nums[i])
        backtrack(n_list,nums,tmp,i+1)
        tmp.pop()
print(subset(n_list,nums))


candidates = [2,3,6,7]
target = 7

# def combinationSum(self, candidates, target):
#     for i in candidates:
#         sum = i
#         num = 0
#         while sum<target:
#             sum+=candidates[num]