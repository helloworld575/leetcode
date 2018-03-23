'''
    题目理解：
    输入：一个数组，一个整数k
    输出：bool值
    过程：
        数组中连续子序列中数字的和是k的整数倍
'''


class Solution:
    # method1 n^3
    # def checkSubarraySum(self, nums, k):
    #     """
    #     :type nums: List[int]
    #     :type k: int
    #     :rtype: bool
    #     """
    #     length = len(nums)
    #     for i in range(length+1):
    #         for j in range(length-i+1):
    #             if not k==0:
    #                 if self.arraySum(nums,i,j)%k==0:
    #                     return True
    #             else:
    #                 if self.arraySum(nums,i,j)==0:
    #                     return True
    #     return False
    #
    # def arraySum(self,nums,i,j):
    #    sum = 0
    #    for k in range(j,j+i):
    #        sum += nums[k]
    #    return sum

    # n^2logn
    # def checkSubarraySum(self, nums, k):
    #     """
    #     :type nums: List[int]
    #     :type k: int
    #     :rtype: bool
    #     """
    #     length = len(nums)
    #     for i in range(length):
    #         for j in range(2, length - i + 1):
    #             if (not k == 0) and self.arraySum(nums, i, j) % k == 0:
    #                 return True
    #             elif self.arraySum(nums, i, j) == 0:
    #                 return True
    #     return False
    #
    # def arraySum(self,nums,i,j):
    #     sum = 0
    #     for k in range(i,i+j):
    #         sum+=nums[k]
    #     return sum

    #method3 brute force
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        length = len(nums)

        if length < 2:
            return False
        if k == 0:
            return self.checkZero(nums)

        for i in range(length):
            sum = 0
            for j in range(i, length):
                sum += nums[j]
                if sum % k == 0 and j-i>=1:
                    return True
        return False

    def checkZero(self, nums):
        for i in range(len(nums) - 1):
            if nums[i] == 0 and nums[i + 1] == 0:
                return True
        return False




if __name__ == '__main__':
    nums = [1, 1]
    k = 2
    Sol = Solution()
    print(Sol.checkSubarraySum(nums, k))
