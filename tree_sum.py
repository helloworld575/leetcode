# class Solution:
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         thr_sums = []
#         two_sums = []
#         ans = []
#         n = len(nums)
#         for i in range(n):
#             for j in range(i + 1, n):
#                 two_sums.append([nums[i], nums[j], nums[i] + nums[j], i, j])
#         t = len(two_sums)
#         for i in range(n):
#             for j in range(t):
#                 if nums[i] + two_sums[j][2] == 0 and two_sums[j][3] != i and two_sums[j][4] != i:
#                     thr_sums.append([two_sums[j][0], two_sums[j][1], nums[i]])
#         if [0, 0, 0] in thr_sums:
#             thr_sums.append([0, 0, 0])
#         h = len(thr_sums)
#         for i in range(h):
#             flag = 0
#             for j in range(i + 1, h):
#                 if (thr_sums[i][0] in thr_sums[j]) and (thr_sums[i][1] in thr_sums[j]) and (
#                         thr_sums[i][2] in thr_sums[j]):
#                     flag = 1
#             if flag == 0:
#                 ans.append(sorted(thr_sums[i]))
#         return ans
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 2:
            return []
        thr = []
        ans = []
        nums = sorted(nums)
        n = len(nums)
        min_z = 0
        while min_z < n and nums[min_z] < 0:
            min_z += 1
        min_z-=1
        max_z = n - 1
        while max_z > 0 and nums[max_z] > 0:
            max_z -= 1
        max_z+=1
        print(min_z, max_z)
        print(nums)
        i = 0
        while i <= max_z:
            j = n - 1
            while j >= min_z:
                if nums[i] + nums[j] < 0:
                    k = max_z
                    while k < j:
                        if nums[i] + nums[k] + nums[j] == 0:
                            thr.append([nums[i], nums[k], nums[j]])
                        k += 1
                if nums[i] + nums[j] > 0:
                    k = min_z
                    while k > i:
                        if nums[i] + nums[k] + nums[j] == 0:
                            thr.append([nums[i], nums[k], nums[j]])
                        k -= 1
                if nums[i] + nums[j] == 0:
                    print(nums[i],nums[j])
                    k = min_z
                    while k >= min_z and k <= max_z:
                        print(nums[i],nums[k],nums[j])
                        if nums[i] + nums[k] + nums[j] == 0:
                            thr.append([nums[i], nums[k], nums[j]])
                        k += 1
                j -= 1
            i += 1
        print(thr)
        if [0, 0, 0] in thr:
            thr.append([0, 0, 0])
        for i in range(len(thr)):
            flag = 0
            for j in range(i + 1, len(thr)):
                if (thr[i][0] == thr[j][0]) and (thr[i][1] == thr[j][1]) and (thr[i][2] == thr[j][2]):
                    flag = 1
                    break
            if flag == 0:
                ans.append(thr[i])
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.threeSum( [-1, 0, 1, 2, -1, -4]))
