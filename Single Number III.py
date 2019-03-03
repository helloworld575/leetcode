class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ans = []
        tmp = {}
        for num in nums:
            if tmp.get(num):
                tmp[num] = 0
            else:
                tmp[num] = 1
        for (key, value) in tmp.items():
            if value == 1:
                ans.append(key)
        return ans
