# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #recrusice DFS
        # 1+ max depth of its left and right subtrees
        #for each node check recurivesly left subtree
        #recursively compute depth of right subtree
        #take max of two
        #add to current node

        #if root is null retunr 0
        #otherwide lefDepth = maxDepth(root.left)
        #right
        # return 1 + max(leftDepth, rightDepth)

        #base condition
        if not root:
            return 0

        #recursion
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)

    #return

        return 1 + max(leftDepth, rightDepth)
        