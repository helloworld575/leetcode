# leetcode 171.Excel Sheet Column Number

class Solution:
    def titleToNumber(s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        num = 0
        for i in range(len(s)):
            tmp = ord(s[i])-ord('A')+1
            num = num*26+tmp
        return num

print(Solution.titleToNumber("AA"))