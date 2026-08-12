# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def recurse(L, R):
            if L == None and R == None:
                return True
            elif L == None or R == None or L.val != R.val:
                return False
            
            return recurse(L.left, R.left) and recurse(L.right, R.right)

        if root == None:
            return False
        
        if root.left == True or root.right == True:
            return True 
        
        elif root.val == subRoot.val:
            boolVal = recurse(root, subRoot)
            if boolVal == True:
                return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)






