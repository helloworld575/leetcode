class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxlength = 0
        substring = ""
        for i in range(len(s)):
            print(substring)
            while s[i] in substring:
                substring = substring[1:]
            substring+=s[i]
            if len(substring)>maxlength:
                maxlength = len(substring)
        return maxlength

if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("pwwkew"))
