class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        self.s = matrix.deepcopy()
        def findSquare(i,j):
