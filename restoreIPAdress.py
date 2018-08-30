class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # mother fucker coding
        ret = []
        for a in range(1,4):
            for b in range(1,4):
                for c in range(1,4):
                    for d in range(1,4):
                        if a+b+c+d==len(s):
                            s1 = s[0:a]
                            s2 = s[a:a + b]
                            s3 = s[a+b:a+c+b]
                            s4 = s[a+b+c:a+b+c+d]
                            A = int(s1)
                            B = int(s2)
                            C = int(s3)
                            D = int(s4)
                            if(A<=255 and B<=255 and C<=255 and D<=255 and str(A)==s1 and str(B)==s2 and str(C)==s3 and str(D)==s4):
                                st = str(A)+"."+str(B)+"."+str(C)+"."+str(D)
                                ret.append(st)

        return ret

a = Solution()
print(a.restoreIpAddresses("010010"))