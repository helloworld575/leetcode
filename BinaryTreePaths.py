# leetcode 257. Binary Tree Paths

def binaryTreePaths(self, root):
    """
    :type root: TreeNode
    :rtype: List[str]
    """
    def dfs(root,path,answer):
        if not (root.left or root.right):
            answer.append(path+str(root.val))
        if root.left:
            dfs(root.left,path+str(root.val)+"->",answer)
        if root.right:
            dfs(root.right,path+str(root.val)+"->",answer)
    answer = []
    dfs(root,"",answer)
    return answer