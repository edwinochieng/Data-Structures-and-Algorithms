from collections import deque

class TreeNode:
    def __init__(self, val = 0 , left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self,root:TreeNode):

        if not root:
            return None
        
        res = []
        q = deque()
        q.append(root)
        
        while q:
            level = []
            n = len(q)

            for i in range(n):
                node = q.popleft()
                level.append(node.val)

                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(level)

        return res