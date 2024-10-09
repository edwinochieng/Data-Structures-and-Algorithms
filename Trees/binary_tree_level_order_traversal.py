from collections import deque

class TreeNode:
    def __init__(self, val = 0 , left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self,root:TreeNode):
        res = []
        q = deque()
        q.append(root)
        
        while q:
            level = []
            n = len(q)

            for i in range(n):
                node = q.popleft()

                if node:
                    level.append(node)
                    q.append(node.left)
                    q.append(node.right)
            res.append(level)

        return res