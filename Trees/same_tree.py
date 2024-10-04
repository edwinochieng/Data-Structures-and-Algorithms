class TreeNode:
    def __init__(self, val=0, right = None, left = None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def isSameTree(self, p:TreeNode, q:TreeNode) -> bool:
        if not p and not q:
            return True
        
        if not p or not q or p.val != q.val:
            return False
        
        return (self.isSameTree(p.left,q.left) and self.isSameTree(p.right, p.left))

        