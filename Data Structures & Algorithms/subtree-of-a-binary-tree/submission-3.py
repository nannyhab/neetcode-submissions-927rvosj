# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if subRoot == None:
            return True
        if root == None:
            return False
        if root.val == subRoot.val:
            if self.recurse(root, subRoot):
                return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    def recurse(self, L, R):
        if L == None and R == None:
            return True
        elif L == None or R == None or L.val != R.val:
            return False
        
        return self.recurse(L.left, R.left) and self.recurse(L.right, R.right)

        






