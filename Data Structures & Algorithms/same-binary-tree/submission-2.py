# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        #base 
        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        #have root and root equal so compare children

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right,q.right)

        #if both no roots return true
        #if one of not root retunr False
        #if both have root then compare if roots not equal return False
        #if root equal then need to compare the left and right nodes
        #time Big O(n) space Big o(n) n is number of nodes