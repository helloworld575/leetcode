class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #wrong ans
        # if root == None or root.left==None:
        #     return -1
        # elif root.left!=root.right:
        #     return max(root.left.val,root.right.val)
        # else:
        #     return min(self.findSecondMinimumValue(root.left),self.findSecondMinimumValue(root.right))
        # ans1
        # def dfs(node):
        #     if node:
        #         unique.add(node.val)
        #         dfs(node.left)
        #         dfs(node.right)
        #
        # unique = set()
        # dfs(root)
        # ans = float('inf')
        # mini = root.val
        # for i in unique:
        #     if mini<i<ans:
        #         ans = i
        # return ans if ans<float('inf') else -1
        #ans2
        self.ans = float('inf')
        mini = root.val

        def dfs(node):
            if node:
                if mini < node.val < self.ans:
                    self.ans = node.val
                elif mini == node.val:
                    dfs(node.left)
                    dfs(node.right)
        dfs(root)
        return self.ans if self.ans<float('inf') else -1
