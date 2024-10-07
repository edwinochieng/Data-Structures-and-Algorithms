class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubTree(self, root: TreeNode, subRoot: TreeNode):
        if not subRoot: return True
        if not root: return False

        if self.sameTree(root,subRoot):
            return True
        
        return self.isSubTree(root.left, subRoot) or self.isSubTree(root.right,subRoot)


    def sameTree(self, root: TreeNode, subRoot: TreeNode):
        if not root and not subRoot:
            return True
        
        if not root or not subRoot or root.val != subRoot.val:
            return False
        
        return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right)

    

