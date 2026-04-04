# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root == None:
            return []
        
        totalList = []
        queue = deque()
        queue.append(root)

        while queue:
            innerList = [] 
            qLen = len(queue)
            for i in range(qLen):
                node = queue.popleft()
                innerList.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            totalList.append(innerList)

        return totalList