# leetcode 129. Sum Root to Leaf Numbers


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        nums = []
        Nodes = [(root,root.val)]
        while Nodes:
            Now = Nodes.pop()
            if not (Now[0].right or Now[0].left):
                nums.append(Now[1])
            if Now[0].left:
                Nodes.append((Now[0].left,Now[1]*10+Now[0].left.val))
            if Now[0].right:
                Nodes.append((Now[0].right,Now[1]*10+Now[0].right.val))
        return sum(nums)