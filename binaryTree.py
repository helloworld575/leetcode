def isBalance(root):

    def height(root):
        if root == None:
            return 0
        left = height(root.left)
        right = height(root.right)
        if abs(left-right)>1:
            return 9999
        return max(left,right)+1
    return False if height(root)>=9999 else True