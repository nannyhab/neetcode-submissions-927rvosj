# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def recurse(curr):
            if curr == None:
                return 0

            L = recurse(curr.left)
            R = recurse(curr.right)

            if abs(L-R) > 1 or L == -1 or R == -1:
                return -1
            
            return 1 + max(L,R)
        
        rVal = recurse(root)

        if rVal == -1:
            return False
        return True