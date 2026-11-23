# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        #for a subroot to exist must be same tress as subtree of main tree
        #if subtree empty must be subtree
        if not subRoot: 
            return True
        #main root empty then subtree cannot be valid
        if not root and subRoot:
            return False
        #compare if same tree, 
        
        if self.isSameTree(root,subRoot):
            return True
        #if not the check sub trees left and right of root to compare with subRoot
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        #code for same tree
        #base case
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False

        if root.val != subRoot.val:
            return False
        #return and recursive call
        return self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right)

        #big o (n) time
        #space Big O(h) h height of tree n/2

        