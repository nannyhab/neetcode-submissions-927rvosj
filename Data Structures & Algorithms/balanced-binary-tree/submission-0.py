# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        self.height = 0
        self.falseFlag = False
    
        def recurse(curr):
            if curr == None:
                return 0
        
            L = recurse(curr.left)
            R = recurse(curr.right)

            print(f"L is {L} and R is {R}")
            if abs(L - R) > 1:
                self.falseFlag = True
                return -1

            return 1 + max(L,R)

        recurse(root)
        if self.falseFlag:
            return False
        return True




    

    