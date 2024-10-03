class TreeNode:
    def __init__(self,val = 0, right = None, left = None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def maxDepth(self,root):
        if not root:
            return 0
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1 + max(left + right)