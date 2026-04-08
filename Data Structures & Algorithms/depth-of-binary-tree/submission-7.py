# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        
        stack = []
        stack.append([root, 1])
        depth = 0

        while stack:
            node, depthT = stack.pop()
            if node:
                depth = max(depthT, depth)
                stack.append([node.left, depthT+1])
                stack.append([node.right, depthT+1])

        return depth

