# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        if root:
            temp = root.left
            root.left = root.right
            root.right = temp
        
            if root.left:
                left = self.invertTree(root.left)
            if root.right:
                right = self.invertTree(root.right)
            
        return root