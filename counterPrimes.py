class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [0] * n
        # print(nums)
        for i in range(2, n // 2 + 1):
            if nums[i]!=1:
                for j in range(2 * i, n, i):
                    nums[j] = 1
        # print(nums)
        sum = 0
        for i in range(2, n):
            if (nums[i] == 0):
                sum += 1
        return sum


if __name__ == '__main__':
    s = Solution()
    print(s.countPrimes(1500000))
