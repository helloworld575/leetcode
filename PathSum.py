class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    end = False

    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        self.judge(root,0,sum)
        return self.end

    def judge(self,root,val,sum):
        if not self.end and root is not None:
            if root.left is None and root.right is None and root.val+val==sum:
                self.end = True
            if root.left is not None:
                self.judge(root.left,val+root.val,sum)
            if root.right is not None:
                self.judge(root.right,val+root.val,sum)

