# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        #base case
        if not p and not q:
            return True
        if not p or not q:
            return False
        
        if p.val != q.val:
            return False

        #recursive calls

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right,q.right)

        #DFS
        #base root
            # if p and q not root return True
            #if not p or not q retunr False
            #if p vale != q vale return false
        # self.(p.left, q.left)
        #self.(right,right)
        #return recursive calls
        
        