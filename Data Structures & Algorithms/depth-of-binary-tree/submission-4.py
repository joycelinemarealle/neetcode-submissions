# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #base case
        if not root:
            return 0
        #recursive call 
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        length = 1 + max((left,right))
        return length

        #DFS
        #go to deeper
        #find the deeper node
        #return 1+ compare the left and right take the max
        #return the depth
       
        #basecase if node has no childreen reutnr 1 #edge if not root -< 0
        #recurisve call
        #return 1
        