# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if root and root.left and root.right:
            return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
        elif root and root.left:
            return self.hasPathSum(root.left, sum - root.val)
        elif root and root.right:
            return self.hasPathSum(root.right, sum - root.val)
        else:
            if root and root.val == sum:
                return True
        return False