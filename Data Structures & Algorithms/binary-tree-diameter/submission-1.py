# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result = 0

        def recurse(curr):
            if curr == None:
                return 0

            L = recurse(curr.left)
            R = recurse(curr.right)

            self.result = max(self.result, L + R)
            return 1 + max(L,R)
        
        recurse(root)

        return self.result
            
