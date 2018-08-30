m = 10
n = 10
N = 11
i = 5
j = 5


class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        # 没必要使用矩阵，方法如下
        # line = [0]*n
        # self.bin = [line]*m
        # print(self.bin)
        # self.count = 0
        # def Path(i,j,N):
        #     if i<0 or j<0 or i>=m or j>=n:
        #         self.count+=1
        #         return
        #     if N==0:
        #         return
        #     Path(i,j+1,N-1)
        #     Path(i,j-1,N-1)
        #     Path(i+1,j,N-1)
        #     Path(i-1,j,N-1)
        # Path(i,j,N)
        # return self.count
        # 以上方法的优化
        # if i==m or j==n or i<0 or j<0:
        #     return 1
        # if N==0:
        #     return 0
        # return self.findPaths(m,n,N-1,i-1,j)+self.findPaths(m,n,N-1,i+1,j)+self.findPaths(m,n,N-1,i,j-1)+self.findPaths(m,n,N-1,i,j+1)


a = Solution()
print(a.findPaths(m,n,N,i,j))