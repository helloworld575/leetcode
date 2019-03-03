
a = [1,2,3,0,2]
class Solution(object):
    def maxProfit(self, profit):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(profit)<2:
            return 0
        s0 = [0]
        s1 = [-profit[0]]
        s2 = [float("-inf")]
        for i in range(1,len(profit)):
            s0.append(max(s0[i-1],s2[i-1]))
            s1.append(max(s1[i-1],s0[i-1]-profit[i]))
            s2.append(s1[i-1]+profit[i])
        return max(s0[len(profit)-1],s2[len(profit)-1])
S = Solution()
print(S.max_fit(a))

